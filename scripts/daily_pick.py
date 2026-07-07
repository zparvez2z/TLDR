#!/usr/bin/env python3
"""Pick one Machine Learning URL and one System Design URL for the daily run."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ML_FILE = ROOT / "input" / "daily-machine-learning.md"
SD_FILE = ROOT / "input" / "daily-system-design.md"
QUEUE_FILE = ROOT / "input" / "links-to-summarize.md"
DONE_FILE = ROOT / "input" / "daily-processed.md"
KNOWLEDGE_DIR = ROOT / "knowledge"


def read_urls(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip().startswith(("http://", "https://"))
    ]


def read_knowledge_urls() -> set[str]:
    urls = set()
    if not KNOWLEDGE_DIR.exists():
        return urls
    for md_file in KNOWLEDGE_DIR.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line in text.splitlines():
            if line.startswith("source_url:"):
                urls.add(line.split(":", 1)[1].strip())
                break
    return urls


def first_unprocessed(source_urls: list[str], processed_urls: set[str]) -> str | None:
    for url in source_urls:
        if url not in processed_urls:
            return url
    return None


def main() -> None:
    processed_urls = set(read_urls(DONE_FILE)) | read_knowledge_urls()

    picks = [
        first_unprocessed(read_urls(ML_FILE), processed_urls),
        first_unprocessed(read_urls(SD_FILE), processed_urls),
    ]
    picks = [url for url in picks if url]

    if not picks:
        QUEUE_FILE.write_text("", encoding="utf-8")
        print("No new daily topics available.")
        return

    QUEUE_FILE.write_text("\n".join(picks) + "\n", encoding="utf-8")

    print("Queued daily topics:")
    for url in picks:
        print(f"- {url}")


if __name__ == "__main__":
    main()
