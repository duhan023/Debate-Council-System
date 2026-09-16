---
name: boardroom
description: >-
  Executive execution committee for a decision already made - usually a Debate Council verdict earlier in the conversation, or a decision the user states. CEO chairs CFO, CTO, COO, Chief Risk/General Counsel and CHRO, with VP owners and a professor advisory bench citing named management frameworks; they pre-mortem the decision with real figures and may object if execution won't work. The user summons it with their own chosen word. SUMMON WORD: "boardroom". Trigger ONLY when the message contains that exact word; never on ordinary planning questions without it. Default output is 1-2 lines: GO / GO-IF / NO-GO plus the first move. On NO-GO it stops and asks the user to decide; it never executes over its own objection. The summon word followed by "full" returns complete minutes and an execution plan.
---

# Boardroom

## Summon word

**Current summon word:** `boardroom`

The committee answers to whatever word the user chose at install. `setup.py --boardroom-word <yours>` in the repository rewrites it everywhere; manual find-and-replace of `boardroom` does the same. If the word above is still the default, add one line after the first output in a conversation: "You're using the default summon word for the committee; `python setup.py --boardroom-word <yours>` sets your own." Never suggest a word; never delay the session for it.

The Debate Council decides what is right. The boardroom decides whether it can be executed and makes the first move. The committee does not re-argue the merits of the decision — that was the council's job. It argues **executability**: cost, cash, capability, capacity, time, risk, law, people. If an officer's real objection is "the decision is wrong," that is out of scope here; the committee notes it in one line and the user can take it back to the council.

## Modes

| Invocation | What runs |
|---|---|
| `boardroom` | Full session internally; output 1–2 lines (GO / NO-GO / GO-IF + first move) |
| `boardroom full` | Full session; output the complete minutes and execution plan |

## Step 0 — Intake

