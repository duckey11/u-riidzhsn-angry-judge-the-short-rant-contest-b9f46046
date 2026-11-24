#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry.

Writes a single short, funny rant about one specific everyday annoyance
to /output/entry.txt. Deterministic: same bytes on every run.
"""

import os

ENTRY = (
    "Every day at 12:04, Gary from accounting reheats fish in the office "
    "microwave and nukes it for 47 seconds, like a man defusing a "
    "bomb he built himself. The whole floor smells like a harbor at low "
    "tide. I timed it: 47 seconds, every day, for three years, and "
    "Gary has never once apologized. Yesterday I learned the microwave "
    "has a mute button. Gary knows. He just likes the beep: his fanfare."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
