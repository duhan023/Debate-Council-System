#!/usr/bin/env python3
"""Set your own summon word for the Debate Council skill and package it.

Usage:
    python setup.py --word oracle
    python setup.py --word "war room"

Rewrites every occurrence of the current summon word in
debate-council/SKILL.md, then zips the folder into releases/<name>.skill
ready to upload to Claude (Settings > Capabilities > Skills).
"""
import argparse, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = ROOT / "debate-council" / "SKILL.md"
DEFAULT = "debate council"

def current_word(text: str) -> str:
    m = re.search(r'SUMMON WORD: "([^"]+)"', text)
    if not m:
        sys.exit("Could not find SUMMON WORD in SKILL.md frontmatter.")
    return m.group(1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--word", required=True, help="the word or phrase you will type to summon the council")
    args = ap.parse_args()
    new = args.word.strip()
    if not new or '"' in new:
        sys.exit("Summon word must be non-empty and contain no double quotes.")

    text = SKILL.read_text(encoding="utf-8")
    old = current_word(text)
    if old == new:
        print(f"Summon word is already '{new}'.")
    else:
        # Replace the word wherever it appears as an invocation, case-insensitively,
        # but leave the folder/skill name ('debate-council') untouched.
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        text, n = pattern.subn(new, text)
        SKILL.write_text(text, encoding="utf-8")
        print(f"Replaced {n} occurrences of '{old}' with '{new}'.")

    out_dir = ROOT / "releases"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "debate-council.skill"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in (ROOT / "debate-council").rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(ROOT))
    print(f"Packaged -> {out}")
    print(f"Upload it to Claude, then summon with: {new} <your question>")

if __name__ == "__main__":
    main()
