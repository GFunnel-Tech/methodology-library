---
id: ED-20
person: eric-deeran
departments: [sales, technology]
source: stated
---

# ED-20 — AI triage booking bot and the call automations around it

`source: stated` (S-14, sections "How To Use Our AI Booking Bot", "CRM 101 - The Basics" and
"Setting Up Your Call Calendar Inside The CRM") unless marked. Restated in our words.

**Tool note.** The bot is a GoHighLevel workflow his team pushes into each student's account,
with GoHighLevel's AI appointment-booking step inside it; it texts from the account's number.
The exact steps, waits and wording are his template's and change between versions (one
lesson calls itself an update after carrier crackdowns). The shape — confirm number, short
qualifying call booked automatically, multi-day follow-up, pipeline moves — is the method.
`source: derived`.

## Purpose
Book every new lead onto a short qualifying phone call at any hour, without a person texting
them, so the founder or closer only spends a long call on people who fit.

## When to use
Once A2P registration is approved (ED-09) and leads arrive from ads or a lead form (ED-02).

## Inputs
The game-plan calendar (15-min phone call); the AI triage booking bot workflow; the
game-plan reminders workflow; the booked-call reminders workflow; the no-show and post-call
nurture workflows; your offer's outcome in one phrase.

## Steps (his order)
1. **Lead enters** — by funnel opt-in or by Facebook lead form (the workflow trigger must
   match the source) (S-14 · lesson 163 "What To Customize & Overview").
2. **Confirm the number** — the first text asks whether this is the right number. Since the
   compliance update, the opener must also **name what the person opted into** and offer to
   send details, aiming for a simple yes (S-14 · lesson 159 "What To Do If Your SMS Gets
   Suspended").
3. **Introduce** — your name and company (square-bracket fields) (lessons 157, 163).
4. **Offer the short call** — one line on what is working for clients *for the outcome you
   promise*, then the ask for a brief call (lesson 159's updated wording calls it about five
   minutes; the calendar slot is 15). Rewrite the outcome phrase to your offer; if your offer is not
   "scale your business", rewrite the follow-up questions too (lesson 163).
5. **Book** — the AI booking step books the lead onto the **game-plan calendar**; the
   location is set to a phone call, and you call them from the CRM at the time
   (lesson 163; lesson 143 for calendar settings).
6. **Follow up for five days** — if they do not reply, the workflow keeps texting over about
   five days and moves the lead through the SDR stages; after five days with no reply it
   moves them to **ghosted**, from where reactivation picks them up (lesson 163; ED-04).
7. **Game-plan reminders** fire on a confirmed appointment in that calendar (lesson 157).
8. **Run the game-plan call** — 15 minutes to decide: is this someone I can help, and worth a
   45-minute sales call? If yes, book the sales call yourself (lesson 163; ED-07 triage call).
9. **Booked-call reminders** for the discovery or strategy call (ED-18 step 12).
10. **No-show recovery** — moving a deal to the *no-show* stage triggers a sequence that tries
    to rebook (lesson 157).
11. **Post-call nurture** — moving a deal to *follow-up* sends a text, then about five minutes
    later an email, each with more training or proof; you need that material first
    (lesson 157).

## Decision points
- Lead replies and books → booked-appointment stage, new game-plan appointment (lesson 163).
- Five days of silence → ghosted (lesson 163).
- Game-plan call: fit → book the long call; no fit → not a fit (lesson 163).
- In business hours, a human calls first; the bot is the backstop (ED-18 step 6). `source:
  derived` from lesson 140 and lesson 162 ("if you cannot pick up the phone right away").

## What to customise (his checklist, lessons 157, 163)
Every block labelled "customise"; every square bracket; the calendar link in two texts and
one email; the from-name and from-email; the outcome phrase; the calendar chosen in the AI
step; the trigger (lead form vs. funnel); then publish. Read every message for tone.

## Outputs
Short qualifying calls booked automatically; leads sorted into booked, ghosted, no-show and
follow-up stages without manual texting.

## His stated benchmarks
- Follow-up window 5 days `[tag: assumption] stated by S-14 · lesson 163; template setting`.
- Game-plan call 15 minutes; sales call 45 minutes `[tag: assumption] stated by S-14 ·
  lessons 143, 163`.
- "It will book you calls at any time of day" and needs no follow-up from you
  `[tag: assumption] stated by S-14 · lesson 163; marketing claim; falsifier: share of bot
  bookings that show and qualify, against human-booked ones`.

## Sources
S-14 lessons 143, 157, 159, 162, 163, 205.

## Open edges
- **Consent and texting rules.** The bot texts every lead repeatedly for days. That is only
  allowed for people who gave SMS consent of the right kind (marketing vs. transactional),
  and the form must not make consent required (lessons 153, 159, 161; ED-09). Quiet hours and
  state rules on automated texts are not covered in these lessons.
- **"Is this the right number" openers.** The lesson that predates the compliance update used
  a bare number check; the update says the opener must reflect the opt-in. Use only the
  updated form. `[tag: conflict]` between lessons 163 and 159 on the first message.
- **AI saying it is a person.** The lessons do not say whether the bot discloses that it is
  automated. Our version should.
- **Opt-outs.** Lesson 159 reports a flag above roughly **2%** opt-outs
  `[tag: assumption] stated by S-14; GoHighLevel threshold as reported, date fast`. Track the
  rate per campaign.
- Whether bot-booked calls show and close as well as human-booked ones is not measured in the
  course. Held open.

## Canon map
- **ACE Acquisition — automate first response:** this is that step, built. It also *tags at
  capture* (pipeline stage per reply) and keeps one record per lead.
- **ACE Creation:** the game-plan call is the qualification gate before the seven-step script;
  the bot does not run the script.
- **Database step:** every bot move is a pipeline stage on the contact, so the record documents
  itself.
- **For GFunnel builds:** a brief can specify this as data — trigger, opener tied to the opt-in,
  outcome phrase, booking calendar, follow-up length, stage names, rebook and nurture
  sequences, consent fields required to start. `source: derived`.
