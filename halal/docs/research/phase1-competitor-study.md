# Phase 1: competitor study (9 October 2026)

Saved from the report given to Irfan in chat, so later sessions can read it.

## Limits of the research

- The cloud environment's network policy blocked direct page reads for competitor
  sites, app stores, Reddit and OpenStreetMap hosts. Findings come from search-result
  summaries, press, public app trackers, and Overture Maps' official docs and files.
- Not done: checking competitors' structured data, sampling listings for dates and
  closures, reading full app-store and Reddit reviews. App ratings come from trackers.
- Keyword volumes: Google Ads-based monthly averages (OpenSEO project "Halal food
  platform (research)"). Ramadan terms spike in season, so averages understate peaks.
- No data was copied: no logins, no competitor APIs, no listings, reviews or recipes.

## Halal restaurant finders

| Competitor | Offer | Price | Revenue | Data source | Halal labels | Strengths | Weaknesses |
|---|---|---|---|---|---|---|---|
| Zabihah (about 50–60k places) | Finder, mosques, reviews, delivery links, shop, scanner | Free | Shop, delivery referrals; partner API $99/month | 25 years of user submissions, owners, certificates | HalalRank 0–100 with tiers; full/partial; alcohol; certifier; hand-slaughtered. Listed if one halal-meat dish. Disputes shown with evidence, not removed | Best-known brand; evidence-based score | Stale and closed listings; few reviews; messy URLs after migration |
| HalalTrip / CrescentRating | Finder, prayer tools, travel packages, city guides | Free | Travel sales; B2B "Muslim-friendly" ratings (C–AAA) | Users, editors, rated venues | Free text, inconsistent | Global reach; travel index authority | Pages 4–10 years old; parameter URLs indexed |
| Halal Navi (Japan) | About 800 restaurants, prayer spaces, "Halal Tips" | Free | Unclear; Instagram-led | Users and editors | Certifier named; menu vs whole-kitchen; alcohol-free, pork-free | Most detailed labels; fresh | Japan only; Android 2.9 |
| Muslim Pro (halal places) | Finder inside a prayer app | Premium $12.99/month or $34.99/year | Subscriptions, ads | Foursquare keyword match | None | Huge user base | Shallow data; 2020 location-data scandal |
| Have Halal Will Travel | Editorial guides "(2026 Guide)" | Free | Native ads for tourism boards and brands | In-house editors | Certified, Muslim-owned, Muslim-friendly, self-certified, partial | Strong search pages | Mostly SE/E Asia |
| Halal Gems (UK, Amaliah) | Reviews, city lists, app | Free | Media, events | Editors | "All meat halal / alcohol served" | Trusted UK voice | Old reviews; no single UK guide brand exists |
| Certifier lists (HMC, HMS, HMA, Shariah Board) | Certified outlets | Free | Certification fees | Their audits | Certified; HMS validity date; HMC spot-check months | Most trustworthy | Narrow; no open licence |
| Yelp, Tripadvisor, Uber Eats, DoorDash, Google | Halal category or tag | Free | Ads, commission | Businesses themselves | Self-chosen tag | Dominate US "near me" | No certification or alcohol detail |
| Newer evidence-first sites (HalalSpy, HalalVouch, halalcodecheck, Halal Hit List, CraveHalal) | Verified lists with dates | Free | Unclear | Calls, visits, certificates | Status + evidence + date | Show where the market is going | Small, local |

Other-diet finders (structure lessons):
- **HappyCow**: three clear tiers; hubs `/{continent}/{country}/{region}/{city}/`;
  `/best-vegan-restaurants/{city}`; "reported closed [month/year]"; featured placement
  $100/month per location; weaknesses: duplicate URL trees, spam city names, slow approval.
- **Find Me Gluten Free**: programmatic "city × topic" and "landmark × topic" pages;
  "reported dedicated gluten-free" wording; separate safety vote with the vote count;
  Premium $24.99/year; mistake to avoid: safety filters behind the paywall.

## Meal planners

| Competitor | How plans are made | Price | Revenue | Halal-aware | Notes |
|---|---|---|---|---|---|
| Mealime | User picks; aisle-grouped list | Pro $2.99/month | Pro, grocery hand-off | No | Shuts down 21 Oct 2026 (Albertsons); no export |
| Eat This Much | Auto week to calorie/macro targets; budget, time, leftovers | $9/month or $59.99/year | Subscriptions, pro tier, Instacart | No | Strong programmatic pages `/diet-plan/1500-calorie/...` |
| PlateJoy | Long questionnaire | About $99/year | Subscriptions | No | Closed 1 July 2025 |
| Plan to Eat | User's own recipes, manual | $5.95/month or $49/year | Subscriptions | Only via user recipes | Good store-section lists |
| Paprika | Manual calendar, pantry, aisle list | One-off ~$4.99 mobile, $29.99 desktop | App sales | No | Trusted honest price |
| Samsung Food (Whisk) | AI week, fridge photo, 14 diets | Free with ads; $6.99/month or $59.99/year | Subscriptions, ads, appliances | No halal option found | Ads and "health scores" annoy users |
| Small halal planners (FamilyPlate, Zadi, Ramadan AI apps, Noor) | Mostly AI | Free–$4.99/month | — | Claimed, method not shown | Almost no ratings |
| Halal ingredient checkers (Verify Halal, Scan Halal, ~10 AI scanners) | Barcode / E-number | Often $3.99/week or $29.99/year | Subscriptions | Yes | Paywalled; rarely name authority or differences |

Halal recipe audiences are mostly on video (Food Fusion 5M+ YouTube, Masala TV,
Cooking with Alia). Text results for karahi and biryani are won by general recipe
blogs with Recipe structured data.

## Search demand (monthly, 12-month average)

| Keyword | UAE | India | UK | US | Canada |
|---|---|---|---|---|---|
| halal food near me | 590 | 8,100 | 301,000 | 823,000 | 165,000 |
| halal restaurants near me | 1,000 | 27,100 | 165,000 | 450,000 | 135,000 |
| halal restaurants | 3,600 | 6,600 | 74,000 | 201,000 | 49,500 |
| halal food | 1,000 | 8,100 | 33,100 | 301,000 | 27,100 |
| halal pizza near me | – | – | 18,100 | 40,500 | 22,200 |
| halal meat / butcher near me | – | 390 | 22,200 (butcher) | 60,500 (meat) | 18,100 (meat) |
| halal certified restaurants | – | – | 30 | 880 | 90 |
| City examples | restaurants in dubai 33,100 | halal restaurants in bangalore 880; biryani near me 550,000 | halal restaurants birmingham 14,800; halal food manchester 9,900; halal restaurants london 8,100 | halal food nyc 6,600; halal restaurants chicago 2,900 | halal restaurants mississauga 8,100; calgary 4,400; toronto 3,600 |
| Travel: halal food in tokyo / paris | 70 / 20 | 90 (japan) | 390 / 880 (barcelona 1,000) | 390 / 260 | 140 / 70 |
| Chains: is KFC / McDonald's / Nando's halal | – | – | 5,400 / 5,400 / 4,400 (+ "halal nandos" 12,100) | – | Popeyes 1,900; McDonald's 1,000 |
| halal meal plan | <10 | <10 | 70 | 140 | 50 |
| halal meal prep | – | – | 1,900 | 1,000 | 320 |
| meal planner / weekly meal planner | 2,400 / – | 4,400 / – | 8,100 / 2,400 | – / 9,900 | 4,400 / 1,000 |
| halal recipes | <10 | 50 | 480 | 320 | 110 |
| ramadan recipes / iftar recipes | 210 / 210 | 480 / 1,300 | 590 / 260 | 720 / 480 | 260 / 170 |
| Fasting times | iftar time dubai 49,500; sehri time dubai 18,100; prayer times dubai 1.22M | iftar time today 165,000; sehri time today 49,500 | – | – | – |
| is gelatin halal | 90 | 390 | 720 | 880 | 390 |
| is vanilla extract halal | 50 | 140 | 720 | 1,300 | 720 |
| is E120 / E471 halal | 50 / 10 | 90 / 20 | 1,300 / 480 | 260 / 10 | 90 / 10 |
| is cheese / rennet halal | – | 40 / – | 590 / 260 | 720 / 210 | 320 / – |

Who ranks: US "halal restaurants near me" is Yelp, Tripadvisor, Uber Eats, DoorDash
(hard). London, Toronto and Tokyo are Instagram, blogs, Reddit (winnable). "halal
meal plan" shows only meal-prep delivery firms; no planner tool ranks. Ingredient
questions show Quora, manufacturers, fatwa sites, small E-number sites (winnable).

## User complaints (most common first)

Self-declared "halal" (CBC 2024: none of 10 chain branches claimed as certified
were); alcohol at halal-listed places; supply fraud; no zabiha vs machine vs stunned
distinction; unclear which certifier to trust; stale and closed listings; mixed
kitchens; no certificate shown or expired; hidden haram ingredients; poor coverage
outside big cities; bugs and login walls; hard to correct listings; distrust of ads
and tracking. Scholars warn against relying on apps: users want evidence they can
check, not a badge.

## Top 10 gaps and how we fill them

1. Unverifiable halal status → four labels with source and date; separate facts for
   alcohol, pork, whole/partial menu, certifier and standard; personal filter.
2. Stale and closed listings → decay to "needs re-check", one-tap closed report,
   automatic checks against open data, owner reconfirmation emails.
3. No halal-aware planner for Muslim household cuisines → our core offer.
4. Gimmicky Ramadan apps → suhoor/iftar plans with city fasting times and shopping list.
5. Paywalled, unexplained ingredient checkers → free, conservative, explains differences, offers swaps.
6. Home and eating out are separate → one site, one account, linked.
7. Lists can't reach the household shopper → WhatsApp-formatted list, print.
8. Planners close and lock data in → free, export everything.
9. Distrust of ads and tracking → cookie-free analytics, never sell location.
10. Thin and stale competitor pages → clean URLs, structured data, thresholds, dated guides.

## Restaurant data sources

| Source | Licence | Recommendation |
|---|---|---|
| Overture Maps Places (81M; halal signal: US ~4,000, UK ~1,000, Canada ~580, India ~290, UAE 20) | CDLA-Permissive-2.0, Apache-2.0, CC0; no OSM data | Use as the base list of real businesses; mirror deletions (60-day retention) |
| UK FSA hygiene data | Open Government Licence v3 | Use for UK "still trading" |
| City inspection open data (NYC, Toronto, Chicago) | City licences | Use city by city |
| Foursquare open places | Apache-2.0 via portal | Secondary; dedupe against Overture |
| Wikidata | CC0 | Chains, certifiers, multilingual names |
| Certifier lists | All rights reserved | Check one by one and link; never bulk copy; no logos |
| Google, Yelp, Tripadvisor, Zomato | Terms forbid storage | Avoid (Google place ID at most) |
| Owners and users | Our contributor terms | Core |
| OpenStreetMap (diet:halal) | ODbL 1.0 | Decision: A none / B everywhere with ODbL dump / C travel countries only (recommended, lawyer) |

ODbL in plain terms: visible "© OpenStreetMap contributors"; changed or combined OSM
data used publicly must be offered under ODbL; a separate table alone does not avoid
share-alike when OSM and non-OSM restaurants mix in the same area.

Lawyer questions: ODbL share-alike reach; certifier database rights and logos;
liability for wrong halal claims; India certification rules; Foursquare portal terms;
UAE government data licences.
