#!/usr/bin/env python3
"""
BTBA Skill Validator — skills/validate_skills.py

Checks structural conventions in skills/<name>/SKILL.md against the local
authoring standard (see skills/README.md). The flat routing fields and short
description recommendation are local conventions, not upstream requirements.
This does not validate engineering content, routing behavior, or readiness.

Usage:
    python skills/validate_skills.py
    python skills/validate_skills.py --skill drawing-reader
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

SKILLS_ROOT = Path(__file__).parent
MAX_DESCRIPTION_CHARS = 200  # Local style recommendation, not an upstream limit
MAX_SKILL_MD_LINES = 500
REQUIRED_FIELDS = ("name", "description")
STRING_FIELDS = (
    "name", "description", "license", "safety_level", "status",
    "dependencies", "run_before", "load_priority",
)
LIST_FIELDS = ("triggers", "load_with", "auto_load_on")
KNOWN_FIELDS = {
    "name", "description", "license",
    "triggers", "load_with", "safety_level", "dependencies", "run_before",
    "load_priority", "auto_load_on", "status",
}
SAFETY_LEVELS = ("low", "medium", "high", "critical")
STATUS_VALUES = ("unreviewed", "draft", "production")
TRUST_BOUNDARY_HEADING = re.compile(r"^##\s+Trust Boundary\s*$", re.MULTILINE)


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous configuration instead of silently keeping the last key."""


def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(None, None, "Field names must be strings", key_node.start_mark)
        if key in mapping:
            raise yaml.constructor.ConstructorError(None, None, f"Duplicate field: {key}", key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].rstrip() != "---":
        return None, "SKILL.md must start with '---' frontmatter delimiter"
    closing = next((i for i in range(1, len(lines)) if lines[i].rstrip() == "---"), None)
    if closing is None:
        return None, "Could not find closing '---' for frontmatter"
    try:
        fm = yaml.load("\n".join(lines[1:closing]), Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError, OverflowError, RecursionError) as e:
        return None, f"Invalid YAML frontmatter: {e}"
    if not isinstance(fm, dict):
        return None, "Frontmatter must be a YAML mapping, not empty, scalar, or list data"
    if any(not isinstance(key, str) for key in fm):
        return None, "Frontmatter field names must be strings"
    return fm, None


def validate_skill(skill_dir: Path) -> list:
    """Returns a list of (level, message) tuples. level is 'error' or 'warn'."""
    issues = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [("error", "Missing SKILL.md")]

    try:
        text = skill_md.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as e:
        return [("error", f"Could not read SKILL.md: {e}")]
    line_count = len(text.splitlines())

    fm, err = load_frontmatter(text)
    if err:
        issues.append(("error", err))
        return issues  # can't check further without valid frontmatter

    for field in REQUIRED_FIELDS:
        if field not in fm:
            issues.append(("error", f"Missing required field: {field}"))

    for field in STRING_FIELDS:
        if field in fm and (not isinstance(fm[field], str) or not fm[field].strip()):
            issues.append(("error", f"{field} must be a non-empty string"))

    for field in LIST_FIELDS:
        if field not in fm:
            continue
        value = fm[field]
        if not isinstance(value, list) or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            issues.append(("error", f"{field} must be a YAML list of non-empty strings (use [] if none)"))

    name = fm.get("name")
    if isinstance(name, str) and name.strip():
        if name != skill_dir.name:
            issues.append(("error", f"name '{name}' does not match directory name '{skill_dir.name}'"))
        if not re.fullmatch(r"[a-z0-9-]+", name):
            issues.append(("error", f"name '{name}' must be lowercase letters, numbers, and hyphens only"))
        if len(name) > 64:
            issues.append(("error", f"name is {len(name)} chars, max is 64"))

    desc = fm.get("description")
    if isinstance(desc, str) and len(desc) > MAX_DESCRIPTION_CHARS:
        issues.append((
            "warn",
            f"description is {len(desc)} chars; local style recommends at most "
            f"{MAX_DESCRIPTION_CHARS} for concise routing hints (not an upstream limit)",
        ))

    if "metadata" in fm:
        issues.append((
            "error",
            "Uses nested 'metadata:' block — this repo's standard keeps triggers/load_with/"
            "safety_level as flat top-level fields (see skills/README.md)",
        ))

    unknown = set(fm.keys()) - KNOWN_FIELDS
    if unknown:
        issues.append(("warn", f"Unrecognized frontmatter field(s): {sorted(unknown)}"))

    if line_count > MAX_SKILL_MD_LINES:
        issues.append((
            "warn",
            f"SKILL.md is {line_count} lines, exceeds the {MAX_SKILL_MD_LINES}-line guideline — "
            "move detailed reference material to references/",
        ))

    safety_level = fm.get("safety_level")
    if isinstance(safety_level, str) and safety_level not in SAFETY_LEVELS:
        issues.append(("warn", f"safety_level '{safety_level}' should be one of: {', '.join(SAFETY_LEVELS)}"))

    status = fm.get("status")
    if "status" not in fm:
        issues.append(("warn", "No status declared; treat as unreviewed, not implicit production"))
    elif isinstance(status, str) and status not in STATUS_VALUES:
        issues.append(("warn", f"status '{status}' should be one of: {', '.join(STATUS_VALUES)}"))
    elif status == "production":
        issues.append(("warn", "status: production is self-declared; verify review and test evidence separately"))

    if isinstance(safety_level, str) and safety_level in ("high", "critical") and not TRUST_BOUNDARY_HEADING.search(text):
        issues.append((
            "warn",
            "safety_level is high/critical but SKILL.md has no '## Trust Boundary' section — "
            "state what is preliminary and what needs a task-appropriate Norwegian "
            "designer, trade, surveyor or authority review (see skills/README.md)",
        ))

    scripts_dir = skill_dir / "scripts"
    if scripts_dir.is_dir() and any(scripts_dir.iterdir()) and "dependencies" not in fm:
        issues.append((
            "warn",
            "Has scripts/ but no 'dependencies' field declaring what they require",
        ))

    return issues


def main():
    parser = argparse.ArgumentParser(description="Check BTBA skill structure, not content accuracy or production readiness")
    parser.add_argument("--skill", help="Validate only this skill (directory name)")
    args = parser.parse_args()

    skill_dirs = [d for d in sorted(SKILLS_ROOT.iterdir()) if d.is_dir() and not d.name.startswith("_")]
    if args.skill:
        skill_dirs = [d for d in skill_dirs if d.name == args.skill]
        if not skill_dirs:
            print(f"No such skill: {args.skill}")
            sys.exit(1)

    total_errors = 0
    total_warnings = 0
    for d in skill_dirs:
        issues = validate_skill(d)
        if not issues:
            print(f"OK    {d.name} (structure only)")
            continue
        print(f"--    {d.name}")
        for level, msg in issues:
            marker = "ERROR" if level == "error" else "WARN "
            print(f"      [{marker}] {msg}")
            if level == "error":
                total_errors += 1
            else:
                total_warnings += 1

    print(f"\n{len(skill_dirs)} skills checked — {total_errors} error(s), {total_warnings} warning(s)")
    print("Structural lint only. No engineering, routing, dependency-graph, or production certification.")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
