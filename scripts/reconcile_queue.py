#!/usr/bin/env python3
"""Reconcile queued URLs after processing.

This script protects the queue from silent model/API failures. It compares the
URLs selected for the current run with generated knowledge files. URLs that do
not appear in knowledge/*.md are written back to input/links-to-summarize.md.
URLs that do appear are appended to input/daily-processed.md.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE_FILE = ROOT / "input" / "links-to-summarize.md"
RUN_FILE = ROOT / "input" / "run-selected.md"
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


def unique_in_order(urls: list[str]) -> list[str]:
    seen = set()
    result = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            result.append(url)
    return result


def main() -> None:
    selected_urls = unique_in_order(read_urls(RUN_FILE))
    if not selected_urls:
        print("No run-selected URLs found; nothing to reconcile.")
        return

    generated_urls = read_knowledge_urls()
    succeeded = [url for url in selected_urls if url in generated_urls]
    failed = [url for url in selected_urls if url not in generated_urls]

    if failed:
        QUEUE_FILE.write_text("\n".join(failed) + "\n", encoding="utf-8")
        print("Restored failed URLs to queue:")
        for url in failed:
            print(f"- {url}")
    else:
        QUEUE_FILE.write_text("", encoding="utf-8")
        print("All selected URLs are present in knowledge files.")

    if succeeded:
        existing_done = set(read_urls(DONE_FILE))
        with DONE_FILE.open("a", encoding="utf-8") as done_file:
            for url in succeeded:
                if url not in existing_done:
                    done_file.write(url + "\n")
                    existing_done.add(url)
        print("Marked succeeded URLs as processed:")
        for url in succeeded:
            print(f"- {url}")

    RUN_FILE.write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
