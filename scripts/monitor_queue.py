#!/usr/bin/env python3
"""
Monitor queue status and provide recovery commands.

Usage:
    python scripts/monitor_queue.py           # Show queue status
    python scripts/monitor_queue.py --clear   # Clear queue after full success
    python scripts/monitor_queue.py --rollback N  # Restore last N commits
"""
import argparse
import os
import sys
from pathlib import Path
from datetime import datetime
import subprocess

QUEUE_FILE = Path(__file__).parent.parent / "input" / "links-to-summarize.md"
KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"


def get_queue_status():
    """Return queue status: count, first URL, last modified."""
    if not QUEUE_FILE.exists():
        return 0, None, None

    with open(QUEUE_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip().startswith("http")]

    if not urls:
        return 0, None, QUEUE_FILE.stat().st_mtime

    mod_time = datetime.fromtimestamp(QUEUE_FILE.stat().st_mtime)
    return len(urls), urls[0], mod_time


def get_summary_count():
    """Return total summaries generated."""
    if not KNOWLEDGE_DIR.exists():
        return 0
    return len(list(KNOWLEDGE_DIR.rglob("*.md")))


def print_status():
    """Print current queue and knowledge status."""
    queue_count, first_url, mod_time = get_queue_status()
    summary_count = get_summary_count()

    print("=" * 70)
    print("QUEUE STATUS")
    print("=" * 70)

    if queue_count == 0:
        print("✓ Queue is EMPTY (all URLs processed successfully)")
    else:
        print(f"⚠ Queue has {queue_count} URL(s) pending:")
        print(f"  First: {first_url}")
        if mod_time:
            print(f"  Last modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"\n📚 Knowledge base: {summary_count} summaries generated")

    if queue_count > 0:
        print("\nRECOVERY OPTIONS:")
        print(f"  • Resume processing:     python scripts/process_links.py")
        print(f"  • View queue:            cat {QUEUE_FILE}")
        print(f"  • Force clear queue:     python scripts/monitor_queue.py --clear")
        print(f"  • Rollback commits:      git log --oneline {QUEUE_FILE} | head -5")


def clear_queue():
    """Clear queue (only if user confirms)."""
    count, _, _ = get_queue_status()
    if count == 0:
        print("Queue is already empty.")
        return

    response = input(f"Clear {count} pending URL(s)? [y/N]: ").lower()
    if response == "y":
        QUEUE_FILE.write_text("")
        print(f"✓ Queue cleared. {count} URL(s) discarded.")
    else:
        print("Cancelled.")


def rollback_commits(count=1):
    """Show last N commits for rollback."""
    print(f"Last {count} commit(s) affecting {QUEUE_FILE.name}:")
    cmd = ["git", "log", "--oneline", "-n", str(count + 1), str(QUEUE_FILE)]
    try:
        subprocess.run(cmd, cwd=QUEUE_FILE.parent.parent)
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Monitor queue status and provide recovery commands."
    )
    parser.add_argument(
        "--clear", action="store_true", help="Clear the queue after confirming"
    )
    parser.add_argument(
        "--rollback",
        type=int,
        metavar="N",
        help="Show last N commits for rollback",
    )

    args = parser.parse_args()

    if args.clear:
        clear_queue()
    elif args.rollback:
        rollback_commits(args.rollback)
    else:
        print_status()


if __name__ == "__main__":
    main()
