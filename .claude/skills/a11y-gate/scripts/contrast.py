#!/usr/bin/env python3
"""Contrast and target-size checks for the a11y-gate skill.

Deterministic maths, no estimates. Standard library only.

Usage:
  contrast.py FG BG [--kind text|large-text|non-text]
  contrast.py --tokens design-system/tokens.json
  contrast.py --target WIDTHxHEIGHT      (CSS pixels)

Thresholds follow WCAG 2.2. Read the criteria for the exact requirements:
  1.4.3  Contrast (Minimum)   https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
  1.4.11 Non-text Contrast    https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
  2.5.8  Target Size (Minimum) https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

Exit code 0 when every check passes, 1 when any fails, 2 on bad input.
Passing a check here does not make a design accessible. It answers one narrow question.
"""
import json
import re
import sys

THRESHOLDS = {"text": 4.5, "large-text": 3.0, "non-text": 3.0}
TARGET_MIN_PX = 24


def parse_hex(value):
    m = re.fullmatch(r"#?([0-9a-fA-F]{6}|[0-9a-fA-F]{3})", value.strip())
    if not m:
        raise ValueError(f"not a hex colour: {value!r}")
    h = m.group(1)
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb):
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    l1, l2 = luminance(parse_hex(fg)), luminance(parse_hex(bg))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def lookup(tree, path):
    node = tree
    for part in path.split("."):
        node = node[part]
    return node


def resolve(tree, value, depth=0):
    if depth > 10:
        raise ValueError("token reference loop")
    m = re.fullmatch(r"\{(.+)\}", value)
    if m:
        return resolve(tree, lookup(tree, m.group(1)), depth + 1)
    return value


def check_tokens(path):
    with open(path, encoding="utf-8") as f:
        tokens = json.load(f)
    failures = 0
    for pair in tokens.get("contrastPairs", []):
        kind = pair.get("kind", "text")
        minimum = pair.get("min", THRESHOLDS[kind])
        try:
            fg = resolve(tokens, lookup(tokens, pair["text"]))
            bg = resolve(tokens, lookup(tokens, pair["on"]))
            r = ratio(fg, bg)
        except (KeyError, ValueError) as err:
            print(f"ERROR  {pair['text']} on {pair['on']}: {err}")
            failures += 1
            continue
        ok = r >= minimum
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'}   {r:5.2f}:1 (min {minimum})  {pair['text']} on {pair['on']}")
    return failures


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--tokens":
        if len(argv) < 2:
            print("usage: contrast.py --tokens FILE")
            return 2
        return 1 if check_tokens(argv[1]) else 0
    if argv[0] == "--target":
        if len(argv) < 2 or not re.fullmatch(r"\d+(\.\d+)?x\d+(\.\d+)?", argv[1]):
            print("usage: contrast.py --target WIDTHxHEIGHT")
            return 2
        w, h = (float(x) for x in argv[1].split("x"))
        ok = w >= TARGET_MIN_PX and h >= TARGET_MIN_PX
        print(f"{'PASS' if ok else 'FAIL'}   {w:g}x{h:g} px (min {TARGET_MIN_PX}x{TARGET_MIN_PX}). "
              "WCAG 2.5.8 has exceptions (spacing, inline, equivalent control): "
              "a FAIL here needs a human to check them.")
        return 0 if ok else 1
    if len(argv) < 2:
        print("usage: contrast.py FG BG [--kind text|large-text|non-text]")
        return 2
    kind = "text"
    if "--kind" in argv:
        kind = argv[argv.index("--kind") + 1]
        if kind not in THRESHOLDS:
            print(f"unknown kind {kind!r}; use text, large-text or non-text")
            return 2
    try:
        r = ratio(argv[0], argv[1])
    except ValueError as err:
        print(f"ERROR  {err}")
        return 2
    ok = r >= THRESHOLDS[kind]
    print(f"{'PASS' if ok else 'FAIL'}   {r:.2f}:1 (min {THRESHOLDS[kind]} for {kind})  {argv[0]} on {argv[1]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
