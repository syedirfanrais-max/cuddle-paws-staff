# Starting a new website the way EveryNearby was built

Written on 10 October 2026, 13:15 India time, by the EveryNearby leader (the session that built everynearby.com), for the
first session of Irfan's new halal website. It knows nothing yet; this is its starting point.

Irfan's words: "i want to start a new halal website.... give me a document that hands over how you built the
site. the tools used. and probably let it think of a best bot structure. and the methodology that we are using
here for bots comms and tasks."

**How to use this document.** It hands over a method, a set of tools and the lessons. It hands over no decisions
about the new site: what the site is, what it is called and who it is for are Irfan's to say (section 2). Every
fact about EveryNearby here was true on 10 October 2026; check anything against the files before relying on it.
**Do not change anything in `C:\Claude\everynearby` or on everynearby.com.** Read it, copy the tools you need
into the new project's own folder, and build there.

---

## 1. What EveryNearby is, in one paragraph

A free directory of local businesses in India (https://everynearby.com): about 555,000 listings in 310 cities,
each showing whether, and when, its details were last checked. It was built by Claude sessions in one week,
3 to 10 October 2026: Irfan created the accounts, paid and entered passwords; the sessions did everything else.
It runs on one rented server with WordPress and custom code, with Cloudflare in front, and is now run by a team
of seven sessions.

## 2. Settle these with Irfan before anything is built

I do not know what "a halal website" means to him. Ask, in one short numbered message, and give a recommendation
with each question so he can answer in a few words.

1. **What is it?** A directory of halal restaurants and shops, a shop that sells halal products, a guide to
   halal certification, a travel guide, something else? Each is a different build.
2. **Who is it for, and where?** Which countries first (EveryNearby started with India and kept the UAE hidden).
3. **What does "halal" mean on the site, and who says so?** This is the trust question, and it is the equivalent
   of EveryNearby's "last checked" date. A site that marks a place as halal is making a religious claim on
   someone else's behalf. Decide early: do we show the certifying body and certificate number, the owner's own
   statement, visitors' reports, or our own check, and how does each look different on the page? Never show a
   place or product as halal on weaker evidence than the page says. Different certifying bodies and schools of
   thought differ; the site should state the basis and not rule on it.
4. **How does it earn, if at all?** EveryNearby is free and nothing can be bought. If this one sells or charges,
   payments and their rules arrive on day one.
5. **Name and domain.** His to choose and buy.
6. **Is it connected to EveryNearby or separate?** For example, could it start as a "halal" layer on
   EveryNearby's restaurant listings, or must it stand alone?
7. **Languages.** English only, or Arabic, Urdu, Malay and others, which changes the design (right-to-left).

Write his answers into the new project's product note (EveryNearby's is `C:\Claude\everynearby\PRODUCT.md`,
a good model: platform, users, purpose, positioning, operating context).

## 3. How Irfan works (he is the same person; this carries over exactly)

