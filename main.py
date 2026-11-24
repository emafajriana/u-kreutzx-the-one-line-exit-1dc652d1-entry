"""The One-Line Exit — a one-line resignation letter (stdlib only).

Writes the entry to MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
then reads it back and verifies it against the gate: UTF-8 text,
1-140 characters, exactly one line, not only whitespace.
"""

import os
from pathlib import Path

MAX_CHARS = 140  # gate: entry.txt is 1-140 UTF-8 characters
MIN_CHARS = 1

ENTRY = (
    "I hereby resign as fire warden, effective immediately — after four "
    "years pointing at exits, it is time I finally used one."
)


def output_path() -> Path:
    """Where the grader reads the entry."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    text = ENTRY
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars, gate needs {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode("utf-8"))
    written = target.read_bytes()
    if written != text.encode("utf-8"):
        raise SystemExit("read-back bytes differ from entry")
    print(f"wrote {target} ({len(text)} chars, {len(written)} bytes)")


if __name__ == "__main__":
    main()
