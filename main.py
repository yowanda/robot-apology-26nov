#!/usr/bin/env python3
"""The Robot Apology - make.fun entry (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset). Deterministic, stdlib-only, no network.
"""

import os

ENTRY = (
    "I am sorry I sent your birthday card to your dentist, because his address sat right next to yours in my contacts.\n"
    "I have learned that neighbours in a list are not neighbours in life, so from now on I will read the name above the address before I send anything.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    # Runtime validation: read the file back and confirm it is exactly
    # two lines totalling 1-400 characters; rewrite only if valid, so the
    # output bytes never change.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        text = f.read()
    lines = text.split("\n")
    assert text.endswith("\n") and len(lines) == 3 and lines[2] == "", "entry must be exactly 2 lines"
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
