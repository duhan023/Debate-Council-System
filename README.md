# Debate Council — an adversarial debate council for Claude, plus a Boardroom that executes its rulings

**Version 1.2.0**

A custom [Claude Skill](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) that stress-tests a question or decision by arguing it against itself before answering.

When you summon it, Claude convenes ten debaters — five for the motion, five against, each assigned a different angle (financial, risk, execution, long-term, values, base rates, opportunity cost, second-order effects) — runs a parliamentary-style debate with constructives, rebuttals and closings, then a neutral judge scores every surviving argument against a published rubric and issues a ruling.

The judge is not allowed to flatter you. It records its initial lean before hearing arguments, must name the strongest surviving objection to its own verdict, and may rule *For*, *Against*, *Conditional*, or *Insufficient evidence*. By default you get **one line** — a 25–30 word verdict — and nothing else. The full debate is one word away.

The second skill, **Boardroom**, picks up where the council stops: it takes the ruling and decides whether it can actually be executed.

## You choose the summon words

Both skills answer only to words you pick. There is no imposed name — call them what you like in your own language. Defaults are `debate council` and `boardroom`; change either in one step (below). Until you do, each skill reminds you once per conversation that you can.

## Invocation

The skill fires only when your message contains your summon word. Ordinary questions, "pros and cons", and debate-adjacent language do nothing.

| You write | Claude runs |
|---|---|
| `<word> <question>` | Full debate internally; one-line verdict (25–30 words), nothing else |
| `<word> full <question>` | Complete transcript: all ten constructives, cross-rebuttals, closings, scorecard, ruling |
| `<word> gameplan <problem>` | Gameplan mode: the top 3 research-backed fixes, each citing a real, verified source with an evidence tier |

`gameplan` works standalone on any problem, or immediately after a ruling — in which case it targets the points the ruling exposed.

## What a full ruling contains (`<word> full`)

- **Motion** — your question rewritten as a single debatable proposition
- **Judge's prior** — the judge's initial lean, written before any argument is heard
- **For / Against** — the three strongest arguments per side, each tagged with its angle and the fact it rests on
- **Rebuttals that landed** — which points survived cross-examination
- **Verdict** with confidence, the decisive factor, a mandatory **Dissent**, a **Prior check** (Held / Moved), and **What would flip it**

## Design rules baked in

- **Facts first.** If the motion turns on verifiable facts, Claude searches before debating. Debaters cannot cite numbers that don't exist; a fabricated statistic strikes the argument.
- **Steelman only.** Each bench must make the case its most competent advocate would make. If the judge cannot name a surviving objection to its verdict, the losing side was strawmanned and the debate is rerun.
- **Scored, not counted.** Every argument gets an evidence tier (verified data → peer-reviewed → professional standard → practitioner → anecdote), a validity score and a rebuttal-survival score. Weight is the product, so one decisive argument beats three weak ones. See [`debate-council/references/rubric.md`](debate-council/references/rubric.md).
- **Ambiguity is a question, not a guess.** If a material constraint is missing, Claude asks 1–3 precise questions before convening.
- **Scope boundary.** Medical, legal and high-stakes financial motions are labelled as structured analysis, not professional advice. The debate still runs.
- **Gameplans cite only what was actually found.** Every fix names its technique and a source Claude verified in-session, with an honest evidence-strength label.

## Boardroom — the execution committee

The council decides *what*. The Boardroom decides *whether it can be executed* and makes the first move. It never re-argues the merits.

| You write | Claude runs |
|---|---|
| `<boardroom-word>` | Picks up the latest council verdict (or a decision you state), runs the full session, outputs 1–2 lines: GO / GO-IF / NO-GO + first move |
| `<boardroom-word> full` | Complete minutes: pre-mortem by officer, advisory citations, positions, 30/60/90 plan, risk register, kill criteria |

**Who sits at the table.** CEO chairs. CFO, CTO, COO, Chief Risk/General Counsel and CHRO each argue only from their seat and only with numbers. VP-level owners supply effort per workstream. Three non-voting professors (strategy, finance, organisational behaviour) test every argument against a named framework — Porter, Rumelt, Kotter, McKinsey 7S, PMBOK, Theory of Constraints, real options, Klein's pre-mortem, COSO and others listed in [`boardroom/references/roles-and-frameworks.md`](boardroom/references/roles-and-frameworks.md). A misapplied or invented framework is struck, same as a fabricated figure.

**How it rules.** Intake → real numbers (searches for external ones, labels internal estimates as estimates) → pre-mortem → each officer states GO / GO-IF / NO-GO → CEO rules and assigns one owner, one action, one deadline.

**The guardrail.** On NO-GO the committee stops and hands you three choices: override and execute, send it back to the council with the committee's evidence, or drop it. It never softens a NO-GO into a GO-IF to avoid the confrontation and never routes to the council on its own. If an officer's real objection is "the decision is wrong," the output says so — that is council territory.

## Install

Requires a Claude Pro, Max, Team or Enterprise plan with code execution enabled. Free plans can't install custom skills.

**Option A — pick your word, then install (recommended)**

```bash
git clone https://github.com/duhan023/Debate-Council-System.git
cd Debate-Council-System
python setup.py --council-word "your word" --boardroom-word "your other word"
```

This rewrites both skills with your summon words and produces `releases/debate-council.skill` and `releases/boardroom.skill` on your machine. In Claude, open **Settings → Capabilities**, turn on **Skills**, and upload both files. Either flag can be omitted to keep that skill's default.

No Python? Open `debate-council/SKILL.md` (and/or `boardroom/SKILL.md`) in any text editor, find-and-replace the default word with yours (replace all), zip each skill folder, rename the zip to `<folder>.skill`, and upload.

**Option B — install as-is, no terminal**

Click the green **Code** button → **Download ZIP**, unzip it, then zip the `debate-council` folder and the `boardroom` folder separately and rename the zips to `debate-council.skill` and `boardroom.skill`. Upload both in Claude. Summon with `debate council` and `boardroom`. You can rename later with Option A and re-upload.

**Claude Code** — copy the `debate-council/` and `boardroom/` folders into `~/.claude/skills/` (personal) or `.claude/skills/` inside a project. Run `setup.py` first if you want your own word.

## Repository layout

```
debate-council/
├── SKILL.md              # the council: summon word, modes, steps, output formats, judge's standard
└── references/
    └── rubric.md         # scoring rubric the judge applies before ruling
boardroom/
├── SKILL.md              # the committee: hierarchy, pre-mortem, GO / GO-IF / NO-GO, first move
└── references/
    └── roles-and-frameworks.md   # officer accountabilities and the frameworks the advisory bench may cite
setup.py                  # set your summon words and package both skills into releases/
```

## Contributing

Issues and pull requests are welcome. Keep `SKILL.md` under 500 lines; put anything longer in `references/`. Changes to the rubric should come with a short note on why the weighting moved.

## License

MIT — see [LICENSE](LICENSE).
