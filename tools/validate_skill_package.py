#!/usr/bin/env python3
"""Validate the public MeetingAlign repository without third-party packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "meeting-align"
SKILL_FILE = SKILL_DIR / "SKILL.md"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "CITATION.cff",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "assets" / "meetingalign-concept-comic.png",
    ROOT / "docs" / "architecture.md",
    ROOT / "docs" / "evaluation.md",
    ROOT / "docs" / "security-and-privacy.md",
    SKILL_FILE,
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "meeting-align.schema.json",
    SKILL_DIR / "references" / "audio-ingestion.md",
    SKILL_DIR / "assets" / "meeting-align-template.json",
    SKILL_DIR / "scripts" / "validate_meeting_align.py",
    SKILL_DIR / "scripts" / "run_contract_tests.py",
    ROOT / "examples" / "launch-meeting" / "meeting-align.json",
    ROOT / "tests" / "adversarial-contracts.json",
    ROOT / "tools" / "run_adversarial_contracts.py",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "alignment-error.yml",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    fields = parse_frontmatter(skill_text)
    if set(fields) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description")
    if fields["name"] != "meeting-align":
        fail("Skill name must be meeting-align")
    if not 1 <= len(fields["description"]) <= 1024:
        fail("Skill description must contain 1 to 1024 characters")
    if len(skill_text.splitlines()) > 500:
        fail("SKILL.md must stay under 500 lines")

    forbidden = ["TODO", "npm install -g meeting-align-skill"]
    tracked_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json"}
    )
    for phrase in forbidden:
        if phrase in tracked_text:
            fail(f"forbidden placeholder or unverified claim found: {phrase}")

    for json_path in [
        SKILL_DIR / "references" / "meeting-align.schema.json",
        SKILL_DIR / "assets" / "meeting-align-template.json",
        ROOT / "examples" / "launch-meeting" / "meeting-align.json",
        ROOT / "tests" / "adversarial-contracts.json",
    ]:
        with json_path.open(encoding="utf-8") as handle:
            json.load(handle)

    png = (ROOT / "assets" / "meetingalign-concept-comic.png").read_bytes()
    if not png.startswith(b"\x89PNG\r\n\x1a\n"):
        fail("hero asset is not a valid PNG file")

    print("PASS: MeetingAlign public package")
    print(f"Skill lines: {len(skill_text.splitlines())}")
    print(f"Required files: {len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
