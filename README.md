# Debate Council — an adversarial debate council for Claude

**Version 1.1.0**

A custom [Claude Skill](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) that stress-tests a question or decision by arguing it against itself before answering.

When you summon it, Claude convenes ten debaters — five for the motion, five against, each assigned a different angle (financial, risk, execution, long-term, values, base rates, opportunity cost, second-order effects) — runs a parliamentary-style debate with constructives, rebuttals and closings, then a neutral judge scores every surviving argument against a published rubric and issues a ruling.

The judge is not allowed to flatter you. It records its initial lean before hearing arguments, must name the strongest surviving objection to its own verdict, and may rule *For*, *Against*, *Conditional*, or *Insufficient evidence*.

## You choose the summon word

The council answers only to a word you pick. There is no imposed name — call it what you like in your own language: a name, a place, a word that means "tribunal" where you come from. The default is `debate council`; change it in one step (below). Until you do, the skill reminds you once per conversation that you can.

## Invocation

The skill fires only when your message contains your summon word. Ordinary questions, "pros and cons", and debate-adjacent language do nothing.

| You write | Claude runs |
|---|---|
| `<word> <question>` | Full debate internally; condensed ruling (top 3 per side, rebuttals that landed, verdict) |
| `<word> full <question>` | Complete transcript: all ten constructives, cross-rebuttals, closings, scorecard, ruling |
| `<word> gameplan <problem>` | Gameplan mode: the top 3 research-backed fixes, each citing a real, verified source with an evidence tier |

`gameplan` works standalone on any problem, or immediately after a ruling — in which case it targets the points the ruling exposed.

## What a ruling contains

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

## Install

Requires a Claude Pro, Max, Team or Enterprise plan with code execution enabled. Free plans can't install custom skills.

**Option A — pick your word, then install (recommended)**

```bash
git clone https://github.com/duhan023/Debate-Council-System.git
cd Debate-Council-System
python setup.py --word "your word here"
```

This rewrites the skill with your summon word and produces `releases/debate-council.skill` on your machine. In Claude, open **Settings → Capabilities**, turn on **Skills**, and upload that file.

No Python? Open `debate-council/SKILL.md` in any text editor, find-and-replace `debate council` with your word (replace all), zip the `debate-council` folder, rename the zip to `debate-council.skill`, and upload.

**Option B — install as-is, no terminal**

Click the green **Code** button → **Download ZIP**, unzip it, then zip *only* the `debate-council` folder and rename that zip to `debate-council.skill`. Upload it in Claude. Summon with `debate council`. You can rename later with Option A and re-upload.

**Claude Code** — copy the `debate-council/` folder into `~/.claude/skills/` (personal) or `.claude/skills/` inside a project. Run `setup.py` first if you want your own word.

## Repository layout

```
debate-council/
├── SKILL.md              # the skill: summon word, modes, steps, output formats, judge's standard
└── references/
    └── rubric.md         # scoring rubric the judge applies before ruling
setup.py                  # set your summon word and package into releases/debate-council.skill
```

## Contributing

Issues and pull requests are welcome. Keep `SKILL.md` under 500 lines; put anything longer in `references/`. Changes to the rubric should come with a short note on why the weighting moved.

## License

MIT — see [LICENSE](LICENSE).
