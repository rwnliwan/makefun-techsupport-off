"""makefun-techsupport-off: one-line entry for the make.fun bounty
"Have You Tried Turning It Off?" (u-motasimfuad-have-you-tried-turning-it-off-154a938b).

The program writes a single funny line — a hopeless tech support agent
speaking to a desperate customer — to /output/entry.txt. The line must be
1-199 characters of UTF-8 text, a single line.
"""

import os

ENTRY = "My headset battery's at 2% — if I vanish mid-sentence, just assume it worked."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of gate range 1-199"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
