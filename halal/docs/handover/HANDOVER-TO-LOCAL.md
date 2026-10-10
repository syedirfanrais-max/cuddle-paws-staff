# Handover: the halal food website, from the first session to the next

Written 10 October 2026, 22:46 India time, by the first session of Irfan's new halal
website (a Claude Code cloud session, acting as leader). It is for the new session
Irfan is creating on his own computer. That session knows nothing yet; this is its
starting point. Read all of it before doing anything.

Irfan's words that led to this document: "move from cloud to local competeley", then
"just give me a detailed handover document i will create a new session".

---

## 0. In one paragraph

Irfan wants a free, global halal food website with two connected parts: a weekly
halal **meal planner** for home cooking, and a halal **restaurant finder** for eating
out and travel. It will be built on WordPress with our own theme and plugin, the same
way his other site, EveryNearby (everynearby.com), was built. So far: a competitor
study is done (section 4), the project's rules, product note and team tools are set
up (section 6), and a first round of questions to Irfan is waiting for his answers
(section 7). **Nothing has been built, bought or published.** No server, no domain,
no accounts exist for this site.

---

## 1. First steps for you (in this order)

1. **Read this whole document.**
2. **Read Irfan's saved memory:** `C:\Users\irfan\.claude\projects\C--Claude\memory\MEMORY.md`
   and the memory files it points to that matter here (the first session could not,
   because it ran in the cloud).
3. **Read the EveryNearby handover:** `C:\Claude\everynearby\HANDOVER-NEW-SITE.md`.
   It is the method this project follows. **Never change anything in
   `C:\Claude\everynearby` or on everynearby.com. Never open its secret files
   (`cloudflare-token.txt`, `brevo-smtp.txt`, `messagecentral.txt`, `agent-api.txt`)
   or its `backups` folder.**
