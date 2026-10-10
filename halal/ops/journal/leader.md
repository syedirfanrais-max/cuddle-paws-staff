# Journal: leader

Newest entries are at the bottom. Written with ops/journal/note.py.

## 2026-10-10 14:11 IST Project foundation set up

**What was done**
- Phase 1 competitor study (9 Oct), reported in chat and saved to `docs/research/phase1-competitor-study.md`.
- Read the EveryNearby handover (uploaded by Irfan; copy at `docs/handover/HANDOVER-NEW-SITE.md`).
- Set up this project folder inside the `cuddle-paws-staff` repository: `CLAUDE.md` (rules), `PRODUCT.md` (decided vs open), `ops/team/TEAM.md`, `ops/journal/README.md`, and three tools: `ops/team/tell.py`, `ops/journal/note.py`, `ops/progress/task.py`. `.gitignore` keeps secrets, backups and bulk data out.
- Seeded the task log with the first tasks; "Needs you" holds Irfan's decisions.

**Where**
- Everything is under `halal/` on branch `ccr-ac5d3aa9-2ek23x`.

**How it works**
- The three tools are rewritten from the handover's description, not copied (this cloud session cannot see `C:\Claude`). Plain Python, standard library only. Time stamps come from code in India time (UTC+5:30), set in `SITE_TZ` at the top of each script.
- Task streams and owners are lists at the top of `task.py`; add an owner there when a new bot exists.

**How it was checked**
- Ran all three tools on a throwaway copy: add, read, list, done, needs-you, and the error cases (missing sender, missing body, unknown task number, unknown stream). All behaved as expected.

**What is left**
- Irfan's answers to the first round of questions (task 2), name and domain (task 3), bot structure (tasks 4 and 5), halal definitions (tasks 6 and 7), OpenStreetMap decision (task 8), mock-ups (task 9), own repository (task 10).
- Not read, because this session cannot reach his computer: `MEMORY.md` and EveryNearby's model files (`TEAM.md`, `DEVELOPER-BRIEF.md`, `DEVELOPER-KNOWLEDGE.md`, `TESTER-BRIEF.md`). Read them when a session runs on his computer, and reconcile the tools with EveryNearby's originals.
- Saved memory for this project not written yet (the memory folder is on his computer).

**Irfan's decisions**
- 10 Oct 2026, on reading the handover: "lets build the halal website.... lets set the operational foundation first."
- 10 Oct 2026: "grill me with questions until you are clear with the plan"
- 10 Oct 2026: "build here first" (taken to mean: work in this cloud session and this repository before anything is bought).

## 2026-10-10 14:25 IST Handover to a session on Irfan's computer

**What was done**
- Irfan asked to move the project from this cloud session to his computer. Wrote `docs/handover/HANDOVER-TO-LOCAL.md`: where the files are, the first steps for the local session (copy `halal/` to `C:\Claude\halal`, start git, check the tools, read memory and EveryNearby's model files read only, save the project memory), and the nine open questions with recommendations.
- Added a task for the move.

**What is left**
- The local session does the steps in the handover. This cloud session stops making changes once the local copy is confirmed.

**Irfan's decisions**
- 10 Oct 2026: "make this session remote", then "move from cloud to local competeley".
