# methodology-business (PRIVATE)

Researched business methodologies, organised **domain → person → department**, and mapped
to the GFunnel canon (`GFunnel-Tech/methodology`, canon domain 7 Economic / Market).

The canon is GFunnel's own framework (public, CC BY 4.0). This repo holds **other people's
methods**, restated in our own words and credited, so it is kept separate and private. A
method that is tested and holds up can be proposed into the canon through the canon's
contribution process, with credit to its source.

## Layout

| Path | Holds |
| --- | --- |
| `methodology.json` | what this repo is, which canon commit it maps to, who is in it |
| `AGENTS.md` | the rules every person and AI follows here |
| `people/<firstname-lastname>/` | one person's whole system: profile, algorithms, patterns, formulas, sources, registers |
| `departments/<dept>/README.md` | **generated** index of every algorithm touching that department, across people |
| `compare/` | the same problem solved by different people (once there are two) |
| `tools/build_index.py` | rebuilds the department indexes; `--check` fails if they are stale |

## Naming

- Person folder: `firstname-lastname`, lowercase, hyphens.
- Each person has a unique two-letter prefix, recorded in their `methodology.json` and the
  root one. Algorithm IDs: `<PREFIX>-##`; patterns we infer: `<PREFIX>-P##`.
- Departments are the nine the platform uses: strategy, marketing, sales, operations,
  finance, hr, technology, client_success, content.
- Every algorithm and pattern opens with a header (`id`, `person`, `departments`,
  `source: stated|derived`). The indexes are built from it.

## People

| Person | Prefix | Status |
| --- | --- | --- |
| [Eric Deeran](people/eric-deeran/profile.md) | ED | public site done; YouTube and course pending |
