#!/usr/bin/env python3
"""Move generated daily-topic files into their intended categories.

The model can choose a reasonable but different category. For the daily learning
tracks, the source list is the source of truth:
- input/daily-machine-learning.md -> knowledge/Machine-Learning
- input/daily-system-design.md -> knowledge/System-Design
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "knowledge"
DAILY_CATEGORY_FILES = {
    "Machine-Learning": ROOT / "input" / "daily-machine-learning.md",
    "System-Design": ROOT / "input" / "daily-system-design.md",
}


def read_urls(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip().startswith(("http://", "https://"))
    }


def source_url(md_file: Path) -> str | None:
    try:
        for line in md_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("source_url:"):
                return line.split(":", 1)[1].strip()
    except UnicodeDecodeError:
        return None
    return None


def main() -> None:
    preferred_category_by_url = {}
    for category, url_file in DAILY_CATEGORY_FILES.items():
        for url in read_urls(url_file):
            preferred_category_by_url[url] = category

    if not preferred_category_by_url or not KNOWLEDGE_DIR.exists():
        print("No daily category rules to apply.")
        return

    moved = 0
    for md_file in list(KNOWLEDGE_DIR.rglob("*.md")):
        url = source_url(md_file)
        target_category = preferred_category_by_url.get(url or "")
        if not target_category:
            continue

        target_dir = KNOWLEDGE_DIR / target_category
        target_path = target_dir / md_file.name
        if md_file == target_path:
            continue

        target_dir.mkdir(parents=True, exist_ok=True)
        if target_path.exists():
            print(f"Target already exists, leaving source in place: {target_path}")
            continue

        md_file.replace(target_path)
        moved += 1
        print(f"Moved {md_file} -> {target_path}")

    if moved == 0:
        print("No daily knowledge files needed category moves.")
    else:
        print(f"Moved {moved} daily knowledge file(s) to intended categories.")


if __name__ == "__main__":
    main()
