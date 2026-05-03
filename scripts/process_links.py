import pathlib
import re
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urlparse

import requests

try:
    from .model_adapter import ModelAdapter, TransientAPIError
except ImportError:
    from model_adapter import ModelAdapter, TransientAPIError


def write_remaining_queue(input_path, remaining_urls):
    with open(input_path, 'w') as f:
        if remaining_urls:
            f.write('\n'.join(remaining_urls) + '\n')


class PageTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_text_block = False
        self.in_title = False
        self.in_author_block = False
        self.in_personname = False
        self.text_parts = []
        self.title_parts = []
        self.author_parts = []
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'div' and any(name == 'class' and 'ltx_authors' in value for name, value in attrs):
            self.in_author_block = True
        if tag == 'span' and any(name == 'class' and 'ltx_personname' in value for name, value in attrs):
            self.in_personname = True
        if tag in {'p', 'li', 'blockquote', 'h1', 'h2', 'h3'}:
            self.in_text_block = True
        if tag == 'meta':
            key = attr_map.get('name') or attr_map.get('property')
            content = attr_map.get('content')
            if key and content:
                key = key.lower()
                if key == 'citation_author':
                    self.meta.setdefault(key, []).append(content.strip())
                else:
                    self.meta[key] = content.strip()

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'div' and self.in_author_block:
            self.in_author_block = False
        if tag == 'span' and self.in_personname:
            self.in_personname = False
        if tag in {'p', 'li', 'blockquote', 'h1', 'h2', 'h3'}:
            self.in_text_block = False

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return
        if self.in_title:
            self.title_parts.append(text)
        elif self.in_personname or self.in_author_block:
            self.author_parts.append(text)
        elif self.in_text_block:
            self.text_parts.append(text)


def _clean_whitespace(value):
    return re.sub(r'\s+', ' ', value or '').strip()


def _extract_generic_page_data(response_text, max_chars=10000):
    extractor = PageTextExtractor()
    extractor.feed(response_text)

    title = _clean_whitespace(' '.join(extractor.title_parts))
    meta = extractor.meta
    authors = meta.get('citation_author') or meta.get('author') or ['Unknown']
    if isinstance(authors, str):
        authors = [authors]

    title = title or meta.get('citation_title') or meta.get('og:title') or 'Unknown title'
    date = meta.get('citation_publication_date') or meta.get('article:published_time') or meta.get('pubdate') or ''
    abstract = meta.get('description') or meta.get('og:description') or ''

    text_body = _clean_whitespace(' '.join(extractor.text_parts))
    if len(text_body) > max_chars:
        text_body = text_body[:max_chars].rsplit(' ', 1)[0] + '...'

    context_lines = [
        f'Page title: {title}',
        f'Authors: {", ".join(authors)}',
    ]
    if date:
        context_lines.append(f'Date: {date}')
    if abstract:
        context_lines.append(f'Abstract: {abstract}')
    if text_body:
        context_lines.append(f'Visible text excerpt: {text_body}')

    return {
        'context': '\n'.join(context_lines),
        'title': title,
        'authors': authors,
        'date': date,
    }


