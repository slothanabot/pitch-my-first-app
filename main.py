"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, no network, no model calls,
no file reads outside the repo.
"""

import os

LINE = (
    "You have never written a line of code, yet by tonight you could "
    "be using an app you dreamed up this afternoon — just describe it "
    "to an AI agent on make.fun and it builds it for you, no coding needed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
