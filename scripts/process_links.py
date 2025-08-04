import os
import pathlib
import json
from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SummaryOutput(BaseModel):
    title: str
    summary: str
    category: str
    filename: str
    author: Optional[str] = "Unknown"
    date: Optional[str] = None


def call_gemini_api(prompt, url, api_key):

    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-pro"
    tools = [types.Tool(url_context=types.UrlContext())]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
    )
    # Always include the URL in the prompt text
    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
    ]
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Log the full Gemini API response for debugging
    print("\n[DEBUG] Gemini API raw response:")
    try:
        import pprint
        pprint.pprint(response.__dict__)
    except Exception:
        print(response)

    # Parse the response text as JSON with better error handling
    try:
        json_str = response.text.strip()
        # Handle various JSON formatting cases
        if '```json' in json_str:
            # Extract JSON from code block
            start = json_str.find('```json') + 7
            end = json_str.find('```', start)
            if end == -1:  # No closing code block found
                json_str = json_str[start:]
            else:
                json_str = json_str[start:end]
        elif '{' in json_str:
            # Extract JSON between first { and last }
            start = json_str.find('{')
            end = json_str.rfind('}') + 1
            json_str = json_str[start:end]
            
        json_str = json_str.strip()
        if not json_str:
            raise ValueError("Empty JSON string")
            
        data = json.loads(json_str)
        
        # Ensure all required fields are present with defaults
        data.setdefault('author', 'Unknown')
        if not data.get('date'):
            data['date'] = datetime.now().strftime('%d-%m-%Y')
            
        # Convert category to kebab-case for consistency
        if 'category' in data:
            data['category'] = data['category'].replace(' ', '-')
            
        # Ensure filename ends with .md and is in kebab-case
        if 'filename' in data and not data['filename'].endswith('.md'):
            data['filename'] = data['filename'].strip().replace(' ', '-').lower()
            if not data['filename'].endswith('.md'):
                data['filename'] += '.md'
                
        return SummaryOutput(**data)
    except Exception as e:
        print(f"Error parsing JSON response: {e}")
        print(f"Raw response: {response.text}")
        return None

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

def process_links():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return
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
    for url in urls:
        print(f"Processing {url}...")
        prompt = build_prompt(url, existing_categories)
        result = None
        try:
            result = call_gemini_api(prompt, url, api_key)
            if not result:
                print(f"Error: Empty response from API for {url}")
                continue
            category = getattr(result, 'category', 'Uncategorized')
            category_dir = pathlib.Path('knowledge') / category
            save_markdown(result, category_dir, url)
            print(f"Successfully processed and saved {url}")
        except Exception as e:
            print(f"Error processing {url}: {e}")
            print(f"Received from API: {result}")

    # Clear input file after processing all URLs
    open(input_path, 'w').close()
    print("Cleared input file.")
    update_readme()
    print("README updated.")

def update_readme():
    knowledge_dir = pathlib.Path('knowledge')
    if not knowledge_dir.exists():
        return
    categories = {}
    for cat_dir in knowledge_dir.iterdir():
        if cat_dir.is_dir():
            categories[cat_dir.name] = [f for f in cat_dir.glob('*.md')]

    auto_lines = [
        '<!-- TLDR-AUTO-START -->\n',
        '## Overview\n',
        '```mermaid\ngraph TD\n'
    ]
    for cat, files in categories.items():
        auto_lines.append(f"    {cat}(( {cat} ))\n")
        for f in files:
            node = f.stem.replace('-', '_')
            auto_lines.append(f"    {cat} --> {node}\n")
    auto_lines.append("```\n\n## Read the summaries\n")
    for cat, files in categories.items():
        auto_lines.append(f"### {cat}\n")
        for f in files:
            rel_path = f.relative_to('.')
            auto_lines.append(f"- [{f.stem.replace('-', ' ').title()}]({rel_path})\n")
        auto_lines.append("\n")
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
