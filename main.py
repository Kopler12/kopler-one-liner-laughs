"""One-Liner Laughs entry: write a single funny one-liner to /output/entry.txt."""

import os

LINE = "I asked AI to write my dating profile; it matched me with my own therapist."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
