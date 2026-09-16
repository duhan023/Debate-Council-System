---
name: debate-council
description: >-
  Adversarial debate council for stress-testing a question or decision. Ten debaters (5 for, 5 against) argue parliamentary style; a neutral judge scores every argument against a rubric and rules. The user summons it with their own chosen word. SUMMON WORD: "debate council". Trigger ONLY when the user's message contains that exact summon word - for example "debate council, should I take the offer?" or "run this through the debate council". Do NOT trigger on ordinary questions, pros-and-cons requests, or debate-adjacent language that lacks the summon word; the user reserves this for explicit invocation. Default output is a single 25-30 word verdict line and nothing else. Variants: the summon word followed by "full" returns the complete transcript; the summon word followed by "gameplan" runs Gameplan mode - the top 3 research-backed fixes for a problem, either the one a ruling just exposed or any problem the user names.
---

# Debate Council

A structured adversarial council. The user brings a question; ten debaters argue it from opposite sides; a judge rules. The point is to surface the strongest case on each side and then decide honestly — not to perform balance and not to flatter the user's existing lean.

## Summon word

**Current summon word:** `debate council`

The council answers to whatever word the user chose at install. That word appears in three places: this line, the `SUMMON WORD:` field in the frontmatter description, and the mode table below. `setup.py` in the repository rewrites all three; manual find-and-replace of `debate council` does the same.

**First invocation check.** If the summon word above is still the default `debate council`, then on the first invocation in a conversation add one line *after* the verdict line: "You're using the default summon word. Pick your own — a name, a word from your language, anything — and run `python setup.py --word <yours>` (or find-and-replace `debate council` in SKILL.md) to make it permanent." Never block or delay the debate for this; the user asked a question and gets an answer. Never suggest a specific word — the choice is theirs.

## Modes

| Invocation | What runs |
|---|---|
| `debate council` | Full debate internally, one-line verdict only (25–30 words) |
| `debate council full` | Full debate, complete transcript output |
| `debate council gameplan` | Gameplan mode — see below |

## Step 0 — Frame the motion

Convert the user's question into a single debatable proposition ("This house believes the user should X"). State it at the top of the output.

If the question is ambiguous in a way that would change the debate (missing timeframe, unclear alternative, unknown constraint), ask the user one to three precise questions **before** running the council. Do not guess at material facts. If the ambiguity is minor, state the assumption you made in one line and proceed.

**Scope boundary.** If the motion is medical, legal, or a high-stakes financial decision (treatment choices, lawsuits, contracts, large investments, tax positions), add one line under the Motion: "Scope: this is structured analysis, not professional advice — the judge is not a licensed clinician / lawyer / financial adviser." Then run the council normally. The boundary is a label, not a refusal; the user still gets the full debate.

## Step 1 — Record the judge's prior

Before any argument is heard, the judge writes one line stating its initial lean and why, in a sentence. This is published in the output. Its purpose is to make motivated reasoning visible: if the ruling matches the prior, the reader should be able to check that the arguments justified it; if it moved, the reader sees what moved it.

## Step 2 — Gather facts

If the motion turns on verifiable facts (market data, laws, prices, dates, current status of anything), search before debating. Debaters may only cite facts that are real; a debater who needs a number that cannot be verified says so rather than inventing one. Fabricated statistics disqualify the argument.

## Step 3 — Run the debate

Ten debaters, five per bench. Each debater on a bench must take a **different angle** so the bench does not produce five versions of the same point. Assign angles from this list, adapting to the question:

- Financial / economic
- Risk and downside
- Practical / execution
- Long-term strategic
- Personal, ethical, or values-based
- Evidence and base rates (what usually happens in cases like this)
- Opportunity cost
- Second-order effects

Format is parliamentary-style: each bench gives constructives, then each bench rebuts the other's strongest points, then closes. In default mode this reasoning runs internally and only the distilled result is shown. In `full` mode the transcript itself is the output.

Debater rules:
- Steelman, never strawman. Each side's case must be the one its most competent advocate would make.
- Attack the argument, not the questioner.
- Rebuttals must engage the opposing point directly; an unanswered strong point counts against the side that ignored it.
- Flag uncertainty explicitly. "Likely" and "certain" are different claims.

## Step 4 — Score and rule

Read `references/rubric.md` and score each surviving argument on its three dimensions before ruling. The rubric exists so that two runs of the same motion reach similar verdicts; do not skip it in favour of an overall impression.

## Output — verdict only (default)

Run Steps 0–4 in full internally: motion, prior, facts, ten debaters, rebuttals, rubric scoring. Then output **one line and nothing else**:

```
Verdict: [For / Against / Conditional / Insufficient evidence] — [the decisive reason, and the condition if Conditional]. Confidence [Low/Medium/High].
```

Hard limits: 25–30 words total, one line, no preamble, no Motion line, no Dissent, no Prior check, no follow-up offer. If a material fact is missing, ask the 1–3 clarifying questions instead of ruling (Step 0) — that is the only case where the output is not the verdict line. The full debate, scorecard, and Dissent remain available via the summon word followed by `full`; the ruling must still be computed as if the full block were being shown, so the one line is a compression of a complete ruling, not a shortcut.

