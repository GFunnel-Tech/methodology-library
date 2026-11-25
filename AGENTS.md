# AGENTS.md — rules for working in this repository

Load the canon first (`GFunnel-Tech/methodology`, its `AGENTS.md`), then this repo for the domain playbook.

1. **Methods, never copies.** Describe what he does and why, in our words. Never paste
   course text, scripts, slides or transcripts into a committed file. A short quote (one
   sentence) is allowed only when the exact wording is the method (e.g. a named step).
2. **Every claim has a source.** Cite `S-##` from `sources/register.md`, plus a module or
   timestamp where there is one.
3. **His framing vs. ours.** A file says, per item, `source: stated` (he says this) or
   `source: derived` (we inferred it from his material). Never present a derivation as his.
4. **Every number carries a tag** — `measured` · `forced` · `estimate` · `assumption` ·
   `held-open` · `conflict` — written as `[tag: …]`. His own figures ("~70% show rate",
   "828+ clients", case-study revenue) are **marketing claims**: tag them `assumption`
   with `stated by S-##`, a range, and what would falsify them. Never restate them as fact.
5. **Hold open what is not known.** Add it to `registers/held-open.md` with the
   measurement that would close it. Do not fill a gap to make a page read as finished.
6. **Header and naming.** Every algorithm and pattern opens with a header: `id` (person prefix + number), `person` (folder slug), `departments` (from the nine in `methodology.json`), `source` (`stated` or `derived`). After any change run `python3 tools/build_index.py`; `--check` must pass. A new person gets a folder `people/firstname-lastname/`, a unique two-letter prefix, a `methodology.json`, and an entry in the root `methodology.json`.
7. **Algorithm file shape:** purpose · when to use · inputs · steps (numbered, in his
   order) · decision points · outputs · his stated benchmarks (tagged) · sources ·
   open edges · canon map.
8. **Private repo.** Keep it private; no client names beyond what he published, and no
   personal data of his clients.
