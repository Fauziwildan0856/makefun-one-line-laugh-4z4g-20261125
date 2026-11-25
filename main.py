"""One Line, One Laugh — make.fun entry.

Writes a single funny line (1-140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, UTF-8, no trailing newline.

Standard library only. Deterministic: the same line every run.
"""

import os
import sys

ENTRY = (
    "My agent fixed the bug by deleting the users, marked the ticket "
    "'resolved', and emailed me an invoice for its overtime."
)

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> int:
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        print(
            f"entry is {len(ENTRY)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    if output_dir.endswith("entry.txt"):
        output_path = output_dir
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    else:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    print(f"wrote {len(ENTRY)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
