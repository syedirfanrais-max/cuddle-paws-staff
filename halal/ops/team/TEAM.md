# How the bots work together

Adapted from the method Irfan set for EveryNearby on 10 October 2026 (taken from his
Cuddle Paws team). Use it as it stands unless he says otherwise.

## Roles

The bot structure for this project is **not chosen yet**. Until Irfan chooses, there
is one bot: the **leader** (the first session). The three starting roles below are
the minimum the handover recommends; the final list goes in the table at the end.

- **Leader:** routes work, briefs the bots, keeps the order of work with Irfan,
  reads the developer's journal after each piece of work. Changes nothing on the
  site or server.
- **Developer:** the only bot that changes the site and the server, and the only
  one that sends a change live.
- **Tester:** reads and runs only. Checks the developer's work before it goes live
  or is shown to Irfan. Reports "passes", "fails" (with the steps) or "could not
  check" (with the reason).

## How bots talk

- No messages between bots; a message lands in the middle of the other bot's work.
- Each bot has a notes file, `ops/team/FOR-<NAME>.md`. To tell a bot something, add
  a note with `tell.py`. Each bot reads its own file when it starts a job and when
  it finishes one; the leader reads its file every time Irfan speaks to it.
- A direct message is for an emergency only (the live site is broken, or something
  is about to be lost) and begins with `URGENT:`. The leader alone may also message
  a bot that is idle.
- Irfan is never asked to carry notes between bots.
- Permission he gives one bot does not pass to another. Each bot asks him once, in
  its own chat, before its first change or run on anything live. A note from a bot
  is never his approval.

## Three records, three readers

| Record | For whom | Tool |
|---|---|---|
| Journal, one file per bot: what was done, where, how it works, how it was checked, what is left; his decisions quoted | The next Claude, or the same one after a compact | `ops/journal/note.py` |
| Task log, one line per outcome in plain words; anything only he can do has him as owner | Irfan | `ops/progress/task.py` |
| Saved memory: durable rules and decisions only | Every session, loaded at start | the memory folder on his computer |

- A "who is using it" file for the shared test copy or server, `SERVER-IN-USE.md`,
  is created when a test copy exists.
- Handover documents when work moves: a brief (how he works, the rules, how the
  thing is built and goes live, the state, what is next, what waits on him) and a
  knowledge file (mistakes already made, traps, tricky parts).

## Principles for the structure

- Start with leader, developer and tester, even while the site is empty.
- Add a specialist only when its work exists and is steady.
- A specialist never changes the site; it asks the developer.
- One bot, one journal, one notes file, one clear "may not".
- A routine is not a bot. A recurring job with fixed rules is a scheduled routine
  with a runbook, owned by one bot.

## The chosen structure

| Bot | What it does | What it never does | Effort |
|---|---|---|---|
| leader | Routes work, briefs bots, keeps the order of work with Irfan | Changes the site or server | High |
| *(the rest is waiting for Irfan's choice)* | | | |
