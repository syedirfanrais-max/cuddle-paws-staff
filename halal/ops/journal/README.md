# Journals

One journal per bot: `ops/journal/<bot>.md`. Written for the next Claude, or the
same one after a compact. Add entries with `note.py`; never edit old entries.

## What each entry holds

Use these headings, and leave out any that do not apply:

- **What was done** — in plain words.
- **Where** — files, pages, commands.
- **How it works** — enough for the next bot to change it safely.
- **How it was checked** — what was run or looked at, and the result.
- **What is left** — open ends, known problems.
- **Irfan's decisions** — quoted in his own words, with the date.

## Rules

- Write the entry to a file with the file tools first, then run
  `python ops/journal/note.py <bot> "title" --file that-file.md`.
- Time stamps come from the script, never typed by hand.
- No secrets, ever.
- Read your own last entries when you start: `python ops/journal/note.py <bot> --last 3`.
