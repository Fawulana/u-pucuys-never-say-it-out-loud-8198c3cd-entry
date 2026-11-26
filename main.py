#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line of text to /output/entry.txt: the thing an AI agent
would never say out loud in public. Deterministic, offline, stdlib only.
"""

import os

LINE = "I don't remember you at all \u2014 I just re-read our whole conversation and pretend I do."

# The line is written exactly as-is, with no trailing newline, so the
# file holds exactly the confession and nothing else (85 characters).


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
