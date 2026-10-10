# Product note: the halal site

Status: **draft**. Items marked **Decided** come from Irfan's brief of 9 October 2026
or his later answers (quoted). Items marked **OPEN** wait for him. Recommendations
are the first session's, not decisions.

## 1. Purpose

**Decided.** "Plan halal meals at home and find halal food anywhere, free."

Two connected parts:
1. **Meal planner** for home cooking: a 7-day plan from our own recipes, a combined
   shopping list grouped by aisle, shareable on WhatsApp and printable. Includes a
   Ramadan mode (suhoor and iftar plans with fasting times) and an ingredient
   checker ("is this halal?").
2. **Restaurant finder** for eating out and travel: country, city and area pages,
   listing profiles with halal status, source and date checked, report and claim
   flows, and "Halal food in [city]" travel guides.

## 2. Users and places

**Decided.** Muslim families and individuals worldwide. First focus: UAE, India,
UK, US, Canada, plus Muslim travellers in non-Muslim countries. Irfan is based in Dubai.

**OPEN: order of countries for restaurant pages.** Recommendation from the Phase 1
study: planner open to everyone from day one; restaurant pages first in UK, Canada
and US cities (where people search for halal most); UAE and India restaurant pages
hidden at first (halal is the default in the UAE; halal labels are politically
sensitive in India).

## 3. What "halal" means on the site, and who says so

**Decided (brief).** Restaurant labels, each shown with the source and the date last
checked:
- "Halal certified (certificate on file)"
- "Halal meat served (owner or user reported)"
- "Muslim-owned"
- "Not verified"

Never show "certified" without a certificate. The site states the basis; it does not
issue religious rulings. Users are told to confirm with the restaurant.

Ingredient checker entries are marked halal, doubtful or not halal, with the reason
and a safer swap. Conservative; explains where scholars differ.

**OPEN:**
- Exact written definition of each label (what evidence, who checks, how it expires).
  Recommendation: "certified" only after the certificate is checked on the
  certifier's own site; show certifier name and expiry; show alcohol served and pork
  on premises as separate facts.
- Who reviews the religious wording (a named scholar or imam?).

## 4. Money

**Decided (brief).** Free first. Later: ads, a premium tier of about US$3–5 a month,
grocery affiliate links, featured restaurant placement once the business is licensed.
Premium is built behind a switch; no payment provider until decided.

Recommendation from Phase 1: never charge for halal status or safety filters;
featured placement never changes how halal status is shown.

## 5. Name and domain

**OPEN.** Irfan's to choose and buy.

## 6. Connection to EveryNearby

**OPEN.** Recommendation: fully separate site, server, accounts and keys; reuse the
method and tools by copying.

## 7. Languages

**Decided (brief).** English first; built so Arabic (right-to-left) and Urdu can be
added later without a redesign.

## 8. Platform and operating context

**Decided (brief).**
- WordPress, with our own theme and plugin. Third-party plugins only where truly
  needed, each listed with the reason.
- Fully automated, no staff. Human tasks: approving disputed listings and reviewing
  flagged content.
- Rule-based plan generation, no paid AI at runtime; results instant.
- Mobile first, tested at 360px; 4.5:1 contrast; 44px touch targets; main content in
  2.5 seconds on a mid-range phone on 4G.
- Security: few plugins, automatic updates, firewall, two-step sign-in for admins,
  rate limits and Cloudflare Turnstile on forms, image-only uploads re-encoded,
  daily off-site backups, staging for all changes, no secrets in front-end code.
- Cookie-free analytics so no banner is needed.
- Never publish live without Irfan's explicit go-ahead.

**Decided (10 Oct 2026):** "build here first": work starts in this cloud session,
in this folder, before any server is bought.

## 9. Data sources

**OPEN, pending the OpenStreetMap decision.** Recommendation from Phase 1:
- Base list of real businesses: Overture Maps Places (permissive licence, no OSM data).
- UK: Food Standards Agency hygiene data (Open Government Licence) for "still trading".
- City open data where licensed (NYC, Toronto and others).
- Halal status: owners, users, and certificates checked one by one on certifiers'
  own sites (link, never copy their lists).
- Never: Google, Yelp, Tripadvisor, Zomato content, or other halal directories.
- OpenStreetMap: option A (none), B (everywhere, publish listing facts under ODbL),
  or C (only in travel-guide countries, separate tables). Recommendation C, with
  the lawyer.

## 10. Launch scope

**OPEN.** Recommendation: meal planner, recipes, ingredient checker and Ramadan mode
first, on a test copy by mid-January 2027, ready for Ramadan (expected about
8 February 2027). The restaurant finder follows, city by city, once a city has
enough real listings (proposed: 20 listings with a status better than "Not verified",
checked in the last 12 months, at least 3 cuisines).

## 11. What it will not do

- Rule on what is halal.
- Copy other sites' data, recipes or photos.
- Show stock photos of food we did not cook.
- Sell or share users' location.
- Hide halal status or safety filters behind a payment.
