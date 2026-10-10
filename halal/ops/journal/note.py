"""Add an entry to a bot's journal.

One journal per bot, ops/journal/<bot>.md. It is written for the next Claude
(or the same one after a compact): what was done, where, how it works, how it
was checked, what is left, and Irfan's decisions quoted in his own words.

Usage (run from the project folder):
    python ops/journal/note.py leader "Set up the project folder" --file entry.md
    python ops/journal/note.py developer "Shopping list grouping" --text "Short entry."
    python ops/journal/note.py leader --last 3      # show the last three entries

Write the entry to a file with the file tools first, then pass --file. Use the
headings in ops/journal/README.md. Never put secrets in a journal.
"""

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SITE_TZ = timezone(timedelta(hours=5, minutes=30), "IST")

JOURNAL_DIR = Path(__file__).resolve().parent


def now_text() -> str:
    return datetime.now(SITE_TZ).strftime("%Y-%m-%d %H:%M IST")


def journal_file(bot: str) -> Path:
    return JOURNAL_DIR / f"{bot.strip().lower()}.md"


def show_last(path: Path, count: int) -> None:
    if not path.exists():
        print("No journal yet.")
        return
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^(?=## \d{4}-\d{2}-\d{2} )", text)
    entries = [p for p in parts if p.startswith("## ")]
    for entry in entries[-count:]:
        print(entry.rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Add an entry to a bot's journal.")
    parser.add_argument("bot", help="whose journal, for example leader")
    parser.add_argument("title", nargs="?", help="a short title for the entry")
    parser.add_argument("--file", help="read the entry body from this file")
    parser.add_argument("--text", help="a short entry body given directly")
    parser.add_argument("--last", type=int, help="print the last N entries instead")
    args = parser.parse_args()

    path = journal_file(args.bot)

    if args.last:
        show_last(path, args.last)
        return 0

    if not args.title:
        parser.error("give the entry a title")
    if args.file:
        body = Path(args.file).read_text(encoding="utf-8").strip()
    elif args.text:
        body = args.text.strip()
    else:
        parser.error("give the entry body with --file or --text")
    if not body:
        parser.error("the entry is empty")

    if not path.exists():
        path.write_text(
            f"# Journal: {args.bot.strip().lower()}\n\n"
            "Newest entries are at the bottom. Written with ops/journal/note.py.\n",
            encoding="utf-8",
        )

    entry = f"\n## {now_text()} {args.title.strip()}\n\n{body}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Entry added to {path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
