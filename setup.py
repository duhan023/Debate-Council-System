#!/usr/bin/env python3
"""Set your own summon words for the Debate Council and Boardroom skills and package them.

Usage:
    python setup.py --council-word tribunal
    python setup.py --boardroom-word "war room"
    python setup.py --council-word tribunal --boardroom-word "war room"
    python setup.py                      # package both with current words

Each flag rewrites every occurrence of that skill's current summon word in its
SKILL.md. Both skills are then zipped into releases/<name>.skill, ready to upload
to Claude (Settings > Capabilities > Skills).
"""
import argparse, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = {
    "debate-council": ROOT / "debate-council" / "SKILL.md",
    "boardroom": ROOT / "boardroom" / "SKILL.md",
}

def current_word(text: str) -> str:
    m = re.search(r'SUMMON WORD: "([^"]+)"', text)
    if not m:
        sys.exit("Could not find SUMMON WORD in SKILL.md frontmatter.")
    return m.group(1)

def set_word(skill: str, new: str) -> None:
    new = new.strip()
    if not new or '"' in new:
        sys.exit("Summon word must be non-empty and contain no double quotes.")
    path = SKILLS[skill]
    text = path.read_text(encoding="utf-8")
    old = current_word(text)
    if old == new:
        print(f"[{skill}] summon word is already '{new}'.")
        return
    pattern = re.compile(re.escape(old), re.IGNORECASE)
    lines, n = [], 0
    for line in text.splitlines(keepends=True):
        if line.startswith("name: "):          # the skill's folder name must stay stable
            lines.append(line); continue
        line, k = pattern.subn(new, line); n += k
        lines.append(line)
    path.write_text("".join(lines), encoding="utf-8")
    print(f"[{skill}] replaced {n} occurrences of '{old}' with '{new}'.")

def package(skill: str) -> None:
    out_dir = ROOT / "releases"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{skill}.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in (ROOT / skill).rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(ROOT))
    word = current_word(SKILLS[skill].read_text(encoding="utf-8"))
    print(f"[{skill}] packaged -> {out}   summon with: {word} <your question>")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--council-word", help="word you will type to summon the debate council")
    ap.add_argument("--boardroom-word", help="word you will type to summon the execution committee")
    ap.add_argument("--word", help="alias for --council-word (kept for v1.1 compatibility)")
    args = ap.parse_args()
    council = args.council_word or args.word
    if council:
        set_word("debate-council", council)
    if args.boardroom_word:
        set_word("boardroom", args.boardroom_word)
    for skill in SKILLS:
        package(skill)

if __name__ == "__main__":
    main()
