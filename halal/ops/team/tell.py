"""Leave a note for another bot.

Bots never message each other. To tell a bot something, add a note at the
bottom of its notes file, ops/team/FOR-<NAME>.md. Each bot reads its own file
when it starts a job and when it finishes one.

Usage (run from the project folder):
    python ops/team/tell.py developer --from leader "Please build the shopping list next."
    python ops/team/tell.py tester --from developer --file path/to/longer-note.md
    python ops/team/tell.py leader --read          # show the leader's notes

Write longer notes to a file with the file tools first, then pass --file.
Never put secrets in a note.
"""

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Time stamps come from the clock in code, never from an estimate.
SITE_TZ = timezone(timedelta(hours=5, minutes=30), "IST")

TEAM_DIR = Path(__file__).resolve().parent


def now_text() -> str:
    return datetime.now(SITE_TZ).strftime("%Y-%m-%d %H:%M IST")


def notes_file(bot: str) -> Path:
    return TEAM_DIR / f"FOR-{bot.strip().upper()}.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Leave a note for another bot.")
    parser.add_argument("to", help="the bot the note is for, for example developer")
    parser.add_argument("text", nargs="?", help="the note, in plain words")
    parser.add_argument("--from", dest="sender", help="the bot writing the note")
    parser.add_argument("--file", help="read the note from this file instead")
    parser.add_argument("--read", action="store_true", help="print the bot's notes file")
    args = parser.parse_args()

    path = notes_file(args.to)

    if args.read:
        if not path.exists():
            print(f"No notes file yet for {args.to}.")
            return 0
        print(path.read_text(encoding="utf-8"))
        return 0

    if not args.sender:
        parser.error("--from is required when leaving a note")
    if args.file:
        body = Path(args.file).read_text(encoding="utf-8").strip()
    elif args.text:
        body = args.text.strip()
    else:
        parser.error("give the note as text or with --file")
    if not body:
        parser.error("the note is empty")

    if not path.exists():
        path.write_text(
            f"# Notes for {args.to.strip().lower()}\n\n"
            "Read this file when you start a job and when you finish one.\n"
            "Newest notes are at the bottom.\n",
            encoding="utf-8",
        )

    entry = f"\n## {now_text()} from {args.sender.strip().lower()}\n\n{body}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Note added to {path.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