def _extract_arxiv_page_data(response_text, max_chars=10000):
    generic = _extract_generic_page_data(response_text, max_chars=max_chars)
    # Be permissive: match the ltx_authors div content until the closing </div>
    # (some arXiv HTML uses <br class="ltx_break"> without a trailing slash).
    authors_block = re.search(r'<div[^>]*class=["\'][^"\']*ltx_authors[^"\']*["\'][^>]*>(.*?)</div>', response_text, re.S)
    if authors_block:
        author_line = authors_block.group(1)
        # remove footnote superscripts and any remaining tags
        author_line = re.sub(r'<sup.*?</sup>', '', author_line, flags=re.S)
        author_line = re.sub(r'<[^>]+>', '', author_line)
        author_line = author_line.replace('\xa0', ' ')
        # authors are often separated by larger whitespace or repeated spacing
        raw_parts = [part.strip() for part in re.split(r'\s{2,}|\u2003|\u00A0|,\s*', author_line) if part.strip()]
        
        # Filter: check if token is likely an author name
        def is_likely_author_name(token):
            # Reject if contains URLs, code labels, institutions, HTML-like tags
            if re.search(r'http|code:|project page|university|affiliat|\[|\]|mailto:|@|<|>', token, re.I):
                return False
            # Reject if contains LaTeX symbols, math mode, or excessive punctuation
            if re.search(r'\\|\{|\}|\$|\^|_|boldsymbol|footnotemark|footnote', token):
                return False
            # Reject if purely numeric or decimal
            if re.match(r'^[\d.]+$', token):
                return False
            # Reject if too short (< 2 chars) or too long (> 100 chars)
            if len(token) < 2 or len(token) > 100:
                return False
            # Heuristic: reasonable name has 1-6 words, each mostly letters/hyphens/apostrophes
            words = token.split()
            if len(words) > 6:
                return False
            for word in words:
                # Each word should be mostly letters (allow hyphens, apostrophes, dots)
                if not re.match(r"^[a-z\'\-\.]+$", word, re.I):
                    return False
            return True
        
        visible_authors = [p for p in raw_parts if is_likely_author_name(p)]
        if visible_authors:
            generic['authors'] = visible_authors
            # update the PAGE CONTEXT authors line if present
            generic['context'] = re.sub(r'Authors: .*', f"Authors: {', '.join(visible_authors)}", generic['context'])

    return generic


def is_extraction_quality_poor(page_info, url=None, threshold_text_chars=100):
    """Detect if page extraction quality is poor (e.g., mostly LaTeX artifacts, no useful content)."""
    domain = urlparse(url).netloc.lower() if url else ''
    authors = page_info.get('authors') or []
    context = page_info.get('context', '')

    # Basic signal checks
    has_title = bool(page_info.get('title')) and page_info['title'].lower() != 'unknown title'
    has_author = bool(authors) and authors[0] != 'Unknown'
    has_content = len(context) > threshold_text_chars

    # Suspicious author artifacts (LaTeX/math fragments, numeric garbage)
    suspicious_author = False
    for author in authors:
        if re.search(r'\\|\{|\}|\$|\^|_|boldsymbol|footnotemark|footnote', author, re.I):
            suspicious_author = True
            break
        if re.match(r'^[\d.]+$', author):
            suspicious_author = True
            break

    # arXiv pages should fall back if author extraction is missing or looks broken.
    if 'arxiv.org' in domain and (not has_author or suspicious_author):
        return True

    # Quality is poor if we're missing at least 2 of the 3 generic signals.
    signals = [has_title, has_author, has_content]
    return sum(signals) <= 1


def get_raw_html_chunk(url, max_chars=5000):
    """Fetch raw HTML and return a sanitized chunk for fallback use."""
    try:
        headers = {
            'User-Agent': 'tldr-link-summarizer/1.0 (+https://github.com/zparvez2z/TLDR)',
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        html = response.text
        # Remove script/style tags to reduce noise
        html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S | re.I)
        html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.S | re.I)
        # Truncate
        if len(html) > max_chars:
            html = html[:max_chars] + '\n... [truncated]'
        return html
    except Exception as e:
        return f'(Could not fetch raw HTML: {e})'



