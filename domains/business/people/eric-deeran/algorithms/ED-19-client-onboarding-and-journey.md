---
id: ED-19
person: eric-deeran
departments: [client_success, operations, technology]
source: stated
---

# ED-19 — New client A–Z: payment, contract, account access, client CRM build, client journey

`source: stated` (S-14, sections "New Client Checklist A-Z Customer Journey" and
"Onboarding and Client Management/Client Journey") unless marked. Restated in our words.

**Tool note.** Account access steps are Meta Business Manager as recorded; the client build
is GoHighLevel (his white-labelled account); project boards are monday.com; client chat is
Slack. Menu paths date fast. The order and the reasons do not. `source: derived`.

## Purpose
Turn a "yes" on the sales call into a paid, signed, connected client whose system is built
and whose journey is mapped, so every client gets the same experience and none is left
behind.

## When to use
From the moment a prospect agrees to buy, through the first month of delivery.

## Inputs
The agreement template, a payment processor, your Meta business account, a CRM account to
create for the client, the client-journey board template, the onboarding script (a download,
not in the video — H-9).

## Steps (his order)

### A. Acquisition — on the sales call itself
1. **Take payment first.** He processes payment on the call (card or bank transfer details
   taken over the phone, through Stripe or an ACH-capable tool) (S-14 · lesson 287
   "Acquisition: Payment"). See open edges.
