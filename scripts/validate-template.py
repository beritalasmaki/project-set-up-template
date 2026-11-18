#!/usr/bin/env python3
"""Validate that this template keeps its own rules.

Checks:
  - AGENTS.md is at most 100 lines; CLAUDE.md starts with @AGENTS.md
  - every skill folder has a SKILL.md with name (matching the folder) and a description
  - name + description fit the 1,536-character listing cap; SKILL.md is under 500 lines
  - no README.md inside a skill folder
  - files a SKILL.md links to (references/, scripts/, assets/) exist
  - every artefact template has a "Done when" section
  - JSON files parse; token contrast pairs pass
  - relative Markdown links between repo files resolve
  - the overview diagram in README.md matches docs/workflow-map.md
  - docs/skills.md matches the skills (regenerate with --write-catalog)

Usage:
  validate-template.py [--write-catalog]

Exit code 0 when all checks pass, 1 when any fails. Standard library only.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

# Workflow stages. Keep in step with docs/ai-workflow.md.
# Each skill names its stage in its own frontmatter (metadata.stage). The skills stay in one
# flat folder because that is the only layout Claude Code documents for project skills.
STAGES = [
    ("frame", "1. Frame the problem", "00 product context, 01 problem framing"),
    ("people", "2. Understand the people", "02 stakeholder map, 03 requirements spec"),
    ("design", "3. Design", "04 user flows and states, 07 design system rules"),
    ("check", "4. Check", "05 accessibility checklist, 06 security and privacy brief, sameness review"),
    ("handoff", "5. Hand off", "08 handoff spec, 09 stakeholder feedback log"),
    ("record", "6. Record and reflect", "10 decision log, 11 case study notes"),
]
STAGE_KEYS = [s[0] for s in STAGES]


def fail(msg):
    errors.append(msg)


def lines(path):
    return path.read_text(encoding="utf-8").splitlines()


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    current = None
    for line in m.group(1).splitlines():
        if line.startswith("  ") and current is not None and ":" in line:
            k, v = line.strip().split(":", 1)
            data[current][k.strip()] = v.strip()
        elif ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            k, v = k.strip(), v.strip()
            data[k] = v if v else {}
            current = k if not v else None
    return data


def check_agents():
    agents, claude = ROOT / "AGENTS.md", ROOT / "CLAUDE.md"
    if not agents.exists():
        return fail("AGENTS.md is missing")
    n = len(lines(agents))
    if n > 100:
        fail(f"AGENTS.md has {n} lines (max 100)")
    if not claude.exists() or not lines(claude) or lines(claude)[0].strip() != "@AGENTS.md":
        fail("CLAUDE.md must start with @AGENTS.md")


def skills():
    return sorted(p for p in (ROOT / ".claude" / "skills").glob("*") if p.is_dir())


def check_skills():
    for d in skills():
        sk = d / "SKILL.md"
        if not sk.exists():
            fail(f"{d.name}: SKILL.md is missing")
            continue
        fm = parse_frontmatter(sk)
        if fm is None:
            fail(f"{d.name}: SKILL.md has no frontmatter")
            continue
        if fm.get("name") != d.name:
            fail(f"{d.name}: frontmatter name {fm.get('name')!r} must match the folder")
        meta = fm.get("metadata", {})
        stage = meta.get("stage") if isinstance(meta, dict) else None
        if stage not in STAGE_KEYS:
            fail(f"{d.name}: metadata.stage must be one of {', '.join(STAGE_KEYS)} (found {stage!r})")
        desc = fm.get("description", "")
        if not desc:
            fail(f"{d.name}: description is missing")
        if len(desc) + len(fm.get("when_to_use", "")) > 1536:
            fail(f"{d.name}: description is over 1,536 characters")
        if "Do not use" not in desc:
            fail(f"{d.name}: description should say when not to use the skill")
        n = len(lines(sk))
        if n >= 500:
            fail(f"{d.name}: SKILL.md has {n} lines (keep under 500)")
        if (d / "README.md").exists():
            fail(f"{d.name}: remove README.md from the skill folder")
        for link in re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", sk.read_text(encoding="utf-8")):
            if not (d / link).exists():
                fail(f"{d.name}: referenced file {link} does not exist")


def check_artefacts():
    for f in sorted((ROOT / "artefacts").glob("[0-9][0-9]-*.md")):
        if "## Done when" not in f.read_text(encoding="utf-8"):
            fail(f"{f.relative_to(ROOT)}: missing a 'Done when' section")


def check_json():
    for f in [ROOT / ".claude" / "settings.json", ROOT / "design-system" / "tokens.json"]:
        if not f.exists():
            fail(f"{f.relative_to(ROOT)} is missing")
            continue
        try:
            json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as err:
            fail(f"{f.relative_to(ROOT)}: invalid JSON ({err})")
    script = ROOT / ".claude" / "skills" / "a11y-gate" / "scripts" / "contrast.py"
    tokens = ROOT / "design-system" / "tokens.json"
    if script.exists() and tokens.exists():
        r = subprocess.run([sys.executable, str(script), "--tokens", str(tokens)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            fail("token contrast pairs fail:\n" + r.stdout.strip())


def check_links():
    pattern = re.compile(r"\]\((?!https?://|mailto:|#)([^)\s]+)\)")
    for f in ROOT.rglob("*.md"):
        if ".git" in f.parts:
            continue
        for target in pattern.findall(f.read_text(encoding="utf-8")):
            path = target.split("#")[0]
            if path and not (f.parent / path).exists():
                fail(f"{f.relative_to(ROOT)}: broken link {target}")


def first_mermaid(path):
    m = re.search(r"```mermaid\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    return m.group(1).strip() if m else None


def check_diagrams():
    """The overview diagram in README.md is a copy of the first one in docs/workflow-map.md."""
    source = ROOT / "docs" / "workflow-map.md"
    readme = ROOT / "README.md"
    if not source.exists():
        return fail("docs/workflow-map.md is missing")
    if first_mermaid(source) is None:
        return fail("docs/workflow-map.md has no mermaid diagram")
    if first_mermaid(readme) != first_mermaid(source):
        fail("the overview diagram in README.md differs from docs/workflow-map.md. Copy the first diagram across.")


def catalog():
    rows = ["# Skills by workflow stage", "",
            "Generated by `scripts/validate-template.py --write-catalog` from each skill's frontmatter. Do not edit by hand.",
            "The skills sit in one flat folder (`.claude/skills/`), the layout Claude Code documents. "
            "Each names its stage in `metadata.stage`, and this page groups them by it.", ""]
    parsed = {d.name: (parse_frontmatter(d / "SKILL.md") or {}) for d in skills()}
    for key, title, artefacts in STAGES:
        rows += [f"## {title}", "", f"Artefacts: {artefacts}", ""]
        members = [n for n, fm in parsed.items()
                   if isinstance(fm.get("metadata"), dict) and fm["metadata"].get("stage") == key]
        if not members:
            rows += ["_No skill for this stage yet._", ""]
            continue
        rows += ["| Skill | What it does and when it is used |", "|---|---|"]
        for n in sorted(members):
            rows.append(f"| `{n}` | {parsed[n].get('description', '').replace('|', '/')} |")
        rows.append("")
    return "\n".join(rows)


def check_catalog(write):
    target = ROOT / "docs" / "skills.md"
    content = catalog()
    if write:
        target.write_text(content, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")
    elif not target.exists() or target.read_text(encoding="utf-8") != content:
        fail("docs/skills.md is out of date. Run: python3 scripts/validate-template.py --write-catalog")


def main(argv):
    write = "--write-catalog" in argv
    check_agents()
    check_skills()
    check_artefacts()
    check_json()
    check_links()
    check_diagrams()
    check_catalog(write)
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  FAIL  {e}")
        return 1
    print("OK: all template checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
