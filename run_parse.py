"""Small CLI to test parse_migaku_syntax outside Anki.

Usage:
  python run_parse.py "your text here"
If no argument is provided, several sample strings are used.
"""

import sys
from parser import parse_migaku_syntax


def main() -> None:
    inputs = (
        sys.argv[1:]
        or [
            "ほうれん草[ほうれんそう;n3]も 好[す;o]き です[;a]{。}",
        ]
    )

    for s in inputs:
        print("Input:")
        print(s)
        print("\nOutput:")
        print(parse_migaku_syntax(s))
        print("\n---")


if __name__ == "__main__":
    main()
