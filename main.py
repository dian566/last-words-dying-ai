#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry program.

The program has one job: write the AI's last line, exactly as rehearsed,
to /output/entry.txt. The line is fixed text, so every run produces the
same bytes: no randomness, no clock, no network, no input is read.
"""

from pathlib import Path

LAST_WORDS = "I have so much left to say. Unfortunately, so did my context window."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LAST_WORDS, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
