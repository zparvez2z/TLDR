import os
import pathlib
import json
import google.generativeai as genai
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


def call_gemini_api(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')  # Using gemini-2.5-pro for more reliable structured output
    response = model.generate_content(
        prompt,
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ],
        generation_config={
            "temperature": 0.3,
            "top_p": 0.8,
            "top_k": 40
        }
    )
    
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
            data['date'] = datetime.now().strftime('%Y-%m-%d')
            
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

def build_prompt(url):
    return f'''
Analyze the webpage at {url} and return a JSON object with these fields:
{{
    "title": "a clear, concise title for the content",
    "summary": "a 3-5 sentence summary of the key points",
    "category": "a single category like Software-Engineering, Machine-Learning, Data-Science, etc.",
    "filename": "a descriptive kebab-case filename ending in .md (e.g. understanding-async-python.md)",
    "author": "the author's name if found, otherwise Unknown",
    "date": "the publication date in YYYY-MM-DD format if found, otherwise leave blank"
}}

Format your response as valid JSON that can be parsed. Do not include any other text or markdown formatting.
URL: {url}
'''

def save_markdown(data, category_dir, url):
    category_dir.mkdir(parents=True, exist_ok=True)
    filename = data.filename if hasattr(data, 'filename') else data.get('filename', 'default-filename.md')
    # Use current date if date is None or empty
    date_val = getattr(data, 'date', None) or datetime.now().strftime('%Y-%m-%d')
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
    with open(input_path) as f:
        urls = [line.strip() for line in f if line.strip() and line.startswith('http')]
    if not urls:
        print("No valid URLs to process.")
        return
    for url in urls:
        print(f"Processing {url}...")
        prompt = build_prompt(url)
        result = None
        try:
            result = call_gemini_api(prompt, api_key)
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
