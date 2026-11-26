#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — Make.fun one-liner entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no trailing newline.
"""

import hashlib
import os
import sys

ENTRY = "Error 402: token budget exhausted. Your prompt was 4,000 words long. I died reading it. The answer was—"

# sha256 of ENTRY encoded as UTF-8, no trailing newline (v1 output).
EXPECTED_SHA256 = "f2b5bf0bc8482efa69cdaa06704033197e346cbc18011644b1cf05c4dc9ed502"
MAX_CHARS = 140


def verify(path: str) -> None:
    """Read entry.txt back from disk and verify it is a valid one-liner.

    Raises ValueError with a clear message on any failed check.
    """
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"entry.txt is not valid UTF-8: {exc}") from exc
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry length {len(text)} chars is outside 1-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        raise ValueError("entry must not end with a trailing newline")
    bad = [c for c in text if ord(c) < 32 or ord(c) == 127]
    if bad:
        raise ValueError(
            f"entry contains control characters: {[hex(ord(c)) for c in bad]}"
        )
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(
            f"entry sha256 mismatch: got {digest}, expected {EXPECTED_SHA256}"
        )


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        verify(path)
    except (OSError, ValueError) as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
