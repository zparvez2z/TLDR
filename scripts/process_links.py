import os
import pathlib
import json
from datetime import datetime
from typing import Optional

try:
    from .model_adapter import ModelAdapter, TransientAPIError
    from .summary_model import SummaryOutput
except ImportError:
    from model_adapter import ModelAdapter, TransientAPIError
    from summary_model import SummaryOutput


def write_remaining_queue(input_path, remaining_urls):
    with open(input_path, 'w') as f:
        if remaining_urls:
            f.write('\n'.join(remaining_urls) + '\n')

def build_prompt(url, existing_categories=None):
    if existing_categories is None:
        existing_categories = []

    category_prompt = "a single category that best fits the content (e.g., Software-Engineering, Machine-Learning, etc.)."
    if existing_categories:
        category_prompt = f"a single category from this list if a good fit exists, otherwise create a new relevant one: {', '.join(existing_categories)}"

    return f'''
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
'''

def save_markdown(data, category_dir, url):
    category_dir.mkdir(parents=True, exist_ok=True)
    filename = data.filename if hasattr(data, 'filename') else data.get('filename', 'default-filename.md')
    # Use current date if date is None or empty
    date_val = getattr(data, 'date', None) or datetime.now().strftime('%d-%m-%Y')
    md_path = category_dir / filename
    with open(md_path, 'w') as f:
        f.write(f"---\nsource_url: {url}\nauthor: {getattr(data, 'author', 'Unknown')}\ndate: {date_val}\n---\n\n# {getattr(data, 'title', 'No Title')}\n\n{getattr(data, 'summary', 'No summary available.')}")


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
        prompt = build_prompt(url, existing_categories)
        result = None
        try:
            result = adapter.generate_summary(prompt, url)
            if not result:
                print(f"Error: Empty response from API for {url}")
                continue
            category = getattr(result, 'category', 'Uncategorized')
            category_dir = pathlib.Path('knowledge') / category
            save_markdown(result, category_dir, url)
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
                print(f"API quota exceeded. Stopping processing.")
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
