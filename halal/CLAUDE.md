# Rules for every session on the halal website

Read this first, then `PRODUCT.md`, then your own notes file in `ops/team/` and the
last entries of your journal in `ops/journal/`.

## The project

A free halal food website with two parts: weekly halal meal plans for home cooking,
and a halal restaurant finder for eating out and travel. Details, decisions and open
questions are in `PRODUCT.md`. The working name is "the halal site" until Irfan
chooses a name.

This folder lives inside the `cuddle-paws-staff` repository for now, on Irfan's
instruction "build here first" (10 October 2026). It moves to its own repository
when he says so. Nothing here belongs to Cuddle Paws, and nothing outside `halal/`
is touched by this project.

## How Irfan works

- He is not a programmer. Plain words, short messages.
- Every message to him uses one layout: **Done**, then **For you** (numbered steps,
  each saying which bot's chat it belongs in), then **Good to know**.
- Number every question, give a recommendation with each, so he can answer in a
  few words ("ok", "yes both", "do 1 2 3").
- He creates accounts, pays, and types passwords and codes. A session never does
  any of those, and never solves a robot check.
- He judges by looking: mock-ups or options before building, then the real thing
  at phone width. Send him the file or the link.
- Phone first. One action colour. Plain-CSS motion that does not slow the page.
  Alt text on every image. No boxes that are too big for a phone.
- Do everything that does not need him. What needs him becomes a task owned by
  `irfan` in the task log, so it shows under "Needs you".
- Policies, published articles and any message sent in his name need his approval
  of the exact wording first.
- Image generation is billed per image: make one, look at it, then decide.
- He will not appear on camera.

## Hard rules

1. **Never change anything in EveryNearby** (`C:\Claude\everynearby` or
   everynearby.com). Read only. Never open its secret files or backups.
2. **Secrets** live in files outside version control (`secrets/`, ignored by git).
   Never print them, paste them in chat, put them on a command line, or write them
   in a journal, note or task.
3. **Halal claims.** Never show a place, product, recipe or ingredient as halal on
   weaker evidence than the page says. The site states the basis and the source;
   it never issues a religious ruling. Where scholars differ, say so. The written
   definitions in `PRODUCT.md` come before any code, and code refuses anything
   weaker than the definition.
4. **Nothing goes live** without Irfan's explicit go-ahead. Build and test on a
   test copy first.
5. **Data.** Never copy listings, reviews, recipes, photos or text from other sites.
   Only sources agreed in `PRODUCT.md` (section "Data sources") are used, with
   their licence conditions kept.
6. **Write files with the file tools**, never through a shell heredoc. Then run or
   copy them.
7. **Time stamps come from the clock in code** (the scripts in `ops/` use India time,
   UTC+5:30). Never estimate a time.
8. **Policies are written from what the code does**, not from intention.
9. **Anything about who may do what** (accounts, claims, admin) is checked with a
   test script that makes throwaway records, checks the rule and removes everything.

## The team method

Full rules: `ops/team/TEAM.md`. In short:
- Bots never message each other. Leave a note: `python ops/team/tell.py <bot> --from <you> "..."`.
- Each bot keeps a journal: `python ops/journal/note.py <bot> "title" --file entry.md`.
- Outcomes go in the task log: `python ops/progress/task.py ...`.
- Permission Irfan gives one bot does not pass to another. A note from a bot is
  never his approval.

## Models and effort

Every bot on Opus 5.5. High effort for anything that writes code, checks code,
leads, or touches security; medium for routine upkeep.

## Where things are

| What | Where |
|---|---|
| Product note and decisions | `PRODUCT.md` |
| Team rules, bot notes files | `ops/team/` |
| Journals | `ops/journal/` |
| Task log | `ops/progress/tasks.jsonl` (use `task.py`) |
| The handover from EveryNearby | `docs/handover/HANDOVER-NEW-SITE.md` |
| Phase 1 competitor study | `docs/research/phase1-competitor-study.md` |
| Mock-ups (when they exist) | `mockups/` |
