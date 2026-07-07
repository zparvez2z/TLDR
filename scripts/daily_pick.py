#!/usr/bin/env python3
"""Pick one Machine Learning URL and one System Design URL for the daily run.

The script reads curated source lists from input/daily-machine-learning.md and
input/daily-system-design.md, skips URLs already recorded in input/daily-processed.md,
and writes today's picks to input/links-to-summarize.md.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ML_FILE = ROOT / "input" / "daily-machine-learning.md"
SD_FILE = ROOT / "input" / "daily-system-design.md"
QUEUE_FILE = ROOT / "input" / "links-to-summarize.md"
DONE_FILE = ROOT / "input" / "daily-processed.md"


def read_urls(path: Path) -> list[str]:
    """Return HTTP(S) URLs from a Markdown/plain-text file."""
    if not path.exists():
        return []

    urls = []
    for line in path.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if value.startswith(("http://", "https://")):
            urls.append(value)
    return urls


def first_unprocessed(source_urls: list[str], processed_urls: set[str]) -> str | None:
    """Return the first URL that has not already been processed."""
    for url in source_urls:
        if url not in processed_urls:
            return url
    return None


def main() -> None:
    processed_urls = set(read_urls(DONE_FILE))

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

    with DONE_FILE.open("a", encoding="utf-8") as done_file:
        for url in picks:
            done_file.write(url + "\n")

    print("Queued daily topics:")
    for url in picks:
        print(f"- {url}")


if __name__ == "__main__":
    main()
