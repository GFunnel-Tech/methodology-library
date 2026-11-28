---
id: ED-18
person: eric-deeran
departments: [technology, sales, operations]
source: stated
---

# ED-18 — CRM build: pipelines, speed to lead, calendars, funnel pages, tracking sheets

`source: stated` (S-14, sections "CRM 101 - The Basics", "Setting Up Your Call Calendar
Inside The CRM", "Understanding How To Manage Your Pipeline", "Sales Tracking Sheet + How To")
unless marked. Restated in our words; no course text copied. Most lessons in "CRM 101" are
taught by a member of his team, not by him; we still cite them as his course (S-14).

**Tool note.** The CRM is **GoHighLevel**, sold to students as his own white-labelled
account (S-14 · lesson 295 "Creating Customer CRM Account"; lesson 136 "How To Sign Up For The
CRM"). Every menu name, setting and default below is GoHighLevel's as recorded in the videos;
these date fast. The **method** (two pipelines, speed to lead, qualify before the long call,
one source of numbers) does not depend on the tool. `source: derived`.

## Purpose
Put every lead, conversation, appointment and deal in one system so nothing slips at volume,
and so the funnel's numbers can be read daily.

## When to use
Before running any ads (ED-02, ED-08); again when a new rep or a new client account is added.

## Inputs
A CRM account with his pre-loaded snapshot (funnel template, forms, calendars, automations);
a domain; a business phone number; an ad account and pixel; the qualifying questions (ED-07).

## Steps (his order, grouped)

### A. Why and what (lessons 137, 138)
1. He frames the CRM as the answer to volume: a whiteboard cannot hold many leads, and
   untracked deals are money lost. The CRM also holds the source of each lead (ad, page,
   appointment, time stamps), the inbox for every channel, the calendar, payments, and the
   automations (S-14 · lesson 137 "Why You Need A CRM").
2. Connect only what you need from the launchpad; fill in the business profile, your own
   profile and the integrations first (S-14 · lesson 138 "Navigation Inside CRM 101").

### B. Two pipelines (lessons 138, 139, 164)
3. **SDR pipeline** — new lead → booked call, with exits *ghosted* and *not interested / not a
   fit*. **Consultant pipeline** — booked call → sale closed, with exits *not a fit* and
   *no-show*, plus a *hot list* stage for near-closes (S-14 · lesson 139 "How To Keep Your
   Pipeline Organized"; lesson 164 "Understanding Pipelines 101").
4. The split mirrors the future team: setters work the first, closers the second, and the
   closer reads the lead's history before the call. A solo founder runs both.
5. In the SDR pipeline, try a new lead by call and text **at least 5 times** before giving up
   `[tag: assumption] stated by S-14 · lesson 164`. Notes and follow-up tasks live on the
   lead's record. A LinkedIn pipeline and a reactivation pipeline exist but are taught
   elsewhere (lesson 164 points ahead to them).

### C. Speed to lead (lesson 140)
6. When a lead arrives, the phone alert is the trigger: **call within 5 minutes**, inside
   business hours. His reasoning: most traffic is on mobile, so the phone is still in the
   lead's hand. Texting automations are a backstop, not the main contact
   (S-14 · lesson 140 "Speed To Lead"). The "studies show" claim behind the 5 minutes is
   uncited `[tag: assumption] stated by S-14; falsifier: our own contact-time vs. booking-rate data`.

### D. Phone, calendar sync, calendars (lessons 141–143, 162, 203–206)
7. Buy a number with a **local area code** for the area you serve; a toll-free or
   out-of-town number looks less familiar (S-14 · lesson 141). It cannot text until A2P
   registration passes (ED-09).
8. Sync your own calendar one-way; add any other calendars as *conflict* calendars. Two-way
   sync interferes with the automations (S-14 · lesson 142).
9. **Decide one-call or two-call close first**, because it decides the calendars
   (S-14 · lesson 143 "How To Set Up Your Call Booking"):
   - **one-call close**: the strategy-session calendar is the public booking page;
   - **two-call close** (the team member's own preference): a public *discovery* calendar
     (15–20 min, 30-min slots, so a 10-min buffer) and an **internal-only** *strategy
     session* calendar (45 min, 60-min slots) that you book yourself at the end of discovery;
   - plus the bot's **game-plan / triage** calendar, a 15-min phone call (ED-20).
   He calls the result "three calendars" for a two-call close (S-14 · lesson 162 "CRM Tech Check").
10. Calendar settings he recommends: show **6 days** ahead so a Thursday visitor still sees
    next week; auto-confirm on; allow guests (so decision-makers can be added); rescheduling
    allowed, cancelling not; booking link expires about an hour before the slot
    `[tag: assumption] stated by S-14 · lesson 143; tool defaults, date fast`.
11. Attach the **qualifying-question form** to the public calendar (S-14 · lessons 144/203
    "Qualifying Questions…"; 145/204 "How To Add Questions…"). The questions and their
    purpose are already in ED-07 step 1; what the video adds is **why each one is there**:
    priority-this-year then biggest-challenge is meant to open a gap in the lead's own mind
    before the call; monthly revenue screens out businesses with no money ("do not try to
    save a sinking ship" while inexperienced); past spend and why/why not surfaces hidden
    objections early, so the call can bring the matching case study; "anything else" often
    reveals a budget. Make the custom questions required (lesson 204).
12. Turn on the **booked-call reminder workflow** (S-14 · lesson 205): tag the contact,
    create the deal in the consultant pipeline, send a confirmation with a pre-call training
    or case-study link, a one-day-before check that asks for the lead's website, and a
    two-hours-before check about the meeting link. For a two-call close, duplicate it for the
    strategy call and remove the repeat training link (S-14 · lesson 157).
13. Embed the booking calendar on the funnel page (S-14 · lesson 206).

### E. Funnel pages and domain (lessons 146–152, 154, 297–299)
14. Point a **subdomain** (he suggests `learn.`) at the funnel with a CNAME record; never the
    root domain, which would take over an existing website (S-14 · lesson 146 "How To Set Up
    Your Domain").
15. Rebrand every page of the template: anything in square brackets is yours to replace;
    anything in curly braces is a CRM merge field to leave (S-14 · lessons 147, 152, 157).
    The opt-in page's "who we are" section is written to be **cross-checked by the SMS
    reviewers** for A2P, so it must describe the real business clearly (lesson 147).
16. Pages in order: opt-in (with a form pop-up) → VSL page with the booking calendar →
    thank-you page carrying a **pre-call video** that sets expectations (quiet place, what to
    bring) → privacy and terms pages (S-14 · lesson 147; lesson 154 for uploading the VSL).
17. SEO fields on the **opt-in page only**, so search does not land people past the opt-in
    (S-14 · lesson 150). `[tag: conflict]` A later lesson says to set SEO data on **every**
    page (S-14 · lesson 298 "Changing SEO Data"; lesson 297). Our reading: the first is about
    his VSL funnel, the second about client sites. `source: derived`.
18. Test every button, the nav anchors and the form's next step before launch
    (S-14 · lesson 151 "How To Make Sure Everything Functions").

### F. Tracking and lists (lessons 156, 160)
19. Pixel on the opt-in form (lead event) and the booking calendar; then, for fuller
    tracking, the base code in the funnel header and a small event script per page — a
    *lead* event on the VSL page and a *schedule* event on the thank-you page
    (S-14 · lesson 160). Conversions API is offered as a later step, with the team's help.
20. Import a lead list as a CSV with only name, email, phone and address mapped
    (S-14 · lesson 156). See the open edge on texting imported lists.

### G. Tech check before ads (lesson 162)
21. Before launch: terms and privacy linked on the form checkbox and in the footer; buttons
    working; the calendars right for your close type; the three base automations published
    (AI triage bot, game-plan reminders, booked-call reminders, ED-20); the phone's A2P
    brand and campaign approved (ED-09). Optional: the platform's stock email drip after opt-in.

### H. Sales tracking sheets (lessons 134, 135)
22. **Beginner sheet** (one person, on monday.com): each day log conversations had, calls
    booked, calls showed, calls closed, revenue sold, cash collected; the month sums itself
    (S-14 · lesson 134 "Sales Tracking Sheet (Beginner)").
23. **Advanced sheet** (a team): a setter tab (hours on outreach, referrals, follow-up and
    new outreach counts, triage calls offered and booked, sales calls offered and booked,
    closes from their bookings, cash, and an end-of-day list of names booked and closed) and
    a closer tab (self-generated meetings, new and follow-up meetings, connected calls,
    offers made, follow-ups set, closes split first-call vs. follow-up, deposits,
    down-sells, revenue sold vs. collected, lead source, upsells), plus leaderboards and each
    rep's income goal (S-14 · lesson 135). This is the same data ED-11 step 5 lists from the
    written dashboard; the video adds the targets below and how to read them.
24. **The CRM holds the notes; the sheet holds the numbers** — he keeps the two apart
    (lesson 135).

## Decision points
- One-call vs. two-call close → which calendars and reminder workflows exist (step 9).
- Lead arrives in business hours → call now; outside → automations carry it (step 6).
- Data patterns he reads (lesson 135): long hours but few messages → a 1:1 with that setter;
  offered calls not being booked → setter problem; many first-call closes but few follow-up
  closes → the call is not giving enough value to earn a second call; low offer rate → the
  leads are not qualified.

## Outputs
A configured CRM account, a live funnel on a subdomain, three calendars, tracking pixels,
two pipelines, and a daily numbers sheet per person.

## His stated benchmarks (all `[tag: assumption] stated by S-14`; falsifier: our own logged data)
| Metric | Stated | Source |
| --- | --- | --- |
| Conversations per person per day | minimum 25, goal 50 | lesson 134 |
| Setter inputs (messages + calls) per day | 150 | lesson 135 |
| Booked sales calls per setter per month | 100 (depends on niche) | lesson 135 |
| Sales calls offered → booked | about 75% | lesson 135 |
| Closed vs. booked (setter view) | 7% acceptable, above 10% wanted | lesson 135 |
| No-show rate | below 30% (i.e. show ≥70%) | lesson 135 |
| Offer rate on connected calls | 80–90% | lesson 135 |
| Close rate on connected calls | above 20%; 10% "ok to start"; aim 20–30% | lesson 135 |
| Lead follow-up attempts | at least 5 | lesson 164 |
| Call a new lead within | 5 minutes | lesson 140 |
| Discovery / strategy / game-plan call | 15–20 / 45 / 15 minutes | lessons 143, 163 |

`[tag: conflict]` The close-rate range (10–30%) sits under the written closer minimum of 30%
(ED-11) and the funnel sheet's 20–25% (ED-07, ED-08); see H-12. The 70% show floor matches
ED-11 and the calculator (ED-02).

## Sources
S-14 lessons 134–164 and 203–206; lessons 297–299 for client-site page settings.

## Open edges
- **Texting imported or old lists.** The course itself warns not to feed the texting number
  lead lists that did not come through your own ads, because an opt-out rate above about
  **2%** gets the account flagged `[tag: assumption] stated by S-14 · lesson 159; GoHighLevel's
  threshold as reported, date fast`. Whether a contact may be texted at all depends on the
  consent they gave, not on the CRM (see ED-09, ED-04 open edges).
- **Template proof numbers.** The funnel template ships with example counts (locations,
  members, projects, satisfied clients). The lesson says to change or delete them; a student
  who leaves them in publishes made-up proof. Our version: no number on a page that we have
  not measured (S-14 · lesson 147).
- **Privacy/terms drafted by AI with "answer yes if unsure".** Lesson 155 tells students to
  answer yes to any AI interview question they are unsure about. A yes can commit the
  business to practices it does not follow. The lesson itself says to have a lawyer review
  the result; we would drop the default-yes rule. Ties to ED-09.
- **Policies must not mention sharing lead data with third parties**, per the reviewers as
  reported (lesson 162). True or not, a policy has to describe what the business really
  does; if it does share data (with its CRM, its ad platform), deleting the sentence to pass
  review makes the policy false. Needs a legal read.
- **Conflict of interest.** The CRM he recommends is one he resells. That does not make the
  advice wrong; it is a reason to judge the tool on its own.
- AI Studio (lesson 149) was described as a free beta at recording; pricing and features are
  unknown now.

## Canon map
- **ACE Acquisition:** *centralize channels* = the CRM's single inbox and the two pipelines;
  *tag at capture* = the booked-call workflow tagging the contact and the lead source on the
  closer sheet; *automate first response* = the booked-call reminders and the AI bot (ED-20),
  with the human 5-minute call ahead of them; *ROI per channel* = the closer sheet's lead-source
  column and pixel events — he tracks source, not cost per channel, here.
- **ACE Creation:** the seven-step script is not in these lessons; the qualifying form feeds
  its discovery stage (ED-07).
- **Database step (document everything in the CRM):** stated almost word for word in his
  "CRM holds the notes, the sheet holds the numbers" rule — with one split the canon does
  not make: numbers live in a separate sheet. `source: derived`.
- **For GFunnel builds:** steps A–G are close to a checklist a written brief can drive:
  pipelines with named stages, three calendars by close type, reminder workflows, pixel
  events, A2P prerequisites. `source: derived`.
