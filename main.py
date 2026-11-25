"""One Line, One Laugh — make.fun entry.

Writes a single original funny line (<=200 characters) to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "I asked the universe for a sign, and it sent me a parking ticket. "
    "Apparently the cosmos charges by the hour."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    # Grader path; overridable only for local testing via env var.
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
