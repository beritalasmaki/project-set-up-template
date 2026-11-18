#!/usr/bin/env python3
"""Flag raw colour values and off-scale pixel values in code.

Optional. Copy into a project that has code and a design-tokens file. Not run
in this template's own checks, because the template has no UI code.

Checks each given file for:
  - raw hex colours (#fff, #ffffff, #ffffffff) and rgb()/hsl() colours
  - pixel values for spacing properties that are not on the spacing scale

Usage:
  lint-tokens.py FILE [FILE ...] [--tokens design-system/tokens.json]

Files named tokens.* and the tokens file itself are skipped, because raw values
belong there. Exit code 0 when clean, 1 when violations are found, 2 on bad input.
Hook use: run it from a PostToolUse hook on Edit|Write with the changed file path.
"""
import json
import re
import sys
from pathlib import Path

HEX = re.compile(r"#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b")
FUNC = re.compile(r"\b(?:rgb|rgba|hsl|hsla)\(")
SPACING = re.compile(
    r"\b(?:margin|padding|gap|row-gap|column-gap|top|right|bottom|left|inset)"
    r"(?:-[a-z]+)?\s*:\s*([^;}{]+)"
)
PX = re.compile(r"(-?\d+(?:\.\d+)?)px")


def scale(tokens_path):
    try:
        data = json.loads(Path(tokens_path).read_text(encoding="utf-8"))
        return {float(v.replace("px", "")) for v in data["spacing"].values()} | {0.0}
    except (OSError, KeyError, ValueError, json.JSONDecodeError):
        return None


def main(argv):
    tokens_path = "design-system/tokens.json"
    files, args = [], list(argv)
    while args:
        a = args.pop(0)
        if a == "--tokens":
            tokens_path = args.pop(0) if args else tokens_path
        else:
            files.append(Path(a))
    if not files:
        print(__doc__)
        return 2
    allowed = scale(tokens_path)
    if allowed is None:
        print(f"Cannot read a spacing scale from {tokens_path}. Spacing is not checked.")
    violations = 0
    for f in files:
        if not f.exists():
            print(f"ERROR  {f} does not exist")
            return 2
        if f.name.startswith("tokens.") or str(f) == tokens_path:
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if HEX.search(line) or FUNC.search(line):
                print(f"{f}:{n}: raw colour. Use a semantic token.")
                violations += 1
            if allowed is not None:
                for m in SPACING.finditer(line):
                    for px in PX.findall(m.group(1)):
                        if abs(float(px)) not in allowed:
                            print(f"{f}:{n}: {px}px is not on the spacing scale.")
                            violations += 1
    if not violations:
        print("Clean: no raw colours or off-scale spacing found.")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
