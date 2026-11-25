# methodology-library (PRIVATE)

GFunnel's library of researched and derived methodologies, organised
**domain → person → facet**, every piece mapped to the canon
(`GFunnel-Tech/methodology`, the GFunnel Methodology by Cameron Garlick, CC BY 4.0).

The canon is GFunnel's own framework (public). This library holds **other people's methods**
(restated in our own words and credited) and methodologies we derive for a field. It is kept
separate and private. A method that is tested and holds up can be proposed into the canon
through the canon's contribution process, with credit to its source.

## Layout

```
library.json              every domain, every person prefix, the canon commit we map to
AGENTS.md                 rules for every person and AI working here
tools/build_index.py      rebuilds every facet index; --check fails on stale or inconsistent data
domains/<domain>/
  domain.json             canon domain, the facet it is sorted by, its people
  <facet>/<value>/        generated index (business: departments/<dept>/)
  people/<first-last>/    one person's whole system
    profile.md · methodology.json · algorithms/ · patterns/ · formulas/ · sources/ · registers/
  compare/                the same problem solved by different people
```

## Naming

| Thing | Rule | Example |
| --- | --- | --- |
| Domain folder | one of the canon's ten domains, short slug | `business` (canon 7 Economic / Market) |
| Person folder | `firstname-lastname`, lowercase, hyphens | `eric-deeran` |
| Person prefix | two letters, unique across the whole library (`library.json`) | `ED` |
| Algorithm | `<PREFIX>-##` — his named system | `ED-02` |
| Pattern | `<PREFIX>-P##` — a repeated move we infer | `ED-P01` |
| Header | `id`, `person`, `<facet>` (e.g. `departments`), `source: stated\|derived` | |

## Add a person
1. Create `domains/<domain>/people/<first-last>/` with `profile.md` and `methodology.json`.
2. Pick an unused prefix; add it to `library.json` → `prefixes` and to `domain.json` → `people`.
3. Write algorithms/patterns with the header; run `python3 tools/build_index.py`.

## Add a domain
1. Create `domains/<slug>/domain.json` naming its canon domain and its facet (the categories it
   is sorted by, e.g. departments for business).
2. Add it to `library.json` → `domains`; run the builder.

## Contents

| Domain | Person | Prefix | Status |
| --- | --- | --- | --- |
| business | [Eric Deeran](domains/business/people/eric-deeran/profile.md) | ED | public site done; YouTube and course pending |
