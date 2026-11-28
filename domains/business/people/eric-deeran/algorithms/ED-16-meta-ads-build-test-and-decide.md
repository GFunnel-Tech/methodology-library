---
id: ED-16
person: eric-deeran
departments: [marketing, technology, sales]
source: stated
---

# ED-16 — Meta ads: readiness, account setup, campaign build, testing and the keep/kill decision

`source: stated` (S-14, sections "Setting Up Ads" and "Facebook Ads Course") unless an item
says `source: derived`. Described in our words; no lesson text is copied. Students and their
clients are not named.

**Two generations of teaching sit in S-14 and they disagree.** The "Facebook Ads Course"
lessons (306–346) date from roughly 2020–2022 (they mention COVID store traffic, iOS 14 and
"2022" in titles). The "Setting Up Ads" lessons (225–248) and lesson 173 date from 2025
(lesson 173 is dated "late 2025 October" and names Meta's "Andromeda" system). Where they
conflict, this file gives the 2025 method as the main path and the older one as the
alternative, and marks the conflict. Both describe Meta's interface, which changes often:
**every setting below is `[tag: held-open]` for re-checking against the live Ads Manager
before it is taught** (H-22).

## Purpose
Get a paid lead-generation campaign running on Meta (Facebook and Instagram) for your own
agency or for a client, keep it running long enough to learn, and decide what to keep, fix or
turn off from data rather than feeling.

## When to use
After the offer and the sales process exist (ED-05, ED-07) and the funnel pages are built
(ED-02, ED-08). Not as the first way to find clients when cash is tight — see step 1.

## Inputs
An offer, a repeatable sales process, a VSL or case-study page (ED-17), a CRM with calendar
and email/text automation, a business Facebook page, an Instagram account, a domain you
control, a payment card, and 2–3 finished creatives.

## Steps (his order)

1. **Check readiness before spending** (S-14 · lesson 165 "How I've Spent $1.6M Of My Own
   Money On Ads (Profitably)"; lesson 226 "Overview And What To Expect"; lesson 227 "Common
   Pitfalls + Key Reminders").
   - *Offer first:* it must work on people who have never heard of you ("cold-traffic
     friendly"), and for business buyers it must make them more money than it costs.
   - *Sales second:* a repeatable, written sales process, so setters and closers can be hired
     to handle the call volume ads create.
   - *Follow-up third:* an opt-in, a nurture sequence and calls; he attributes about half of
     his deals to follow-up rather than the first booking `[tag: assumption] stated by S-14
     (lessons 165, 227); range 30–60%; falsifier: our own booking-source split`.
   - *Validate cheaply first if budget is thin:* reactivate past clients, run LinkedIn
     automation and organic outreach (ED-04, ED-06) so the message is proven before ads.
   - *Expectation:* the first ad and VSL usually do not work; he says he needed three or four
     iterations of his own. Changing niche or offer after a week or two of ads is named as the
     most common mistake.

2. **Set up the accounts** (S-14 · lessons 228 "Setting Up Your Facebook Business Manager",
   229 "Setting Up Facebook Ad Manager", 230 "Facebook Business Manager Set Up Check List",
   306 "Creating Your Business Manager Account"). In order: business portfolio → business
   info filled in (he treats this as looking legitimate to Meta) → page → ad account (correct
   time zone; it cannot be fixed later without trouble) → Instagram → dataset (formerly
   pixel) connected to the ad account → domain verified by a DNS text record → CRM connected
   for lead access → payment method → two-factor login for everyone → a primary page set
   (without it you cannot request a client's assets). If a page is "owned" by a former
   agency's business manager, that agency has to release it first.
   - *Pixel / dataset* (lessons 230, 231 "Setting Up Your Facebook Pixel", 311 "Facebook
     Pixel Overview Set-Up"): base code in the funnel's site-wide header; a "lead" event on
     the page after opt-in; a "schedule" event on the thank-you page after booking; the pixel
     ID also on the booking calendar and the opt-in form; advanced matching on; test with
     Meta's event tester or a browser helper. One dataset per market — datasets cannot be
     deleted, so do not make spares, and start a new one when you move to a very different
     audience.
   - *Stop false events* (lesson 234 "Adding GHL Domains To Pixel Block List"): block the
     funnel builder's preview domains in the dataset's block list, otherwise your own
     previews fire leads and Ads Manager reports leads the CRM never received.
   - *Map the form fields* (lesson 235 "Confirming FB Integration With FB"): in the CRM,
     every Meta lead form must show as mapped, or leads never arrive.
   - *For a client* (lessons 308, 309, 310): request access to their page and ad account
     from your business manager by their business ID, with full control; then add yourself
     as a person on each asset.

3. **Pick a budget route and do the arithmetic** (S-14 · lessons 226, 227).
   - *Fast route:* one campaign at about $50–100 a day for 4–5 days with 2–3 creatives; cut
     everything outside your cost-per-lead limit after 4–6 days `[tag: assumption] stated by
     S-14 (lesson 226)`. He recommends it only if you can lose about $2,000 on testing and
     still be fine `[tag: assumption] stated by S-14`.
   - *Slow route:* about $15–20 a day as an absolute floor (about $500 a month); expect two
     to four weeks before a verdict `[tag: assumption] stated by S-14`.
   - *The rule under both:* spend about 3–5× your target cost per lead before judging an ad,
     and the number of days to one lead is target cost per lead ÷ daily budget (his example:
     $50 ÷ $20 = 12.5 days to a fair read) `[tag: forced]` as arithmetic, inputs
     `[tag: assumption] stated by S-14`. Meta's optimiser is said to want about 30–50
     conversion events a week per ad set `[tag: assumption] stated by S-14 (lessons 226,
     227); 50/week in lesson 325; [tag: held-open] Meta's current figure`.
   - *Older alternative (lessons 312, 314, 316, 333):* start at $10 a day, never higher, and
     scale only what wins — `[tag: conflict]` with the 2025 floor of $15–20 and preferred
     $50–100 (H-21).

4. **Build the campaign — the 2025 method** (S-14 · lesson 233 "Setting Up Your Facebook Ad";
   lesson 173 "Ad Creative Diversity Overview (Major Update 2025)").
   1. *Objective:* leads, manual setup (more control than the guided option).
   2. *Names:* start every campaign, ad set, ad and form name with the date, then a short
      description (form type, targeting, place, radius, hook number), so changes can be read
      in order later.
   3. *Budget:* at campaign level to start; $20–30 a day `[tag: assumption] stated by S-14`.
   4. *Ad set:* conversion location = instant form; performance goal = maximum leads while
      the account has no data, switching to "conversion leads" only once there is data.
      Start the next morning if it is after midday, so review finishes before spend starts.
   5. *Audience:* location and radius only; untick the option that lets Meta reach beyond
      the radius; minimum age raised to 25; no detailed interests (he says they now limit
      the algorithm and that **the creative does the targeting**). Aim for an audience of
      about 2 million, at least 1 million; a small market may need neighbouring cities or
      the whole state `[tag: assumption] stated by S-14`.
   6. *One campaign, one ad set, many diverse creatives:* since the 2025 change he no
      longer splits top/middle/bottom of funnel into separate campaigns; the system sorts
      people itself, but only if the creatives are genuinely different (script, format —
      video, image, carousel). Swapping a hook on an otherwise identical video is no longer
      enough variety `source: stated`.
   7. *Instant form:* "higher intent" type (a review step the person must confirm, which he
      says cuts spam); phone verification off (it cuts volume too far); optional greeting
      (he is testing removing it); **conditional logic on one qualifying question first** —
      yes continues, no ends the form on a "not a fit" screen. His rule for the revenue
      threshold in that question: the buyer should make about ten times your monthly price
      (a $3,000-a-month package → about $30,000 a month in revenue) `[tag: assumption]
      stated by S-14`. Then name, email, phone (all required) and company; privacy policy
      link; the "qualified" end screen sends them to the VSL page.
   8. *Ad:* page and Instagram selected; single image or video; up to five primary texts and
      five headlines for Meta to mix; description blank; call to action "Learn more";
      tracking set to the dataset. Build one ad fully, then duplicate it and swap only the
      media.
   - *Older alternative (lessons 312, 313, 318, 322, 323, 335):* a **conversions** campaign
     to a website opt-in, called "the bread and butter"; lead forms described as giving
     more, lower-quality leads; interests and job titles stacked (job title, employer,
     industry associations, schools, trade brands) — `[tag: conflict]` with the 2025
     broad-targeting rule. His own successful-client walkthroughs mix both: one medical-niche
     campaign used state targeting plus detailed job-title targeting (lesson 239), one
     home-services campaign used location only and **ad-set** budgets (lesson 240) —
     `[tag: conflict]` with "always campaign budget" (lesson 321).

5. **Write the ad copy** (S-14 · lesson 232 "Writing Your Facebook Ad Copy"; lessons 327–331).
   Turn the video script into the primary text (with an AI assistant as a first draft, then
   edit and have it reviewed); the first two lines carry the weight because the rest is
   hidden behind "see more"; call out who it is for in the words they use about themselves;
   benefits over features; one call to action; plain language. Headlines: list steps,
   suggest a transformation, or name a problem. See ED-17 for scripts.

6. **Launch and follow up every lead yourself** (S-14 · lessons 226, 227, 237, 310).
   Automated email and text on opt-in; then call and text each lead, calling twice in a row
   ("double dial"), every day for about seven days. He says to do this yourself until the
   offer is validated, because an unproven offer is hard to hand to a setter and needs a
   salaried one. For a client, set the expectation of first contact within 5–10 minutes and
   follow-up before marking a lead dead `[tag: conflict]` on length: 7 days (226, 227),
   5 days (237), 5–6 attempts (310).

7. **Judge with the decision tree, not daily feelings** (S-14 · lesson 237 "Evaluating Ad
   Performance Guide"; lesson 338 "Analyzing Results & Adjusting Based On KPIs").
   - No leads yet → spent at least about $60? If not, wait. If so, the creative or offer is
     not compelling enough → change the creative.
   - Leads coming → check cost per lead, then cost per click, then click-through rate:
     a high cost per click or a low click-through rate points at the **ad** (it does not stop
     the scroll); good clicks but no conversions points at the **page**.
   - Fewer than about 5–10 leads → wait for more before judging.
   - Leads but unqualified → add friction questions (step 9).
   - Qualified leads, called, but no deal → it is a **sales** problem, not an ads problem.
   - A deal closed → make variations of the winning ad.
   - Never decide on one day's numbers; he gives 3–5 days, 4–6 days, 7 days or "weeks" in
     different lessons `[tag: conflict]` (lessons 338, 226, 335/341, 227).

8. **Attribute lead quality to the creative** (S-14 · lesson 238 "Attributing & Tracking Lead
   Quality To Ad Creative"). After each triage call (ED-07), write the call notes in a fixed
   format in the CRM, then look up which ad that lead came from. Over one to two weeks, keep
   and vary the creatives that bring qualified people, turn off the ones that bring people
   with no money or the wrong business — even if their cost per lead looks better. His line:
   the worst outcome is winning without knowing why. `source: stated`. (This answers H-13:
   it is manual, by triage notes, not a tracking tool.)

9. **Fix poor lead quality one question at a time** (S-14 · lesson 236 "Lead Quality Not
   Great?"; already in ED-08 step 3 from S-13). Duplicate the form and add one friction
   question at a time, so a collapse in volume can be traced to the question that caused it.

10. **Track weekly in the sheet** (S-14 · lesson 248 "IMPORTANT! Fill Out Data Tracking
    Sheet"). Four blocks — advertising, funnel, sales, profitability — filled weekly and
    brought to coaching. See ED-08 for the targets.

11. **Scale and retarget** (older generation, S-14 · lessons 311, 319, 325, 326, 334–337).
    - *Waterfall from cold to warm:* start with interests/demographics; once a campaign has
      about 300 video views or page engagers, add an ad set whose audience is a lookalike of
      them; then lookalikes of 100 website visitors, 100 leads, 100 booked calls (100
      purchases for e-commerce). Let the campaign budget pick, and turn off the colder ad set
      when the warmer one beats it `[tag: assumption] stated by S-14 (thresholds)`.
    - *Optimise for the deepest event you get about 50 times a week:* leads first; booked
      calls only once leads run into the hundreds `[tag: assumption] stated by S-14`.
    - *Retargeting:* separate ad sets for 3-, 14- and 30-day site visitors and checkout
      starters, and 60-day page/profile engagers, each excluding buyers and the shorter
      windows so they do not overlap; testimonial-heavy creative; 1% lookalikes.
    - *Frequency:* about 1.1–1.4 on a large cold audience; consider shutting an ad near 2;
      keep retargeting under about 3 `[tag: assumption] stated by S-14 (lessons 326, 338,
      342)`. Changing an ad resets the learning, so add new creative early.
    - *Rules:* automated rules can switch campaigns off at night and on weekends (lesson
      346) — `[tag: held-open]` whether this still suits Meta's current delivery.
    - *2025 note:* lesson 173 says separate top/middle/bottom campaigns are no longer how he
      structures new launches `[tag: conflict]` with lessons 334–336.

## Decision points
- Can you lose about $2,000 on testing? Yes → fast route. No → slow route plus manual
  follow-up, or validate with organic and reactivation first.
- High cost per click / low click-through → fix the ad. Good clicks, no opt-ins → fix the
  page. Opt-ins but unqualified → friction. Qualified but unsold → sales.
- An ad with cheap leads that never qualify loses to an ad with dearer leads that close.
- A small client who wants volume now (lesson 343): fewer steps — calendar embedded under
  the video. A larger buyer: more qualifying steps. `[tag: conflict]` with lesson 227's
  "never skip the opt-in" only in part: the opt-in is kept, the separate application page
  is removed.

## Outputs
A verified business setup with working events, a running lead campaign, a lead-follow-up
routine, a decision log by date-prefixed names, a creative-quality list, a weekly sheet.

## His stated benchmarks
All `[tag: assumption] stated by S-14` unless marked; falsifier for every row: our own
campaigns across ≥3 niches, read from the weekly sheet. Many are older than Meta's current
system: treat as priors, not targets.

| Metric | Stated | Lesson | Tag |
| --- | --- | --- | --- |
| His own ad spend | $1.6M "of my own money" / "upwards of $800,000 of my own money, not including clients" | 165 / 226 | `[tag: conflict]` H-23 |
| Acceptable cost per lead (high-ticket B2B) | up to $70–100 (packages over ~$10k); "$50 is very standard for B2B" | 226, 227 | assumption |
| Cost per lead warning sign | $20–30 (older lessons) | 338 | `[tag: conflict]` with the row above |
| Decision-tree limits | CPC < $5; CTR > 1%; CPL < $60–70 (< $40 good); cost per booked call < $300 | 237 | assumption |
| Cost per click | ≤ $2 ideal, $3–4 too expensive | 310, 338 | `[tag: conflict]` with < $5 (237) and $1.50–3 (S-13) |
| Cost per booked call | $100–300 (about $150 the middle) | 248 | assumption; see H-12 |
| Bookings by source | 20–30% of leads self-book; ~20% of bookings come from email; ~50% of deals from follow-up | 227, 165 | assumption |
| Judge a creative after | ~1,000 impressions per ad (older) | 310 | assumption |
| Ads per ad set | 2–3 (2025) / ≤ 5 (older) / "a ton" of diverse creative (2025) | 226 / 332 / 173 | `[tag: conflict]` |
| Testing cycle to a stable winner | 3–4 weeks | 335 | assumption |
| Student results shown (spend → revenue, CPLs of $6–36, a hook swap moving CPL from ~$70 to ~$13) | various | 168, 226, 239–247 | assumption — case claims, unverified, no denominator (how many students did not get this) |

## Sources
S-14 lessons 165, 225–248, 306–346 (all read). Lesson 344 ("Solar Company Part 2") carries
the same transcript as lesson 343; part 2 itself was not captured (H-26). Lesson 324 is
mostly unrelated conversation; its only method content is uploading a scraped list to build
a lookalike. Related: S-13 (ED-08), S-02 (ED-02).

## Open edges
- **Which generation is current** for objective, targeting, budget floor and structure
  (H-21). Until answered, teach the 2025 path and show the older one as history.
- **Interface drift:** names and options (business portfolio, datasets, higher-intent forms,
  Advantage+ audience, campaign score, conversion leads) are Meta's and change; recheck
  before any lesson is recorded (H-22).
- **Risky plays as taught — do not adopt as-is (extends H-15):**
  - *Special ad categories.* He correctly says credit, employment, housing and social/
    political ads must be declared, and advises avoiding those clients (lesson 312). But his
    worked examples include solar offers framed as "get paid to go solar" and "zero cost to
    switch" (310, 326) and real-estate-agent clients (314); solar financing can fall under
    credit, and the category bans the age/gender/radius narrowing he applies (homeowners
    25–40, minimum age 25). Check each niche against Meta's current category rules first.
  - *Getting past review.* For a disapproved fitness "cash prize" ad he advises removing
    money symbols and rewording until it passes (345). Rewording a claim so a reviewer
    misses it is circumvention; the fix is a claim that is true and allowed.
  - *A false promise to get a phone number.* In one review the form says a copy will be
    texted when nothing is sent, only so people give a real number (343). That is deceptive,
    and calling or texting that number then rests on consent obtained by a false statement
    (see ED-09 on SMS consent).
  - *Testimonials from friends, family or yourself* (343) if they are not real clients
    describing a real experience — endorsement rules require real, typical experiences.
  - *Scraped lists into custom audiences* (323, 324): uploading a lead-scraper's list of
    businesses to build a lookalike requires a lawful basis for that data under Meta's terms
    and privacy law.
  - *Running ads through an influencer's account by logging in as them* (340) — use the
    platform's partnership-ad permissions instead of shared credentials, and disclose the
    relationship.
  - *Unsupported claims and scarcity:* unsourced statistics in ad copy (328: "90% of small
    business owners…") and "only N spots" that are not real limits; Meta disapproves
    misleading claims (the solar review mentions this happening).
  - *Before/after images* are correctly flagged by him as not allowed (345) — keep.
  - *Lead details emailed from a personal mailbox via an automation* (343) — lead data is
    personal data; route it through the CRM.
- **Optimiser thresholds** (30–50 or 50 events a week; 100-person lookalike seeds; 300
  video views) are Meta mechanics he reports; `[tag: held-open]` against Meta's current
  documentation.

## Canon map
**ACE Acquisition**, almost step for step `source: derived`:
- *Centralize attention channels:* ads feed the same CRM as organic content, reactivation
  and LinkedIn outreach; every lead lands in one pipeline (lessons 226, 241, 243).
- *Tag at capture:* the instant form's qualifying answer, company, and the source ad (via
  date-prefixed ad names and the dataset's lead/schedule events) are attached at opt-in;
  lesson 238 is the manual version of tagging the creative.
- *Automate first response:* opt-in triggers email and text at once; owner notification;
  first call within minutes (226, 310, 343). The canon's automation is the floor; his manual
  seven-day calling is the layer on top.
- *Track ROI per channel:* the weekly four-block sheet (advertising → funnel → sales →
  profitability) and return on ad spend per campaign (248).
- *Reallocate:* the decision tree (237) and campaign budget allocation move money from what
  does not convert to what does; the "ad / page / sales" diagnosis says which stage to fix.
**ACE Creation** — the ad and VSL pre-frame the seven-step script (see ED-17); the "it is a
sales problem" branch hands off to ED-07. **ACE Expansion** — served clients become the case
studies and testimonial retargeting creative (311, 334, 336). Canon Estimate Protocol: every
benchmark above is a tagged prior, not a target. See `registers/canon-map.md`.
