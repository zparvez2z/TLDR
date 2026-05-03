#!/usr/bin/env python3
"""
Recover from failures: re-queue URLs for reprocessing or inspect summaries.

Usage:
    python scripts/recover.py --requeue <url>     # Add URL back to queue
    python scripts/recover.py --requeue-file <file>  # Re-queue multiple URLs from file
    python scripts/recover.py --inspect <category>   # List recent summaries in category
"""
import argparse
from pathlib import Path
from datetime import datetime

QUEUE_FILE = Path(__file__).parent.parent / "input" / "links-to-summarize.md"
KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"


def validate_url(url):
    """Check if URL is valid HTTP(S)."""
    return url.strip().startswith("http://") or url.strip().startswith("https://")


def requeue_url(url):
    """Add URL to processing queue."""
    if not validate_url(url):
        print(f"❌ Invalid URL: {url}")
        return False

    url = url.strip()

    # Check if already in queue
    if QUEUE_FILE.exists():
        with open(QUEUE_FILE, "r") as f:
            existing = [line.strip() for line in f]
        if url in existing:
            print(f"ℹ URL already in queue: {url}")
            return True

    # Append to queue
    with open(QUEUE_FILE, "a") as f:
        f.write(f"{url}\n")

    print(f"✓ Re-queued: {url}")
    return True


def requeue_file(filepath):
    """Re-queue multiple URLs from file."""
    try:
        with open(filepath, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return False

    count = 0
    for url in urls:
        if validate_url(url):
            requeue_url(url)
            count += 1
        else:
            print(f"⚠ Skipped invalid line: {url[:50]}")

    print(f"✓ Re-queued {count} URL(s)")
    return True


def inspect_category(category):
    """List recent summaries in a category."""
    category_dir = KNOWLEDGE_DIR / category
    if not category_dir.exists():
        print(f"❌ Category not found: {category}")
        print(f"Available: {', '.join(sorted([d.name for d in KNOWLEDGE_DIR.iterdir() if d.is_dir()]))}")
        return False

    files = sorted(
        category_dir.glob("*.md"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    if not files:
        print(f"No summaries in {category}")
        return True

    print(f"\n📂 {category} ({len(files)} summaries)")
    print("-" * 70)

    for f in files[:10]:
        mod_time = datetime.fromtimestamp(f.stat().st_mtime)
        size = f.stat().st_size

        # Extract title from file
        with open(f, "r") as file:
            content = file.read()
            title = "Unknown"
            for line in content.split("\n"):
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

        print(f"  {f.name}")
        print(f"    Title: {title}")
        print(f"    Size: {size} bytes | Modified: {mod_time.strftime('%Y-%m-%d %H:%M')}")
        print()

    return True


def main():
    parser = argparse.ArgumentParser(description="Recover from failures and re-queue URLs.")
    parser.add_argument(
        "--requeue", type=str, metavar="URL", help="Re-queue a single URL"
    )
    parser.add_argument(
        "--requeue-file", type=str, metavar="FILE", help="Re-queue URLs from file"
    )
    parser.add_argument(
        "--inspect",
        type=str,
        metavar="CATEGORY",
        help="Inspect recent summaries in category",
    )

    args = parser.parse_args()

    if args.requeue:
        requeue_url(args.requeue)
    elif args.requeue_file:
        requeue_file(args.requeue_file)
    elif args.inspect:
        inspect_category(args.inspect)
    else:
        print("❌ Provide --requeue, --requeue-file, or --inspect")
        parser.print_help()


if __name__ == "__main__":
    main()