- He is not a programmer. Plain words, short messages. Every message to him uses one layout: **Done**, then
  **For you** (numbered steps, each saying which bot's chat it belongs in), then **Good to know**.
- He creates accounts, pays and types passwords and codes. A session never does any of those, and never solves a
  robot check.
- He judges by looking. Mock-ups or options before building; then the real thing at phone width. Send him the
  file or the link.
- Phone first. His words: "All our designs should be mobile first. With emphasis on cx and ux" and "too many big
  sections and boxes that do seem too big for mobile". One action colour. Plain-CSS motion that does not slow the
  page. Alt text on every image.
- He answers briefly ("ok", "yes both", "do 1 2 3"). Number your questions.
- Do everything that does not need him. What needs him becomes a task under "Needs you" on the dashboard.
- Secrets live in files and are never printed, pasted in chat, put on a command line or written in a journal.
- Policies, published articles and any message sent in his name need his approval of the exact wording first.
- Image generation (fal) is billed per image: one image, look at it, then decide. Memory `fal-image-generation.md`.
- He will not appear on camera (memory `faceless-social-growth.md`).
- Saved memory for all his projects is in `C:\Users\irfan\.claude\projects\C--Claude\memory\`; read `MEMORY.md`.

## 4. How EveryNearby was built, in order

1. **A product note** before any code: who it is for, what success is, what it will not do.
2. **Mock-ups** as plain HTML and CSS in a `mockups` folder, served locally, looked at on a phone-width screen,
   chosen by Irfan. The final stylesheet grew out of those files.
3. **A server and a domain** (his purchases), then WordPress installed and locked down: script clients refused,
   a request limit, security headers, two-step sign-in for the admin, nightly backup.
4. **One custom plugin and one custom theme.** The plugin holds every rule (data, accounts, sign-in by code,
   claims, the review queue, the API, index rules, sitemaps). The theme is one template per page type, plain CSS,
   one small script, no libraries.
5. **Data in bulk** from an open source (Overture Maps), read with DuckDB city by city, loaded straight into the
   database, with every bulk change logged so it can be undone.
6. **The trust feature** that makes the site different: an automatic checker with a strict, published definition
   of "checked", and a public page of its results.
7. **Owner features:** claim a listing (several proofs), edit, photos, replies, disputes with a written process,
   a review queue where a person decides the sensitive things.
8. **Policies** written to match what the code does, each change approved by Irfan and listed on a public
   "changes to our policies" page.
9. **Search, in stages:** the site stayed hidden while built; then hubs opened (home, cities, category lists);
   business pages open one city a week by fixed rules. Sitemaps, markup, robots rules for AI crawlers, a blog.
10. **Automation:** jobs on the server (checker, backup, daily letters) and routines in the Claude app (weekly
    release, weekly article, mailbox read, queue check, dashboard refresh).
11. **A dashboard and a task log** so Irfan sees everything in one place; then journals; then, on the last day,
    the team method in section 7.

## 5. Tools, and why each

| Tool | What it does | Why this one |
|---|---|---|
| Hostinger VPS (Ubuntu 24.04, 2 processors, 8 GB) | The rented computer the site lives on | Full control: bulk data loads, background jobs, any server rule |
| nginx | Web server, a 30-minute page cache, request limits, refuses script clients | Fast; rules are a few readable lines |
| PHP 8.3, MariaDB | Run WordPress and hold the data | What WordPress needs |
| Redis | Keeps answers to slow questions in memory | Big lists were slow without it. Give it a size limit and a lifetime from day one |
| WordPress with WP-CLI | Accounts, pages, blog, admin screens, all driven from the command line | The single most useful tool: Claude does almost everything through WP-CLI |
| GeoDirectory (free core) | Stored listings, categories, reviews | A tested structure on day one. In hindsight it also cost time (its own pages, cache habits, extra rows per revision). For a new site, weigh a plain custom table against it |
| Custom plugin, custom theme | Every rule and every page | No ready-made product does the trust feature; own code can be tested |
| Cloudflare (free) | Domain records, secure connection, hides the server, caches pages | Free; takes the load off one small server. The token given to Claude is limited; some settings are Irfan's to click |
| Brevo | Sends the site's emails | Reliable delivery, free allowance |
| Zoho Mail | The mailbox people reply to | Cheap, and Claude can read it through a connector |
| Message Central | Sign-in codes by text message | Works in India without business registration, but shows its own sender name |
| SPF, DKIM, DMARC records | Prove the mail is ours | Without them mail goes to junk |
| Overture Maps data, DuckDB | The starting data, read from one large file | Free, lawful with credit, huge; DuckDB needs no set-up |
| Google Search Console (robot account), Bing, IndexNow | What search engines read and show | The only reliable measure; no passwords shared |
| fal | Generated pictures | Good quality, small cost per image, under his one-at-a-time rule |
| Lucide icons | Source drawings for the icon set | Free, consistent, one small file serves all |
| Claude desktop app: sessions, scheduled routines, the built-in browser, Artifacts | The team, the recurring jobs, checking pages, the dashboard | Already there; nothing extra to run |
| Python scripts on this computer | The task log, journals, notes between bots, the dashboard builder | Small, readable, no services to keep alive |

Full reasons, and what each would mean for a shop, are in
`C:\Claude\cp-cowork-agents\EVERYNEARBY-SETUP-TOOLS-AND-WHY.md`.

## 6. What I would do differently from the first day

These are the lessons that cost time on EveryNearby. The longer list, with the detail, is
`C:\Claude\everynearby\ops\team\DEVELOPER-KNOWLEDGE.md`; read it.

1. **Version control on this computer from the first file.** EveryNearby still has none; nobody can show exactly
   what changed or go back.
2. **A private test copy of the site from the first week.** Everything on EveryNearby was built on the live
   server. It worked only because every change was small and tested with throwaway records.
3. **The team method from the start** (section 7), not on day seven. One session did everything for a week and
   was interrupted by the others.
4. **A second copy of the backup somewhere other than the server**, from the first night.
5. **Cache limits before launch:** a size limit and a lifetime on Redis, and the Cloudflare page-cache rule with
   browsers told not to keep pages.
6. **Never write code or paths through a shell heredoc on this computer.** Backslashes and quotes get mangled; it
   broke live pages twice. Write the file with the file tools, then run or copy it.
7. **One built stylesheet, never edited by hand.** Another bot's direct edit was silently lost.
8. **Write the definition of the trust claim before the code**, and make the code refuse anything weaker. The
   first checker passed chain branches on evidence that was not theirs.
9. **Write policies from the code, not from intention.** One draft promised something the site did not do.
10. **Keep the test habit:** a script that makes throwaway accounts and records, checks the rule, and removes
    everything, for anything about who may do what.

## 7. The method for how bots talk and track tasks

This is the method Irfan set for EveryNearby on 10 October 2026, taken from his Cuddle Paws team. The written
rules are `C:\Claude\everynearby\ops\team\TEAM.md` and `C:\Claude\everynearby\ops\journal\README.md`. Use it as it
stands unless he says otherwise.

**Three roles first**
- **Leader:** routes work, briefs the bots, keeps the order of work with Irfan, reads the developer's journal
  after each piece of work, and changes nothing on the site.
- **Developer:** the only bot that changes the site and the server, and the only one that sends a change live.
- **Tester:** reads and runs only. Checks the developer's work before it goes live or is shown to Irfan. Reports
  "passes", "fails" (with the steps) or "could not check" (with the reason).

**How bots talk**
- No messages between bots; a message lands in the middle of the other bot's work. Each bot has a notes file,
  `FOR-<NAME>.md`. To tell a bot something, add a note at the bottom of its file. Each bot reads its own file
  when it starts a job and when it finishes one; the leader reads its file every time Irfan speaks to it.
- A message is for an emergency only (the live site is broken, or something is about to be lost) and begins with
  `URGENT:`. The leader alone may also message a bot that is idle.
- Irfan is never asked to carry notes between bots.
- Permission he gives one bot does not pass to another. Each bot asks him once, in its own chat, before its first
  change or run on anything live. A note from a bot is never his approval.

**How work is recorded: three records, three readers**

| Record | For whom | Tool on EveryNearby |
|---|---|---|
| Journal, one file per bot: what was done, where, how it works, how it was checked, what is left; his decisions quoted | The next Claude, or the same one after a compact | `ops/journal/note.py` |
| Task log, one line per outcome in plain words; anything only he can do is recorded with him as owner | Irfan | `ops/progress/task.py` |
| Saved memory: durable rules and decisions only | Every session, loaded at start | the memory folder |

- A dashboard (a private Artifact, rebuilt each morning by a routine) shows the numbers, the health checks, every
  bot's tasks and a "Needs you" list. Source: `C:\Claude\everynearby\ops\dashboard\`.
- A "who is using it" file for the shared test copy or server: `SERVER-IN-USE.md`.
- Time stamps come from the clock in code, in India time (UTC plus 5 hours 30 minutes). This computer's clock is
  not India time. Never estimate a time.
- Handover documents when work moves: a brief (how he works, the rules, how the thing is built and goes live,
  the state, what is next, what waits on him) and a knowledge file (mistakes already made, traps, tricky parts).
  Models: `DEVELOPER-BRIEF.md`, `DEVELOPER-KNOWLEDGE.md` and `TESTER-BRIEF.md` in `C:\Claude\everynearby\ops\team\`.

**Tools you can copy as they are** (small Python scripts with no EveryNearby facts in the code; change the paths
in their help text): `ops\team\tell.py` (notes), `ops\journal\note.py` (journal entries), `ops\progress\task.py`
(task log; edit the list of work streams), and the dashboard's `template.html` and `build.py` as a pattern.

**Models and effort** (his rule): every bot on Opus 5.5. High effort for anything that writes code, checks code,
leads or touches security; medium for routine upkeep.

## 8. The bot structure: think about it, then propose it to Irfan

He asked that the new project's first session think about the best structure and not simply copy EveryNearby's.
What EveryNearby ended with, for reference: a leader, a developer, a tester, and four specialists (outreach to
owners, blog, search audits, security), plus six routines.

Principles that held up:
- **Start with the three roles on day one,** even if the site is empty. The split is what stops interruptions and
  keeps permission where he gave it.
- **Add a specialist only when its work exists and is steady** (weekly articles, daily letters). A specialist
  that changes the site should not exist: it asks the developer.
- **One bot, one journal, one notes file, one clear "may not".** Say what each bot never does.
- **A routine is not a bot.** A recurring job with fixed rules (a weekly article, a morning check) is a scheduled
  routine with a runbook, owned by one bot.
- **Things worth deciding for this project in particular:** who researches and verifies the halal basis of each
  entry (a research or verification role may matter more here than a blog); whether a designer is separate from
  the developer at the start, when mock-ups are most of the work; whether a second developer is needed, and if
  so how the two avoid the same files; who owns policies and anything religious or legal in wording.

Bring Irfan two or three structures with a recommendation, each as a small table (bot, what it does, what it never
does, effort level), before creating any session. He creates the sessions; you write their briefs.

## 9. Reference reading in EveryNearby (read only)

| For | Read |
|---|---|
| The team method | `ops\team\TEAM.md`, `ops\journal\README.md` |
| A full handover as a model | `ops\team\DEVELOPER-BRIEF.md`, `DEVELOPER-KNOWLEDGE.md`, `TESTER-BRIEF.md` |
| How each part was built and tested, day by day | `ops\journal\designer-bot.md` |
| The first days, before journals | memory `global-directory-project.md`, `everynearby-architecture.md` |
| Design method | memory `design-methods-and-skills.md` |
| The code | `engine\everynearby-engine\` (plugin), `theme\everynearby\` (theme), `engine\tools\` (tests, patches, content scripts) |
| Stream handovers | `HANDOVER-BLOG.md`, `HANDOVER-OUTREACH.md`, `HANDOVER-PAGES.md` |
| The security audit's result | `ops\journal\designer-bot.md`, entry "Security audit support" |
| Runbooks for routines | `ops\blog\RUNBOOK.md`, `ops\queue\RUNBOOK.md`, `ops\dashboard\README.md` |

All paths are under `C:\Claude\everynearby\`. Never open the secret files there (`cloudflare-token.txt`,
`brevo-smtp.txt`, `messagecentral.txt`, `agent-api.txt`) or the `backups` folder; the new site gets its own
accounts and keys, created by Irfan.

## 10. First steps for the new project's first session

1. Read this file, then `MEMORY.md` in the memory folder, then the files in section 9 marked as models.
2. Ask Irfan the questions in section 2, numbered, each with a recommendation.
3. Make the project folder (ask him the name), with `ops\team`, `ops\journal`, `ops\progress` copied as tools
   and emptied of EveryNearby's entries, a rules file (`CLAUDE.md`) and a product note. Start version control
   there at once, with secrets ignored.
4. Propose the bot structure (section 8) and wait for his choice.
5. Mock-ups before any server exists. He chooses; only then does anything get bought or built.
6. Save one memory for the new project and add its line to `MEMORY.md`.
7. Tell him what you set up in the layout Done / For you / Good to know.