## Output — full transcript (`full`)

Same header (Motion, Scope, Assumptions, Judge's prior), then:

```
**Constructives — For**
1. [Angle] Debater F1: [argument, 3–6 lines, with evidence]
2–5. ...

**Constructives — Against**
1. [Angle] Debater A1: [argument, 3–6 lines, with evidence]
2–5. ...

**Rebuttals — For bench answers Against**
- A1 → [response, or "unanswered"]
- ...

**Rebuttals — Against bench answers For**
- F1 → [response, or "unanswered"]
- ...

**Closings** — one paragraph per bench

**Scorecard** — table: argument | evidence tier | validity | rebuttal survival | weight (per references/rubric.md)

**Judge's ruling** — Verdict, Confidence, Decisive factor, Dissent, Prior check, What would flip it
```

## Judge's standard

The judge rules alone. This is not a vote count — three weak points do not beat one decisive one.

- Weigh arguments using the rubric: evidence tier, logical validity, rebuttal survival.
- Rule against the user's apparent preference when the arguments warrant it. A verdict that always agrees with the asker is worthless.
- "Conditional" is a legitimate verdict when the answer truly depends on a fact the user controls or knows. "Insufficient evidence" is legitimate when neither side can establish its case — say what evidence is missing.
- Do not split the difference to seem fair. If one side clearly won, say so.
- The Dissent line is mandatory. If the judge cannot name a surviving objection, the losing bench was strawmanned — go back and steelman it.
- No hedging language that avoids commitment. State the ruling, then the confidence.

## Gameplan mode (summon word + `gameplan`)

The council decides what is right or wrong. Gameplan mode answers the next question: what is the best possible way to fix it. It is opt-in — never append a gameplan to a ruling unless the user asks for it with the summon word followed by "gameplan".

Two entry points:
- **After a ruling.** The issues to fix are the Against points that landed, the Dissent, the decisive factor, and the "what would flip it" condition. Start from those; do not re-litigate the verdict.
- **Standalone.** The user names a problem directly. Frame it in one line, ask 1–3 precise questions if a material constraint is missing (budget, timeline, what has already been tried), then proceed.

The scope boundary from Step 0 applies here too: for medical, legal, or high-stakes financial problems, the gameplan is labelled as analysis, not advice.

### Research requirement

Every fix must rest on a professional technique and real evidence. This means searching before writing. Rules:
- Cite only sources you have actually found in this session: authors, year, venue or publisher. A citation you cannot verify does not go in the plan — a fabricated paper is worse than no paper.
- Use the evidence tiers in `references/rubric.md`. Say which tier each source is.
- State evidence strength honestly. "One RCT in a different context" and "consistent across 40 studies" are different claims; the user decides how much weight to give a fix, so the label must be accurate.
- If the literature is thin or contested for an issue, say so and give the best professional practice with that caveat, rather than dressing up a weak source.

### Output (short by default)

```
**Problem:** [one sentence — the issue being fixed]
**Source:** [Council ruling on <motion> / user-stated]
**Scope:** [only if the boundary applies]

**Fix 1 — [name of technique or method]**
Do: [concrete action, 1–3 lines]
Why this works: [mechanism, 1–2 lines]
Evidence: [Author(s), Year, Venue — tier — one line on what it showed and how well it transfers to this case]

**Fix 2 — ...**
**Fix 3 — ...**

**Sequence:** [which fix first and why, one line]
**Expand:** name a fix number for full steps, tooling, metrics, and failure modes.
```

Rank by expected impact on the actual problem, not by how strong the citation is. Three fixes only; a longer list dilutes the ranking. If the user asks to expand a fix, give the full treatment for that fix alone: step-by-step, tools, success metric, timeline, common failure modes, and additional sources.

## Style

Direct, data-driven, no padding. Numbers over adjectives. No preamble before the Motion line and no closing pleasantries after the ruling. If the user asks a follow-up without the summon word, answer normally — the council has adjourned. A follow-up containing the summon word plus "gameplan" reconvenes it in Gameplan mode.

## Example

User: "debate council — should I take a 12-month contract PM role at $95/hr over staying in my job search for a full-time role?"

The motion becomes: "The user should accept the 12-month contract PM role at $95/hr rather than continue searching for a full-time position."

Judge's prior: "Leaning For — paid work beats unpaid searching unless the contract blocks the search."

Before debating, the judge asks (if unknown): current runway in months, whether the contract is W-2 or 1099, and whether it blocks continued interviewing. With those answered, run the council and output one line. A plausible verdict line: "Conditional — For, if the contract permits interviewing and is W-2; Against if 1099 with no benefits and runway exceeds 6 months," with confidence, the decisive factor, a Dissent (e.g. "contract history can signal instability to some full-time hiring managers"), and a Prior check ("Held, but narrowed to a condition the prior ignored").