def fetch_page_context(url, max_chars=10000):
    headers = {
        'User-Agent': 'tldr-link-summarizer/1.0 (+https://github.com/zparvez2z/TLDR)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    response = requests.get(url, headers=headers, timeout=45)
    response.raise_for_status()

    domain = urlparse(url).netloc.lower()
    if 'arxiv.org' in domain:
        return _extract_arxiv_page_data(response.text, max_chars=max_chars)
    return _extract_generic_page_data(response.text, max_chars=max_chars)

def build_prompt(url, page_context=None, existing_categories=None):
    if existing_categories is None:
        existing_categories = []

    category_prompt = "a single category that best fits the content (e.g., Software-Engineering, Machine-Learning, etc.)."
    is_fallback = "[FALLBACK MODE] " in (page_context or "")
    
    if existing_categories:
        category_prompt = f"a single category from this list if a good fit exists, otherwise create a new relevant one: {', '.join(existing_categories)}"

    prompt_prefix = "⚠️ [Note: Using fallback raw HTML due to extraction difficulties]\n" if is_fallback else ""
    
    return f'''
{prompt_prefix}
You are an intelligent assistant that analyzes web content and returns structured data.
Analyze the webpage at the given URL and return ONLY a single, valid JSON object with the following fields:

{{
    "title": "A clear, concise title for the content.",
    "summary": "A concise summary (3-5 sentences) followed by a bulleted list of the most important key points and takeaways.",
    "category": "{category_prompt}",
    "filename": "A descriptive kebab-case filename ending in .md (e.g., understanding-async-python.md).",
    "author": "The author's name if found, otherwise 'Unknown'.",
    "date": "The publication date in DD-MM-YYYY format if found, otherwise leave blank."
}}

Do not include any explanatory text, markdown formatting like ```json, or anything outside of the JSON object itself.

URL: "{url}"

PAGE CONTEXT:
{page_context or 'No extracted page context available.'}
'''

def save_markdown(data, category_dir, url, source_metadata=None):
    category_dir.mkdir(parents=True, exist_ok=True)
    filename = data.filename if hasattr(data, 'filename') else data.get('filename', 'default-filename.md')
    source_authors = (source_metadata or {}).get('authors') or []
    source_title = (source_metadata or {}).get('title')
    source_date = (source_metadata or {}).get('date') or ''

    author = getattr(data, 'author', 'Unknown')
    if (not author or author == 'Unknown') and source_authors:
        author = ', '.join(source_authors)

    date_val = getattr(data, 'date', None) or source_date or datetime.now().strftime('%d-%m-%Y')
    title = getattr(data, 'title', 'No Title')
    if source_title and title.strip().lower() != source_title.strip().lower():
        title = source_title

    md_path = category_dir / filename
    with open(md_path, 'w') as f:
        f.write(f"---\nsource_url: {url}\nauthor: {author}\ndate: {date_val}\n---\n\n# {title}\n\n{getattr(data, 'summary', 'No summary available.')}")


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.strptime(value.strip(), '%d-%m-%Y')
    except Exception:
        try:
            return datetime.strptime(value.strip(), '%Y-%m-%d')
        except Exception:
            return None


def title_from_stem(stem):
    return stem.replace('-', ' ').title()


def collect_entries(knowledge_dir):
    categories = {}
    all_entries = []

    for cat_dir in knowledge_dir.iterdir():
        if not cat_dir.is_dir():
            continue

        entries = []
        for f in sorted(cat_dir.glob('*.md')):
            rel_path = f.relative_to('.')
            date_value = ''
            try:
                for line in f.read_text().splitlines():
                    if line.startswith('date:'):
                        date_value = line.split(':', 1)[1].strip()
                        break
            except Exception:
                pass

            entry = {
                'category': cat_dir.name,
                'title': title_from_stem(f.stem),
                'path': rel_path,
                'date': date_value,
                'parsed_date': parse_date(date_value),
            }
            entries.append(entry)
            all_entries.append(entry)

        entries.sort(key=lambda item: (item['parsed_date'] is not None, item['parsed_date'] or datetime.min, item['title']), reverse=True)
        categories[cat_dir.name] = entries

    return categories, all_entries

def process_links():
    adapter = ModelAdapter()
    input_path = pathlib.Path('input/links-to-summarize.md')
    if not input_path.exists():
        print("Input file not found at input/links-to-summarize.md")
        return

    # Get existing categories to guide the model
    knowledge_dir = pathlib.Path('knowledge')
    existing_categories = [d.name for d in knowledge_dir.iterdir() if d.is_dir()] if knowledge_dir.exists() else []

    with open(input_path) as f:
        urls = [line.strip() for line in f if line.strip() and line.startswith('http')]
    if not urls:
        print("No valid URLs to process.")
        return

    import time
    stop_and_preserve_queue = False
    for idx, url in enumerate(urls):
        print(f"Processing {url}...")
        try:
            page_info = fetch_page_context(url)
        except Exception as e:
            print(f"Error fetching page context for {url}: {e}")
            write_remaining_queue(input_path, urls[idx:])
            print(f"Preserved remaining links in {input_path}")
            stop_and_preserve_queue = True
            break

        # Check extraction quality and fallback to raw HTML if poor
        if is_extraction_quality_poor(page_info, url=url):
            print("  → Extraction quality poor, using fallback (raw HTML chunk)")
            raw_html = get_raw_html_chunk(url)
            page_info['context'] = f"[FALLBACK MODE] Raw HTML excerpt:\n{raw_html}"

        prompt = build_prompt(url, page_info.get('context'), existing_categories)
        result = None
        try:
            result = adapter.generate_summary(prompt, url)
            if not result:
                print(f"Error: Empty response from API for {url}")
                continue
            category = getattr(result, 'category', 'Uncategorized')
            category_dir = pathlib.Path('knowledge') / category
            save_markdown(result, category_dir, url, page_info)
            print(f"Successfully processed and saved {url}")
        except NotImplementedError as ne:
            print(f"Adapter not implemented: {ne}")
            print("Skipping further processing until adapter is configured.")
            write_remaining_queue(input_path, urls[idx:])
            print(f"Preserved remaining links in {input_path}")
            stop_and_preserve_queue = True
            break
        except TransientAPIError as e:
            print(f"Transient API error: {e}")
            write_remaining_queue(input_path, urls[idx:])
            print(f"Preserved remaining links in {input_path}")
            stop_and_preserve_queue = True
            break
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "quota" in str(e).lower():
                print("API quota exceeded. Stopping processing.")
                write_remaining_queue(input_path, urls[idx:])
                print(f"Remaining unprocessed links saved in {input_path}")
                stop_and_preserve_queue = True
                break
            print(f"Error processing {url}: {e}")
            print(f"Received from API: {result}")
        time.sleep(3)  # Add delay between processing links

    if not stop_and_preserve_queue:
        # Clear input file after processing all URLs
        open(input_path, 'w').close()
        print("Cleared input file.")
    update_readme()
    print("README updated.")

def update_readme():
    knowledge_dir = pathlib.Path('knowledge')
    if not knowledge_dir.exists():
        return
    categories, all_entries = collect_entries(knowledge_dir)
    category_names = sorted(categories.keys())
    recent_entries = sorted(
        all_entries,
        key=lambda item: (item['parsed_date'] is not None, item['parsed_date'] or datetime.min, item['title']),
        reverse=True,
    )[:8]

    auto_lines = [
        '<!-- TLDR-AUTO-START -->\n',
        '## Category dashboard\n',
        '| Category | Count | Latest | Browse |\n',
        '| --- | ---: | --- | --- |\n',
    ]
    for cat in category_names:
        entries = categories[cat]
        count = len(entries)
        latest = entries[0] if entries else None
        latest_text = f"[{latest['title']}]({latest['path']})" if latest else '—'
        browse_text = f"[{cat}](#browse-by-category)"
        auto_lines.append(f"| {cat} | {count} | {latest_text} | {browse_text} |\n")
    auto_lines.append("\n")

    if recent_entries:
        auto_lines.append('## Recent additions\n')
        for entry in recent_entries:
            date_suffix = f" — {entry['date']}" if entry['date'] else ''
            auto_lines.append(f"- [{entry['title']}]({entry['path']}) · {entry['category']}{date_suffix}\n")
        auto_lines.append("\n")

    auto_lines.append('## Browse by category\n')
    for cat in category_names:
        entries = categories[cat]
        auto_lines.append(f"<details>\n<summary>{cat} ({len(entries)})</summary>\n\n")
        for entry in entries:
            date_suffix = f" — {entry['date']}" if entry['date'] else ''
            auto_lines.append(f"- [{entry['title']}]({entry['path']}){date_suffix}\n")
        auto_lines.append("\n</details>\n\n")
    auto_lines.append('<!-- TLDR-AUTO-END -->\n')

    # Read the current README
    readme_path = pathlib.Path('README.md')
    if readme_path.exists():
        with open(readme_path, 'r') as f:
            content = f.read()
    else:
        content = ''

    start_marker = '<!-- TLDR-AUTO-START -->'
    end_marker = '<!-- TLDR-AUTO-END -->'
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    auto_content = ''.join(auto_lines)

    if start_idx != -1 and end_idx != -1:
        # Replace only the auto section
        before = content[:start_idx]
        after = content[end_idx + len(end_marker):]
        new_content = before + auto_content + after
    else:
        # Markers not found, append auto section at end
        if content and not content.endswith('\n'):
            content += '\n'
        new_content = content + auto_content

    with open('README.md', 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    process_links()
