# Handover: moving the halal site from the cloud session to Irfan's computer

Written by the first session (the leader, a cloud session) on 10 October 2026, for
the session that continues the project on Irfan's own computer. Irfan's words:
"move from cloud to local competeley".

## 1. Where everything is now

- All project files are in the `halal/` folder of the GitHub repository
  `syedirfanrais-max/cuddle-paws-staff`, on branch `ccr-ac5d3aa9-2ek23x`.
  The folder has nothing to do with Cuddle Paws; it was put there only because
  that was the repository this cloud session had.
- Nothing exists on any server. Nothing has been bought. No accounts exist for the
  new site.

## 2. First steps on Irfan's computer (do these in order)

1. **Copy the project down.** Clone the repository above, check out branch
   `ccr-ac5d3aa9-2ek23x`, and copy only the `halal/` folder to `C:\Claude\halal`
   (working name; it is renamed when Irfan picks the site's name). Do not copy
   anything else from that repository.
2. **Start version control there at once** (`git init` in `C:\Claude\halal`, first
   commit of everything). The `.gitignore` already keeps secrets, backups and bulk
   data out. Lesson 1 of the EveryNearby handover.
3. **Check the copy.** Run each tool once:
   - `python ops/progress/task.py list`: should show tasks 2 to 10 open.
   - `python ops/progress/task.py needs-you`: six tasks owned by Irfan.
   - `python ops/journal/note.py leader --last 1`: the "Project foundation set up" entry.
   - `python ops/team/tell.py leader --read`: the leader's (empty) notes file.
4. **Do what the cloud session could not** (it cannot see `C:\`):
   - Read `C:\Users\irfan\.claude\projects\C--Claude\memory\MEMORY.md`.
   - Read EveryNearby's model files, read only: `ops\team\TEAM.md`,
     `ops\journal\README.md`, `ops\team\DEVELOPER-BRIEF.md`,
     `DEVELOPER-KNOWLEDGE.md`, `TESTER-BRIEF.md`, and `PRODUCT.md`.
   - Compare our three tools (`ops/team/tell.py`, `ops/journal/note.py`,
     `ops/progress/task.py`) with EveryNearby's originals. They were rewritten from
     the handover's description, not copied. Keep ours or replace with copies of
     the originals, whichever is better, and say which in the journal.
   - Save one memory for this project and add its line to `MEMORY.md`.
   - **Never change anything in `C:\Claude\everynearby`. Never open its secret files
     or its `backups` folder.**
5. **Record the move.** Journal entry for the leader, and close task 10 in the task
   log once Irfan confirms the local copy works.
6. **Then carry on** with the open questions in section 3, in the layout
   Done / For you / Good to know.

## 3. Open questions waiting for Irfan (asked 10 October 2026, not yet answered)

Each with the first session's recommendation:

1. Launch order: meal planner, recipes, ingredient checker and Ramadan mode first,
   ready before Ramadan (about 8 February 2027); restaurant finder after. *Yes.*
2. Restaurant pages first in UK, Canadian and US cities; UAE and India hidden at
   first. *Yes.*
3. Name: does he have one? *Suggest ten, check free domains, he buys.*
4. EveryNearby: fully separate site, server and accounts. *Yes.*
5. Religious wording: he approves every halal label and ingredient answer; does he
   want a scholar or imam to review them too, and who?
6. Ingredient checker: where scholars differ, main answer cautious, other views
   noted. *Yes; a school-of-thought setting can come later.*
7. Recipe testing: he or his family cook the first 20 sample recipes; "tested in our
   kitchen" only when actually cooked. *Yes.*
8. Time stamps: India time like EveryNearby, or Dubai time? *India.*
9. Where the work lives: now answered by this move. Local folder
   `C:\Claude\halal` with version control; a private GitHub copy as off-computer
   backup is still recommended (ask him).

After his answers: propose two or three bot structures (handover section 8), then
mock-ups at phone width, before anything is bought.

## 4. What to read

| File | What it is |
|---|---|
| `CLAUDE.md` | Rules for every session |
| `PRODUCT.md` | Decided vs open, with recommendations |
| `ops/team/TEAM.md` | The team method |
| `ops/journal/leader.md` | The leader's journal |
| `ops/progress/tasks.jsonl` | The task log (use `task.py`) |
| `docs/research/phase1-competitor-study.md` | Competitor study, keyword demand, data sources |
| `docs/handover/HANDOVER-NEW-SITE.md` | The method handed over from EveryNearby |

## 5. Things the cloud session set up outside this folder

- An OpenSEO project "Halal food platform (research)", holding the keyword research.
  It is in Irfan's OpenSEO account and is reachable from any session.
- The `halal/` folder on the GitHub branch above. Once the local copy is confirmed,
  that branch can be left alone or deleted on Irfan's say-so; it is not merged into
  the repository's main branch.
