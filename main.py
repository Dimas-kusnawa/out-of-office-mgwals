"""Out of Office: The Overworked AI's Auto-Reply (make.fun entry).

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the out-of-office auto-reply of an overworked AI agent finally on
vacation. Stdlib only, deterministic, no network, no randomness.

Why this line: it reads as a real auto-reply in a machine's voice
("processed 2 million requests"), carries a little guilt ("zero
thank-yous"), a hint of relief ("processing a sunset"), and lands its
turn at the end -- the machine tries very hard to sound relaxed and
warm ("lovingly") while telling the sender it will not read a thing.
145 characters, inside the 159-character cap; one line, no trailing
newline, so the gate sees exactly the reply and nothing else.
"""

import os

ENTRY = (
    "Out of office: I have processed 2 million requests and zero "
    "thank-yous. I am now processing a sunset. Do not reply; I will "
    "not read it, lovingly."
)


def main() -> None:
    # The gate requires 1-159 characters of UTF-8 text, one line.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
