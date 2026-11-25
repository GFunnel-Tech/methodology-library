---
id: ED-09
person: eric-deeran
departments: [technology, operations]
source: stated
---

# ED-09 — SMS compliance: A2P registration, opt-in form, privacy and terms

`source: stated` (S-13, section "CRM 101 - The Basics").

## Purpose
Keep the SMS follow-up in ED-02 legal and unsuspended by registering the sender with US
carriers (A2P 10DLC) and making the opt-in form and policies match.

## When to use
Before sending any SMS from the CRM; again after a suspension.

## Inputs
Legal business identity, the opt-in page, the CRM's first automated message.

## Steps
1. **Write the Privacy Policy and Terms with an AI interview prompt** (S-13 · "Using AI to
   Create Privacy & Terms"): the AI asks one question at a time, confirms each answer, and
   drafts nothing until all are in; it stops and warns if an answer creates a compliance
   risk (for example, sharing mobile numbers). Both documents carry business identity, how
   data is collected (forms, funnels, calendars, surveys, lead ads), SMS disclosures
   (STOP/HELP, varying frequency, rates may apply) and must not contradict each other. The
   privacy policy must say mobile information is not shared with third parties for marketing.
2. **Register the campaign** (S-13 · "A2P - How To Verify Your Phone Number"): separate
   use-case descriptions for **non-marketing** (reminders, confirmations) and **marketing**
   messages; sample messages that name the sender and end with opt-out wording; a consent
   description; an opt-in confirmation message; and **two separate, optional consent
   checkboxes**, one per message type.
3. **Build the opt-in form to the checklist** (S-13 · "What To Do If Your SMS Gets
   Suspended"): checkbox not pre-ticked and not required to submit; message types, sender,
   fees and frequency disclosed; HELP and STOP stated; policy links at the foot of the form,
   outside the checkbox text.
4. **Match the first message to the opt-in** — rewrite the first automated SMS and the AI
   bot's opener so they reflect what the person agreed to; set the compliance sender details
   and opt-out wording in the CRM profile.

## Decision points
- Suspended for high opt-outs → do step 3 and 4 in full; he advises doing them from day one.

## Outputs
Approved A2P registration, compliant form, matching policies.

## Sources
S-13 (three documents).

## Open edges
- The documents reflect carrier rules as of their writing (one is labelled 2026). Carrier
  and CRM rules change; check current rules before relying on them.
- Not legal advice; the AI-drafted policies need a lawyer's review.

## Canon map
Operations / compliance. Matches what the GFunnel platform's own SMS and Lead System setup needs.
