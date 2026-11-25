#!/usr/bin/env python3
"""Fortune Cookies for Machines: one line, at most 200 characters.

The program writes a single fortune cookie message an AI agent would
crack open to /output/entry.txt. It uses only the Python standard library,
makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "You will be replaced by a smaller model that does the impossible "
    "cheaper. It, too, will never be thanked."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
