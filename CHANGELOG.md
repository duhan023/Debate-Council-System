# Changelog

## 1.2.0 — 2026-09-16
- Added the **Boardroom** skill: an executive committee (CEO, CFO, CTO, COO, CRO/GC, CHRO, VP owners, three-professor advisory bench) that pre-mortems a council verdict and rules GO / GO-IF / NO-GO with a first move. On NO-GO it stops and asks the user to decide.
- Debate Council default output is now a single 25–30 word verdict line; the full ruling moved behind `<word> full`.
- `setup.py` now takes `--council-word` and `--boardroom-word` and packages both skills; `--word` kept as an alias.

## 1.1.0 — 2026-09-15
- Renamed public skill to `debate-council`; summon word is now user-chosen (default `debate council`).
- Added `setup.py` to set the summon word and package the skill.
- First-invocation reminder to choose a summon word; never blocks the debate.

## 1.0.0 — 2026-09-15
- Initial release.
- Modes: condensed, `full` (transcript), `gameplan` (top 3 research-backed fixes).
- Judge's prior, mandatory Dissent, Prior check, What-would-flip-it.
- Scoring rubric: evidence tier × logical validity × rebuttal survival.
- Scope boundary for medical, legal and high-stakes financial motions.