4. **Get the project files onto this computer.** Two ways; ask Irfan which, or use (a):
   - **(a) From GitHub (has everything the first session wrote):** clone
     `https://github.com/syedirfanrais-max/cuddle-paws-staff`, check out branch
     `ccr-ac5d3aa9-2ek23x`, copy **only** its `halal` folder to `C:\Claude\halal`.
     Copy nothing else from that repository (the rest is Cuddle Paws, unrelated).
   - **(b) Without GitHub:** create `C:\Claude\halal` yourself from this document:
     sections 3, 5, 6 and 7 hold everything needed for `PRODUCT.md` and `CLAUDE.md`,
     and the team tools can be copied from EveryNearby as its handover says
     (`ops\team\tell.py`, `ops\journal\note.py`, `ops\progress\task.py`, emptied of
     EveryNearby's entries).
5. **Start version control in `C:\Claude\halal` at once** (`git init`, first commit),
   with secrets, backups and bulk data ignored (`.gitignore` in section 6).
6. **Check the tools work** (section 6 lists the commands).
7. **Compare the tools with EveryNearby's originals.** The first session rewrote them
   from the handover's description because it could not see `C:\`. Keep whichever is
   better and note the choice in the leader's journal.
8. **Save one memory for this project** and add its line to `MEMORY.md`.
9. **Write a journal entry** for the move, and close task 11 in the task log.
10. **Then talk to Irfan**: tell him what you set up and ask the open questions in
    section 7, in his layout (section 2).

---

## 2. How Irfan works (this carries over exactly from EveryNearby)

- He is not a programmer. Plain words, short messages.
- **Every message to him uses one layout: Done, then For you (numbered steps, each
  saying which bot's chat it belongs in), then Good to know.**
- Number every question and give a recommendation with each, so he can answer in a
  few words ("ok", "yes both", "do 1 2 3").
- **Ask questions in plain numbered text, not in pop-up question forms.** When the
  first session used the pop-up multiple-choice tool, he dismissed it.
- He creates accounts, pays, and types passwords and codes. A session never does
  any of those, and never solves a robot check.
- He judges by looking: mock-ups or options before building, then the real thing at
  phone width. Send him the file or the link.
- Phone first. His words: "All our designs should be mobile first. With emphasis on
  cx and ux" and "too many big sections and boxes that do seem too big for mobile".
  One action colour. Plain-CSS motion. Alt text on every image.
- Do everything that does not need him. What needs him becomes a task with him as
  owner, so it shows under "Needs you".
- Secrets live in files and are never printed, pasted in chat, put on a command line
  or written in a journal.
- Policies, published articles and any message sent in his name need his approval of
  the exact wording first.
- Image generation (fal) is billed per image: one image, look at it, then decide.
- He will not appear on camera.
- He is based in Dubai. EveryNearby's time stamps use India time (UTC+5:30); the
  first session used India time too (open question 8 asks him to confirm).
- Models and effort (his rule): every bot on Opus 5.5; high effort for anything that
  writes code, checks code, leads or touches security; medium for routine upkeep.

---

## 3. The project in Irfan's own words (his brief of 9 October 2026, complete)

> You are building a new website from scratch: a global, free halal food platform
> with two connected parts, (1) a weekly halal meal planner for home cooking and (2) a
> halal restaurant finder for eating out and travel. The owner (me) is based in Dubai.
>
> **Product summary**
> - Proposition: "Plan halal meals at home and find halal food anywhere, free."
> - Audience: Muslim families and individuals worldwide; first focus on the UAE,
>   India, the UK, the US and Canada, plus Muslim travellers in non-Muslim countries.
> - Model: free first, paid later (ads, a premium tier of about US$3-5 a month,
>   grocery affiliate links, featured restaurant placement once the business is
>   licensed).
> - Operations: fully automated, no staff. The only human tasks are approving
>   disputed restaurant listings and reviewing content I flag.
> - Platform: WordPress backend (as on my other site), with our own custom theme and
>   plugin code written by you. Avoid third-party plugins except where truly needed
>   (for example a security plugin or SMTP); list any you want to use and why.
>
> **PHASE 1: competitor study** (done; see section 4)
>
> **PHASE 2: build (only after I approve Phase 1)**
>
> *Meal planner*
> - Inputs: household size (adults, children), weekly budget level, cuisines (Indian,
>   Pakistani, Arab, Levantine, Turkish, Malay/Indonesian, East African, Western,
>   mixed), diet goals (none, diabetic-friendly, high-protein, weight loss,
>   kids-friendly, vegetarian days), cooking time per meal, dislikes and allergies.
> - Output: a 7-day plan (breakfast, lunch, dinner, optional snacks) from our own
>   recipe database, with a combined shopping list grouped by aisle, shareable on
>   WhatsApp and printable.
> - Generation: rule-based selection from our recipe database (variety, budget, time,
>   diet constraints, leftovers reuse). No paid AI API at runtime for launch. Results
>   must appear instantly.
> - Ramadan mode: suhoor and iftar plans, with fasting times for the user's city from
>   a reliable calculation method (let me choose the calculation method; show it on
>   the page).
> - Ingredient checker: a page and a search box that answers "is this halal?" for
>   common ingredients and additive codes (gelatine, E120, E471, alcohol in vanilla
>   extract, rennet, L-cysteine and others), each marked halal, doubtful or not halal,
>   with the reason and a safer swap. Be conservative and explain where scholars
>   differ; do not issue religious rulings.
> - Recipe database: start with 300 original recipes that you write, each with
>   ingredients in metric and US units, steps, time, servings, cost level, cuisine,
>   diet tags, and a substitutions note. Do not copy recipes from other sites; facts
>   like ingredient lists for common dishes are fine, but wording and method must be
>   ours. I will review a sample of 20 before you write the rest.
>
> *Restaurant finder*
> - Pages: country, city and area hubs; a city list page with filters (halal status,
>   cuisine, price, open now, alcohol-free premises, prayer space nearby); a
>   restaurant profile; a map view loaded on tap.
> - Halal status labels, shown with the source and the date last checked: "Halal
>   certified (certificate on file)", "Halal meat served (owner or user reported)",
>   "Muslim-owned", "Not verified". Never show "certified" without a certificate.
> - Report button on every listing (closed, not halal, wrong details) and a claim flow
>   for owners (code sent to the listed phone or an email at the restaurant's own
>   website domain), with changes to name, phone or address held for review.
> - Seed listings only from legally usable data sources agreed in Phase 1. Publish a
>   city only when it has enough real listings to be useful (propose the threshold).
> - Travel guides: "Halal food in [city]" pages built from our own listing data with
>   an original introduction you write per city.
>
> *Accounts and premium (build the structure, keep payments switched off)*
> - Free account to save plans, recipes and favourite restaurants.
> - Premium features built behind a flag: unlimited saved plans, family profiles,
>   calorie and macro tracking, printable plan packs, no ads. Payment provider to be
>   decided later; do not integrate one yet.
>
> *Design*
> - Mobile-first, tested at 360px wide. Clean, warm, trustworthy. One brand colour,
>   generous white space, no stock photos of food we did not cook; use simple
>   illustrations or icons until we have real photos.
> - English first; build so Arabic (right-to-left) and Urdu can be added later
>   without redesign.
> - Accessibility: labelled fields, keyboard use, 4.5:1 contrast, 44px touch targets.
> - Speed: main content visible within 2.5 seconds on a mid-range phone on 4G.
>
> *SEO*
> - Clean URLs, unique titles and descriptions, one H1 per page, breadcrumbs,
>   structured data (Recipe for recipes, Restaurant for listings, BreadcrumbList,
>   ItemList for city lists).
> - Only publish pages with real, useful content; no mass-generated thin pages.
> - Sitemaps per section, submitted later by me.
>
> *Legal pages*
> - Terms, privacy policy, cookie notice (prefer cookie-free analytics so no banner
>   is needed), listing and halal-labelling policy, report and removal policy,
>   disclaimer that users should confirm halal status with the restaurant, data
>   sources and attribution page. Draft them for my lawyer to review.
>
> *Security*
> - Few plugins, automatic updates, firewall, two-step sign-in for admins, rate
>   limits and Cloudflare Turnstile on all forms, image-only uploads re-encoded on
>   upload, daily off-site backups, staging site for all changes, no secrets in
>   front-end code.
>
> **How to work**
> 1. Phase 1 report, then wait for approval.
> 2. Propose the architecture (WordPress structure, custom post types or tables,
>    plugin code layout, hosting needs) and a build plan with milestones. Wait for
>    approval.
> 3. Build in milestones on a staging site: recipe database and planner first, then
>    ingredient checker, then restaurant finder, then accounts.
> 4. After each milestone: tell me what was built, how to test it, and anything that
>    needs my decision.
> 5. Never publish live without my explicit go-ahead.

**Status against this brief:** step 1 (Phase 1 report) is done and reported. Irfan
has **not yet approved** the Phase 1 feature list. He then asked to set up the
operating foundation first (EveryNearby's method), which is done. Step 2
(architecture and build plan) has not started.

---

## 4. Phase 1 competitor study: what was found

Full report: `halal\docs\research\phase1-competitor-study.md` (in the GitHub copy).
The essentials:

**Research limits (be honest about these if asked).** The cloud environment blocked
direct page reads of competitor sites, app stores, Reddit and OpenStreetMap hosts.
Findings came from search-result summaries, press, public app trackers, and Overture
Maps' own documents and data files. Not done: checking competitors' structured data,
sampling their listings for dates and closures, reading full app-store and Reddit
reviews. A session on Irfan's computer may be able to do these.

**Competitors in one line each**
- **Zabihah**: best-known global finder (about 50–60k places), free, evidence-based
  "HalalRank" score; main complaint: stale and closed listings.
- **HalalTrip / CrescentRating**: travel-first, pages years old.
- **Halal Navi**: Japan only, the most detailed labels (certifier named, menu vs
  whole kitchen, alcohol-free, pork-free).
- **Muslim Pro**: finder buried in a prayer app, data is a Foursquare keyword match;
  2020 location-data scandal still hurts trust.
- **Have Halal Will Travel**: editorial guides, earns from tourism-board advertising.
- **Halal Gems** (UK): trusted but old reviews.
- **Certifier lists** (HMC UK, HMS USA, HMA Canada): most trustworthy, narrow, no open
  licence: link to them, never copy.
- **Yelp, Tripadvisor, Uber Eats, DoorDash**: dominate US "halal near me" searches.
- **HappyCow** (vegan) and **Find Me Gluten Free**: the structure models (city hubs,
  "best in [city]" pages, "reported" wording, closure dates; HappyCow charges
  restaurants $100/month for featured placement; FMGF wrongly paywalls safety filters).
- **Meal planners**: Mealime ($2.99/month, **shuts down 21 October 2026, no export**),
  Eat This Much ($9/month), PlateJoy (**closed July 2025**), Plan to Eat, Paprika,
  Samsung Food. **None is halal-aware.** The small halal planners are new, AI-based
  and barely used. Halal ingredient checkers are mostly paywalled AI scanners that
  do not say which scholarly view they follow.

**Search demand (monthly searches, 12-month average)**
- "halal food near me": US 823,000; UK 301,000; Canada 165,000; India 8,100; UAE 590.
- "halal restaurants near me": US 450,000; UK 165,000; Canada 135,000; India 27,100;
  UAE 1,000.
- UK city terms are strong: "halal restaurants birmingham" 14,800, "halal food
  manchester" 9,900, "halal restaurants london" 8,100.
- Ramadan fasting times are huge: "iftar time today" (India) 165,000; "iftar time
  dubai" 49,500; "prayer times dubai" 1.22 million.
- "halal meal plan" is tiny (US 140), so the planner must be found through recipe,
  Ramadan and ingredient pages.
- Ingredient questions are steady: "is vanilla extract halal" US 1,300; "is E120
  halal" UK 1,300; "is gelatin halal" US 880.
- In the UAE and India almost nobody searches "halal": in the UAE it is assumed; in
  India people search by dish ("biryani near me" 550,000).
- Keyword data is in Irfan's OpenSEO account, project "Halal food platform (research)".

**The 10 gaps, and how the site fills each**
1. Halal status nobody can check → four labels with source and date; separate facts
   for alcohol served, pork on premises, whole menu vs some dishes, certifier and its
   standard (stunned or not); a personal filter.
2. Stale and closed listings → "needs re-check" after a set time, one-tap "closed"
   report, checks against open data, owner reconfirmation emails.
3. No halal-aware planner for Pakistani, Arab, Turkish, Malay and East African home
   cooking on a budget → the core offer.
4. Gimmicky Ramadan apps → suhoor and iftar plans with city fasting times and a
   shopping list.
5. Paywalled, unexplained ingredient checkers → free, conservative, explains where
   scholars differ, offers a swap, built into recipes and the shopping list.
6. Home cooking and eating out are separate products → one site, one account.
7. Lists can't reach the household shopper → WhatsApp-formatted list, and print.
8. Planners close and lock data in → free, export everything.
9. Distrust of ads and tracking → cookie-free analytics, never sell location.
10. Thin and stale competitor pages → clean URLs, structured data, city thresholds,
    dated guides.

**Restaurant data sources that can be used legally**
- **Overture Maps Places**: the base list of real businesses (permissive licences,
  contains no OpenStreetMap data). Weak halal signal: places with "halal" in the
  category or name in the September 2026 release: US about 4,000, UK about 1,000,
  Canada about 580, India about 290, **UAE 20**. Overture keeps public files only
  60 days, so mirror its deletions. EveryNearby already loads Overture with DuckDB.
- **UK Food Standards Agency hygiene data** (Open Government Licence): which UK
  businesses are trading now.
- **City open data** (NYC, Toronto and others), city by city.
- **Owners and users**: the main source of halal status.
- **Certificates**: checked one at a time on the certifier's own website, linked,
  never copied; no certifier logos without permission.
- **Never**: Google, Yelp, Tripadvisor or Zomato content, or other halal directories.
- **OpenStreetMap** (`diet:halal` tags): richest free halal tagging, but its ODbL
  licence means changed or combined OSM data used publicly must be shared under ODbL,
  and keeping it in a separate table does not avoid that if OSM and non-OSM
  restaurants mix in the same area. Options: **A** none; **B** everywhere, publish
  listing facts as an open download; **C** only in travel-guide countries, in separate
  tables (recommended, to confirm with his lawyer). **Not decided.**

**Questions for his lawyer** (later): how far ODbL share-alike reaches; certifier
database rights and logos; liability for a wrong halal claim; India's halal
certification rules (Uttar Pradesh banned halal-certified products in 2023);
Foursquare portal terms; UAE government data licences.

---

## 5. Recommendations already given to Irfan (not yet approved)

**Launch, in priority order**
1. Recipe database: 300 original recipes with Recipe structured data; Irfan reviews 20 first.
2. Weekly planner: inputs from the brief, instant rule-based generation, swap or lock
   a meal, leftovers reuse, aisle-grouped shopping list shared by WhatsApp and printed;
   works without an account.
3. Ramadan mode: suhoor and iftar plans plus city fasting times; Irfan picks the
   calculation method, and the page names it.
4. Ingredient checker: about 150 entries at launch (common ingredients and E-numbers),
   each halal / doubtful / not halal with reason, where scholars differ, and a swap;
   one page per entry; flags inside recipes.
5. Legal pages, cookie-free analytics, security baseline.
6. Restaurant finder, opened city by city when a city meets the threshold.
7. "Halal food in [city]" travel guides, only for cities that meet the threshold.
8. Free accounts (save plans, recipes, favourites).

**Rules recommended**: no star reviews at launch (no staff to moderate; use dated
"still open / still halal" confirmations instead); never charge for halal status or
safety filters; featured placement never changes how halal status is shown.

**Later**: premium (built, switched off), ads, grocery affiliates, featured listings,
Arabic and Urdu, barcode scanner, "is [chain] halal" pages (high UK demand but status
varies by branch), city × cuisine pages, mosque directory.

**Countries**: planner open to all; restaurant pages first in UK, Canadian and US
cities; UAE and India restaurant pages hidden at first. UAE angle: lead with planner,
Ramadan and travel guides; a UAE finder, if built, is framed around "alcohol-free
premises" and "no pork on site". India: neutral wording, evidence shown.

**City threshold proposed**: a city page opens at 20 active listings with a status
better than "Not verified", each checked within 12 months, covering 3 or more
cuisines; area hubs at 10; filter or cuisine sub-pages indexed only at 5 or more.
Overture records nobody has confirmed stay private (used as a pick-list of real
businesses), except those that call themselves halal, shown as "Not verified".

**Timing**: Ramadan 2027 is expected around 8 February 2027 (depends on moon
sighting). Aim: planner, Ramadan mode and checker on a test copy by mid-January 2027.

---

## 6. The project foundation the first session set up

All in the `halal` folder (GitHub branch `ccr-ac5d3aa9-2ek23x`, two commits:
`b5e0c46` and `762e16a`; this document is in a third).

| File | What it is |
|---|---|
| `README.md` | Where to start |
| `CLAUDE.md` | Rules for every session: how Irfan works, hard rules, team method, where things are |
| `PRODUCT.md` | Product note: decided vs open, with recommendations |
| `.gitignore` | Keeps out `secrets/`, `*.secret`, `*.key`, `*.pem`, `.env*`, `*-token.txt`, `*-smtp.txt`, `*-api.txt`, `wp-config.php`, `backups/`, `data/raw/`, `*.sql`, `*.sql.gz`, `*.parquet`, `*.osm.pbf`, `__pycache__/` |
| `ops/team/TEAM.md` | The team method (roles, notes not messages, three records) |
| `ops/team/tell.py` | Leave a note in another bot's `FOR-<NAME>.md` |
| `ops/team/FOR-LEADER.md` | The leader's notes file (empty) |
| `ops/journal/README.md` | Journal headings and rules |
| `ops/journal/note.py` | Add a journal entry |
| `ops/journal/leader.md` | The leader's journal (two entries) |
| `ops/progress/task.py` | Task log; streams: foundation, product, design, recipes, planner, ramadan, checker, finder, accounts, policies, server, search; owners: irfan, leader, developer, tester |
| `ops/progress/tasks.jsonl` | The task log itself |
| `docs/handover/HANDOVER-NEW-SITE.md` | Copy of EveryNearby's handover |
| `docs/handover/HANDOVER-TO-LOCAL.md` | This document |
| `docs/research/phase1-competitor-study.md` | The competitor study |

**Hard rules written into `CLAUDE.md`**: never change EveryNearby; secrets only in
ignored files, never shown; never show anything as halal on weaker evidence than the
page says, state the basis, never rule, say where scholars differ, definitions before
code; nothing live without Irfan's go-ahead; never copy other sites' data, recipes or
photos; write files with the file tools, never through a shell heredoc; time stamps
from code; policies written from what the code does; test "who may do what" with
throwaway records.

**Check the tools** (run in `C:\Claude\halal`; use `python` or `py` on Windows):
- `python ops\progress\task.py list` → tasks 2 to 11 open
- `python ops\progress\task.py needs-you` → the tasks owned by Irfan
- `python ops\journal\note.py leader --last 2` → the two leader entries
- `python ops\team\tell.py leader --read` → the empty notes file

The scripts use only Python's standard library and write UTF-8. Time stamps are India
time, set by `SITE_TZ` at the top of each script.

**Task log as handed over**
| # | Owner | Task | State |
|---|---|---|---|
| 1 | leader | Set up the project folder and tools | done |
| 2 | irfan | Answer the first round of questions | open |
| 3 | irfan | Choose the site name and buy the domain | open |
| 4 | leader | Propose two or three bot structures | open |
| 5 | irfan | Choose the bot structure, then create the sessions | open |
| 6 | leader | Write the exact definition of each halal label and ingredient status | open |
| 7 | irfan | Approve the definitions; name a scholar or imam to review if wanted | open |
| 8 | irfan | Decide how to use OpenStreetMap (A, B or C), with the lawyer | open |
| 9 | leader | Phone-width mock-ups: home, weekly plan, shopping list, ingredient checker | open |
| 10 | irfan | Say when the project moves to its own GitHub repository | open (now: probably answered by the move; confirm) |
| 11 | irfan | Start a Claude session on his computer so the project moves to `C:\Claude\halal` | open (close it once the move is done) |

---

## 7. Open questions waiting for Irfan

Ask these first, numbered, in plain text, each with the recommendation, so he can
answer in a few words.

1. **Launch order**: planner, recipes, ingredient checker and Ramadan mode first,
   ready before Ramadan (about 8 Feb 2027); restaurant finder after. *Recommend yes.*
2. **Restaurant pages**: UK, Canadian and US cities first; UAE and India hidden at
   first. *Recommend yes.*
3. **Name**: does he have one? *Recommend: suggest ten and check which domains are
   free; he chooses and buys.*
4. **EveryNearby**: fully separate site, server, accounts and keys; reuse the method
   and tools only. *Recommend yes.*
5. **Religious wording**: he approves every halal label and ingredient answer; does he
   also want a scholar or imam to review them, and who?
6. **Ingredient checker**: where scholars differ (gelatine, E471, vanilla extract),
   main answer cautious, other views noted. *Recommend yes; a school-of-thought setting
   (Hanafi, Shafi'i and others) can come later.*
7. **Recipe testing**: he or his family cook the first 20 sample recipes before the
   rest are written; "tested in our kitchen" appears only when someone actually
   cooked it. *Recommend yes.*
8. **Time stamps**: India time like EveryNearby, or Dubai time? *Recommend India.*
9. **Backup copy**: keep a private GitHub copy of `C:\Claude\halal` as an off-computer
   backup? *Recommend yes.* (He asked "why do you want to use git host the site
   locally". The answer given: git is only the change history inside the folder, not
   hosting; GitHub was only the delivery route plus an optional backup; the site
   itself will be on a rented server, bought after mock-ups are approved.)

Also still open from Phase 1 (bring back at the right step, do not stack them all now):
- Approval of the launch feature list and "later" list (section 5).
- OpenStreetMap option A, B or C (section 4).
- UAE and India positioning (section 5).
- The city threshold (section 5).

---

## 8. What comes after his answers

1. **Bot structure** (EveryNearby handover section 8): bring two or three structures,
   each as a small table (bot, what it does, what it never does, effort level), with
   a recommendation. Start with leader, developer and tester. Things to decide for
   this project in particular: a halal-verification role (checks certificates,
   researches ingredient entries) probably matters more than a blog writer; whether
   a designer is separate from the developer while mock-ups are most of the work; who
   owns policies and anything religious or legal in wording. He creates the sessions;
   you write their briefs.
2. **Halal definitions** (task 6): write the exact definition of each label and each
   ingredient status, what evidence each needs, who checks, and how it expires; then
   code refuses anything weaker.
3. **Mock-ups** at phone width (task 9), plain HTML and CSS in `mockups\`, before any
   server exists. He chooses.
4. **Architecture and build plan** (brief step 2): WordPress structure, custom tables
   vs post types (EveryNearby's lesson: weigh a plain custom table against
   GeoDirectory), plugin layout, hosting needs, the few third-party plugins wanted and
   why. Then he buys the server and domain, and the build starts on a test copy.

---

## 9. Traps and lessons for whoever continues

- **The first session ran in the cloud** and could not read `C:\`, Irfan's memory, or
  EveryNearby's files. Anything it wrote about EveryNearby comes only from the handover
  document. Check against the real files.
- **Research gaps are real**: competitor structured data, listing freshness samples,
  app-store review text, and OpenStreetMap halal tag counts were not checked.
- **Mealime closes on 21 October 2026** with no export. A comparison page for its
  users is timely, but only once there is something to show.
- **India**: halal labelling is politically sensitive. Neutral wording, evidence shown.
- **UAE**: halal is the default. "Alcohol-free" and "no pork on site" are the useful
  labels there.
- **"Certified" means a certificate we have checked** on the certifier's own site,
  with certifier name and expiry shown. HMC (UK) and HFA (UK) differ on stunning, so
  show the certifier's standard, not a bare "halal".
- **Never charge for halal status or safety filters.**
- **Recipes**: write our own wording and method. No stock photos of food we did not
  cook; illustrations or icons until real photos exist.
- **EveryNearby's lessons** (its handover section 6) apply from day one: version
  control from the first file; a private test copy of the site from the first week;
  the team method from the start; a second backup copy off the server from the first
  night; cache limits before launch; never write code through a shell heredoc; one
  built stylesheet, never hand-edited; trust definition before code; policies written
  from the code; throwaway-record tests for anything about who may do what.

---

## 10. Things outside the project folder

- **OpenSEO project** "Halal food platform (research)" in Irfan's OpenSEO account:
  holds the keyword research (about 75 credits used).
- **GitHub**: the `halal` folder on branch `ccr-ac5d3aa9-2ek23x` of
  `syedirfanrais-max/cuddle-paws-staff`. Not merged into that repository's main
  branch. Once the local copy is confirmed, it can stay as a backup or be deleted, on
  Irfan's say-so.
- **The first cloud session**: Irfan should stop using it after the move and can
  archive it.
