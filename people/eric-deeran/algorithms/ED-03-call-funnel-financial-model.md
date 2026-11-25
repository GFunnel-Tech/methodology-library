---
id: ED-03
person: eric-deeran
departments: [finance, marketing, sales]
source: stated
---

# ED-03 — Call-Funnel Financial Model

`source: stated` (S-06, an interactive calculator). Runnable: `formulas/call_funnel.py`.

## Purpose
Decide whether paid acquisition into sales calls is profitable, and what to scale.

## Inputs (his defaults, all `[tag: assumption] stated by S-06`)
cost per qualified lead ($65 implied) · cost per qualified booked call ($200) ·
show rate (70%) · close rate (25%) · average cash collected up front ($10K) ·
average contract value ($15K) · monthly ad spend ($10K).

## Formulas (`source: forced` — arithmetic, read from S-06 "How it reads")
1. booked calls = ad spend ÷ cost per booked call
2. leads = ad spend ÷ cost per lead; booking rate = cost per lead ÷ cost per call
3. live calls = booked × show rate
4. clients = live calls × close rate
5. cash per booked call = show × close × avg cash
6. ROAS = revenue ÷ spend (run twice: on cash collected, and on contract value)
7. ROI = (revenue − spend) ÷ spend
8. CAC = spend ÷ clients
9. break-even close rate = cost per call ÷ (show × avg cash)

With his defaults: 50 calls → 35 shows → 8.75 clients; $87,500 cash; cash ROAS 8.75×;
CAC $1,143; break-even close 2.9% — matching S-06.

## His decision rule (S-06)
If every KPI is healthy, the lever is **spend**: raise budget while watching CPL and show
rate for slippage. (Red-flag rules for unhealthy KPIs not visible on the public page — H-7.)

## Open edge
The model has no churn, no fulfillment cost and no sales commission, so "net" is before
delivery cost. Our version should add those (derived extension, labelled).
