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


if __name__ == "__main__":
    main()
