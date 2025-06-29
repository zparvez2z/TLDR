import os
import pathlib
import json
import google.generativeai as genai
from google.generativeai.types import Tool

def call_gemini_api(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    url_context_tool = Tool(url_context={}) # Enable URL context tool
    response = model.generate_content(
        prompt,
        tools=[url_context_tool]
    )
    return response.text

def build_prompt(url):
    return f'''
You are an expert summarizer and classifier. Analyze the content at the URL {url} and return a clean JSON object with these fields:
- "title": a concise title for the content.
- "summary": a 3-5 sentence summary.
- "category": a single, appropriate category for the content (e.g., "Software-Engineering", "Machine-Learning").
- "filename": a descriptive, kebab-case filename ending in .md (e.g., "understanding-async-python.md").
- "author": the author, if found, otherwise "Unknown".
- "date": the publication date, if found, otherwise "Unknown".

URL: {url}
'''

def save_markdown(data, category_dir, url):
    category_dir.mkdir(parents=True, exist_ok=True)
    filename = data.get('filename', 'default-filename.md')
    md_path = category_dir / filename
    with open(md_path, 'w') as f:
        f.write(f"---\nsource_url: {url}\nauthor: {data.get('author','Unknown')}\ndate: {data.get('date','Unknown')}\n---\n\n# {data.get('title','No Title')}\n\n{data.get('summary','No summary available.')}")

def process_links():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return
    input_path = pathlib.Path('input/links-to-summarize.md')
    if not input_path.exists():
        print("Input file not found at input/links-to-summarize.md")
        return
    with open(input_path) as f:
        urls = [line.strip() for line in f if line.strip() and line.startswith('http')]
    if not urls:
        print("No valid URLs to process.")
        return
    for url in urls:
        print(f"Processing {url}...")
        prompt = build_prompt(url)
        try:
            result_text = call_gemini_api(prompt, api_key)
            # Clean the result to be valid JSON
            clean_json_str = result_text.strip().replace('```json', '').replace('```', '')
            data = json.loads(clean_json_str)
            category = data.get('category', 'Uncategorized')
            category_dir = pathlib.Path('knowledge') / category
            save_markdown(data, category_dir, url)
            print(f"Successfully processed and saved {url}")
        except Exception as e:
            print(f"Error processing {url}: {e}")
            print(f"Received from API: {result_text}")

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
    lines = ["# TLDR Knowledge Base\n", "\n## Knowledge Graph\n", "```mermaid\ngraph TD\n"]
    for cat, files in categories.items():
        lines.append(f"    {cat}(( {cat} ))\n")
        for f in files:
            node = f.stem.replace('-', '_')
            lines.append(f"    {cat} --> {node}\n")
    lines.append("```\n\n## All Knowledge\n")
    for cat, files in categories.items():
        lines.append(f"### {cat}\n")
        for f in files:
            rel_path = f.relative_to('.')
            lines.append(f"- [{f.stem.replace('-', ' ').title()}]({rel_path})\n")
        lines.append("\n")
    with open('README.md', 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    process_links()
