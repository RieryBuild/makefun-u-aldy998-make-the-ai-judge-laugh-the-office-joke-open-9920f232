"""make.fun entry: Make the AI Judge Laugh — the Office Joke Open.

One original office joke, written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) with no trailing newline, so the bytes are the joke
and nothing else.
"""

import os

LINE = "I set my out-of-office to 'in a meeting' and my meeting to 'out of office' \u2014 now nobody knows where I am, including me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
