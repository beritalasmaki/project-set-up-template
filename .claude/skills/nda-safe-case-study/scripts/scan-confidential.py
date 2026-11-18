#!/usr/bin/env python3
"""Scan files for terms that must not be published.

Reads a list of terms (one per line) from .confidential-terms in the current
folder, or from the path in --terms. Case-insensitive substring match.
The terms file holds real client names and must never be committed.

Usage:
  scan-confidential.py FILE [FILE ...] [--terms PATH]

Exit code 0 when nothing is found, 1 when a term is found, 2 on bad input.
A clean scan only means the listed terms are absent. It does not make a text safe to publish.
"""
import sys
from pathlib import Path


def main(argv):
    terms_path = Path(".confidential-terms")
    files = []
    args = list(argv)
    while args:
        a = args.pop(0)
        if a == "--terms":
            if not args:
                print("--terms needs a path")
                return 2
            terms_path = Path(args.pop(0))
        else:
            files.append(Path(a))
    if not files:
        print(__doc__)
        return 2
    if not terms_path.exists():
        print(f"No terms file at {terms_path}. Nothing scanned. "
              "Create one with one confidential term per line, and keep it out of git.")
        return 2
    terms = [t.strip() for t in terms_path.read_text(encoding="utf-8").splitlines()
             if t.strip() and not t.startswith("#")]
    found = 0
    for f in files:
        if not f.exists():
            print(f"ERROR  {f} does not exist")
            return 2
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            low = line.lower()
            for term in terms:
                if term.lower() in low:
                    print(f"FOUND  {f}:{n}  contains a listed term")
                    found += 1
    if not found:
        print(f"Clean: none of {len(terms)} listed terms found in {len(files)} file(s).")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
