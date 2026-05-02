import pathlib
from datetime import datetime


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

        files = sorted(cat_dir.glob('*.md'))
        entries = []
        for f in files:
            rel_path = f.relative_to('.')
            date_value = None
            try:
                text = f.read_text()
                if 'date:' in text:
                    for line in text.splitlines():
                        if line.startswith('date:'):
                            date_value = line.split(':', 1)[1].strip()
                            break
            except Exception:
                pass

            parsed_date = parse_date(date_value)
            entry = {
                'category': cat_dir.name,
                'title': title_from_stem(f.stem),
                'path': rel_path,
                'date': date_value or '',
                'parsed_date': parsed_date,
            }
            entries.append(entry)
            all_entries.append(entry)

        entries.sort(key=lambda item: (item['parsed_date'] is not None, item['parsed_date'] or datetime.min, item['title']), reverse=True)
        categories[cat_dir.name] = entries

    return categories, all_entries

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
    
    print("README updated successfully!")

if __name__ == "__main__":
    update_readme()