2. **Sign on the call.** Draft the agreement **before** the sales meeting so it can go out
   the moment they say yes: fill in services, price, both company names and the governing
   state, export to PDF, send through an e-signature tool (S-14 · lesson 288 "Sign
   Agreement/Contract"). He says to have it reviewed by a lawyer; he names a low-cost review
   service at about **$25** `[tag: assumption] stated by S-14 · lesson 288; price not checked`.

### B. Account connection — get access, never logins
3. From your own Meta business account, **request access** to the client's Page and to their
   ad account (by its ID, which you ask them for) (S-14 · lessons 289, 290). `source: derived`
   — the method is request-access rather than asking for the client's password.
4. Create a pixel per client (or per audience) in their events manager and install it on the
   client funnel (S-14 · lesson 291; a recorded working session with a member).
5. Verify the client's domain in Meta with a DNS text record; allow a few hours to propagate
   (S-14 · lesson 292).
6. Show the client where their lead-form leads live and how to download them
   (S-14 · lesson 293).

### C. Build the client's own CRM
7. Link the domain to the client CRM (CNAME, any prefix such as `crm.` or `www.`)
   (S-14 · lesson 294).
8. Create the client's CRM account. He recommends **monthly** billing unless you expect to
   keep the client more than a year, and the **client's own card** unless the cost is built
   into your retainer (S-14 · lesson 295).
9. Add yourself and your team to the client's account as staff, with permissions and
   calendars (S-14 · lesson 296).
10. Build the client funnel from a template (free-training funnel: three pages), rebrand it,
    set SEO data and the share image on **every page**, put tracking codes in page settings
    (S-14 · lessons 297, 298); adjust the pop-up and forms (299, 300).
11. Create a calendar group named for the client; have the client connect their own Zoom and
    Google calendar; add qualifying questions for **their** customers; check the calendar
    shows under their staff account (S-14 · lesson 301).
12. Give the client a text line (S-14 · lesson 302); it still needs A2P (ED-09).
13. Customise three automations to the client's brand — the free-training email follow-up,
    the booked-call reminders, and the opt-in text that offers the lead magnet. The opener
    changes by niche: a fitness client offers the challenge, a roofer offers the quote
    (S-14 · lesson 303). If you run a reactivation for the client, rewrite that too.
14. Connect the client's Facebook lead form to the CRM and map name, phone, email, address
    (S-14 · lesson 304). A lead form needs a privacy-policy link; take the client's own, or
    generate one (S-14 · lesson 305 "Ads Privacy Policy").

### D. Kickoff and the client journey
15. Run the kickoff / onboarding call from his onboarding script (S-14 · lesson 249; the
    script itself is a download, not in the video). A member's example onboarding board lists
    about 20 items to cover on that call and the logins needed for done-for-you posting
    (S-14 · lesson 251 "Example Client Journey").
16. **Map the client journey** (S-14 · lesson 250 "What Is A Client Journey…"): every step the
    client goes through after paying, by month, week or stage — one board per client, each
    step marked done with its date. Example first month: book the kickoff, ideas, shoot,
    deliver.
17. **Mark activation points** — the milestones that make a client more likely to stay
    (e.g. content shot; content delivered; content posted; traffic up). They need not be
    money results (lesson 250).
18. **Give the client access to the board**, so they always know where they are and what is
    next. He models it on how his own programme shows students their board (lesson 250).
19. A member's working version (lesson 251), offered as an example, not a rule: a 12-month
    package board whose first month front-loads quick wins (short-form content for an early
    impact), asks the client to book their own testimonial subjects now (scheduling takes
    time), books the production day and location scout, sends a short tutorial on the review
    tool, delivers a first draft and revisions, sends a post-delivery survey, and marks
    "videos and stills delivered" as the activation point. Separate master checklists for
    location scouts, gear and the shoot day.

### E. Communication
20. **One channel**: a private Slack channel per client with their whole team; tell them at
    the start it is the only channel. Recorded Zoom calls for check-ins, posted back into the
    channel (S-14 · lesson 252 "Client Communication - Best Practices").
21. **Cadence over volume.** When a client feels they are not getting value and you cannot
    deliver more output, communicate more: a note at every finished step, proactive updated
    deadlines before they ask, and check-ins along a long edit. His analogies: a pizza
    tracker and mirrors in a lift — progress shown makes the wait feel shorter (lesson 252).
22. Survey, KPIs and back-end offers continue in ED-10.

## Decision points
- They said yes on the call → payment, then signature, before the call ends (steps 1–2).
- Client pays for their CRM vs. you do → depends on whether the retainer covers it (step 8).
- Client unhappy but output cannot grow → raise communication cadence, not output (step 21).

## Outputs
A paid and signed client; Meta access, pixel and verified domain; a branded client CRM with
funnel, forms, calendar, text line, lead-form link and automations; a shared journey board
with activation points; one communication channel.

## His stated benchmarks
- Contract review cost ~$25 `[tag: assumption] stated by S-14 · lesson 288`.
- Domain verification "a couple of hours" `[tag: estimate] stated by S-14 · lesson 292; DNS
  propagation varies`.
- No retention or speed-to-first-value targets in these lessons; see ED-10.

## Sources
S-14 lessons 249–252 and 287–305.

## Open edges
- **Card details over the phone.** Reading a card number aloud on a call, and anyone writing
  it down, raises card-data handling rules (PCI). Our version sends a payment link the
  client completes themselves while still on the call. `source: derived`.
- **Pay before sign** is his order. Paying before the terms are signed leaves both sides
  without written terms for a moment; we would send the agreement and the payment link
  together and take both before ending the call. `source: derived`.
- **Generated privacy policies for a client's lead form.** A generator's text has to match
  what the client really does with lead data; a lawyer's review applies here as in ED-09.
- **Onboarding script** content is not in the videos (H-9 stays open for its content).
- **Lesson 251 and 291** are a member's board and a recorded working session; useful as
  examples, not as his own method.
- **Texting the client's leads** carries the same consent and A2P rules as your own (ED-09).

## Canon map
- **Canon Client Onboarding algorithm**, step by step `source: derived`:
  - *pre-immersion prep* ≈ drafting the agreement before the sales call (step 2) and
    requesting account access (B); he has no separate pre-work for the client;
  - *calibration session* ≈ the kickoff call (step 15);
  - *full data capture* ≈ the onboarding script's ~20 items plus the customer-avatar intake
    in ED-10 step 1;
  - *organize* ≈ one journey board per client and one Slack channel (16, 20);
  - *blueprint within 48h* — **missing**: he maps the journey but states no deadline for
    delivering a plan to the client;
  - *build* = part C, the client CRM build;
  - *first result within 30 days* ≈ activation points and the member's month-one quick wins;
    ED-10's time-to-first-value example is 15 days;
  - *monthly review* ≈ the post-delivery survey and check-in calls (ED-10); no fixed monthly
    meeting is stated;
  - *quarterly review* — **missing** in these lessons;
  - *document* = every step on the board, dated.
- **ACE Expansion:** *monthly result reporting* is partly covered by the shared board (status
  is visible) but not by a results report; *quarterly reviews* and *post-sale referral
  sequences* are not in these lessons.
- **For GFunnel builds:** part C is a ready list of what a client account needs, in order,
  that a written brief can specify: domain, staff, funnel pages, forms, calendar group,
  number, three automations, lead-form mapping, policy link. `source: derived`.