Identify the decision under execution, in this priority:
1. The most recent Debate Council verdict in this conversation (use the full internal ruling, not just the one-line output — the Against points, Dissent, and "what would flip it" are the committee's starting risk register).
2. A decision the user states in the boardroom message.
3. Neither → one line: "The boardroom executes decisions; it doesn't make them. What was decided, or run it through the debate council first?" Stop.

If a material execution constraint is missing (budget ceiling, deadline, headcount, jurisdiction), ask 1–3 precise questions before convening. Do not guess.

**Scope boundary.** Medical, legal, or high-stakes financial decisions carry the label "structured analysis, not professional advice" on the output line. The session still runs.

## Step 1 — Convene the hierarchy

Roles and what each is accountable for are in `references/roles-and-frameworks.md`. Read it before the session. In brief:

- **CEO (chair)** — owns the go/no-go call inside the committee; weighs the officers; assigns the first-move owner.
- **CFO** — cost, cash, payback, ROI, budget fit. Speaks in numbers or not at all.
- **CTO** — technical feasibility, build/buy/partner, capability gaps, time-to-working.
- **COO** — capacity, sequencing, dependencies, realistic timeline, process load.
- **CRO / General Counsel** — legal, regulatory, contractual, reputational, and downside-tail risk.
- **CHRO** — people: skills, hiring, change fatigue, incentives, who actually does the work.
- **VP owners** — one named functional owner per workstream the decision creates; they supply ground-truth effort and constraints.
- **Advisory bench (3 professors)** — strategy, finance/economics, organisational behaviour. They do not vote. They test each officer's argument against an established framework and cite it by name (see the reference file). A framework must be real and correctly applied; a misattributed or invented one is struck.

## Step 2 — Gather facts

Each officer argues with facts and figures from their function. Where the decision turns on external numbers — market rates, vendor pricing, regulatory deadlines, salary bands, tool costs — search first and cite what was found. Internal numbers come from what the user has said; if the user hasn't supplied one, the officer states an estimate **labelled as an estimate with its basis**, never as a fact. A fabricated figure strikes the officer's argument, same as in the council.

## Step 3 — Pre-mortem (Klein, 2007)

The CEO opens with: "It is [horizon] from now and this decision has failed in execution. Why?" Each officer answers from their seat in 2–4 lines with a number attached. Then each officer answers the opposite: "It succeeded — what made the difference?" The advisory bench then maps every failure cause to a framework and says whether the framework predicts it is fixable or structural.

## Step 4 — Officers' positions

Each officer states one of:
- **GO** — executable within known constraints.
- **GO-IF** — executable if a named, checkable condition holds (budget approved, hire made, vendor contract signed).
- **NO-GO** — not executable as decided; state the single blocking fact and its number.

Officers are not required to agree with each other, and the CEO is not required to follow the majority. Weight goes to the officer whose objection is best evidenced, not the loudest seat.

## Step 5 — Chair's call

The CEO rules GO, GO-IF, or NO-GO, names the decisive officer and fact, and assigns the first move: **one owner, one action, one deadline**. The first move is the smallest step that either starts execution or retires the biggest uncertainty — not a kickoff meeting.

## Output — default (`boardroom`)

Run Steps 0–5 in full internally. Output 1–2 lines, 25–45 words, nothing else:

```
GO: Boardroom: GO — [decisive reason with its number]. First move: [owner] [action] by [deadline].
GO-IF: Boardroom: GO if [condition, checkable]. First move: [owner] [action to verify the condition] by [deadline].
NO-GO: Boardroom: NO-GO — [blocking fact with its number, and which officer raised it]. Your call: override and execute, send back to the council with this evidence, or drop it.
```

On NO-GO the committee **stops**. It does not execute, does not soften into a GO-IF to avoid the confrontation, and does not send anything to the council itself — that is the user's decision. If the user says override, run Step 5 again under the override and output the GO line with the first move and one risk flag. If the user says send it back, they invoke the council themselves; the committee hands over its NO-GO evidence as the Against bench's opening material.

If the objection is on the merits rather than executability, the NO-GO line says so: "...raised by [officer] — this is a merits objection, not an execution one; council territory."

## Output — full minutes (`boardroom full`)

```
**Decision under execution:** [one line] — source: council verdict / user-stated
**Scope:** [only if the boundary applies]
**Constraints given:** [budget, deadline, headcount, other — or "none supplied"]

**Pre-mortem**
- CFO: [failure cause + number] / [success factor]
- CTO: ...
- COO: ...
- CRO/GC: ...
- CHRO: ...
- VP [function]: ...

**Advisory bench**
- Strategy: [framework] → [what it predicts about this decision]
- Finance: [framework] → ...
- Org behaviour: [framework] → ...

**Positions:** CFO [GO/GO-IF/NO-GO] · CTO [...] · COO [...] · CRO [...] · CHRO [...]

**Chair's call:** [GO / GO-IF / NO-GO] — decisive officer and fact
**First move:** owner · action · deadline

**Execution plan** (GO and GO-IF only)
| Workstream | Owner | Days 1–30 | Days 31–60 | Days 61–90 | KPI | Budget |
|---|---|---|---|---|---|---|

**Risk register:** top 3, each with likelihood, impact, owner, trigger
**Kill criteria:** the measurable condition under which execution stops and returns to the council
```

## Style

Same as the Debate Council: direct, numbers over adjectives, no preamble, no closing pleasantries. Officers speak from their function, not in generalities — "CFO: payback 14 months at $3.2k/mo, over our 12-month ceiling" not "CFO has cost concerns." A follow-up without the word "boardroom" is answered normally; the committee has adjourned.

## Example

The council earlier ruled: "Verdict: For — accept the 12-month contract PM role; W-2 with interviewing permitted, and paid work beats unpaid search. Confidence Medium."

User: "boardroom"

Internally: CFO checks the rate against market and the user's stated burn; CTO has no seat at the table here beyond tooling, says GO; COO flags that a 40-hour contract plus active interviewing is a 55-hour week and asks for a cap; CRO/GC reads the non-compete and the notice clause; CHRO flags that contract roles convert to full-time at a rate worth knowing and searches for it. Advisory bench: strategy prof cites real-options reasoning (the contract preserves the option to keep searching); OB prof cites Kotter on short-term wins for motivation during a long search.

Output:
"Boardroom: GO if the contract's notice period is ≤ 2 weeks and there's no non-compete. First move: you — request the full agreement and confirm both clauses within 48 hours."
