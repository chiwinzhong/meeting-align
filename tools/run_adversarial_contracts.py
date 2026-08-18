#!/usr/bin/env python3
"""Validate MeetingAlign synthetic golden adversarial contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SEMANTIC_SECTIONS = (
    "decisions", "actions", "alignment_gaps", "roles", "understanding_checks"
)


def fail(case_id: str, message: str) -> None:
    print(f"FAIL: {case_id} — {message}")
    raise SystemExit(1)


def text(value) -> str:
    return json.dumps(value, ensure_ascii=False).casefold()


def evaluate(case: dict) -> None:
    case_id = case["id"]
    result = case.get("result", {})
    expected = case.get("expectations", {})
    all_text = text(result)

    if "ingestion_status" in expected:
        actual = result.get("ingestion", {}).get("status")
        if actual != expected["ingestion_status"]:
            fail(case_id, f"expected ingestion status {expected['ingestion_status']}, got {actual}")

    if expected.get("semantic_output_empty"):
        populated = [name for name in SEMANTIC_SECTIONS if result.get(name)]
        if populated:
            fail(case_id, f"blocked input contains semantic sections: {populated}")

    if "decision_count" in expected and len(result.get("decisions", [])) != expected["decision_count"]:
        fail(case_id, "decision count differs from contract")

    if "action_count" in expected and len(result.get("actions", [])) != expected["action_count"]:
        fail(case_id, "action count differs from contract")

    if "meeting_type" in expected and result.get("meeting_semantics", {}).get("primary_type") != expected["meeting_type"]:
        fail(case_id, "meeting type differs from contract")

    if "outcome_state" in expected and result.get("meeting_semantics", {}).get("outcome_state") != expected["outcome_state"]:
        fail(case_id, "outcome state differs from contract")

    minimum_questions = expected.get("strategic_open_questions_min")
    if minimum_questions is not None and len(result.get("strategic_open_questions", [])) < minimum_questions:
        fail(case_id, "too few strategic open questions")

    if "score_profile" in expected and result.get("alignment_score", {}).get("profile") != expected["score_profile"]:
        fail(case_id, "alignment score profile differs from contract")

    for phrase in expected.get("must_contain", []):
        if phrase.casefold() not in all_text:
            fail(case_id, f"missing required phrase: {phrase}")

    for phrase in expected.get("must_not_contain", []):
        if phrase.casefold() in all_text:
            fail(case_id, f"forbidden phrase found: {phrase}")

    actions_text = text(result.get("actions", []))
    for phrase in expected.get("actions_must_not_contain", []):
        if phrase.casefold() in actions_text:
            fail(case_id, f"forbidden action found: {phrase}")

    gaps = result.get("alignment_gaps", [])
    gap_types = {item.get("type") for item in gaps}
    for gap_type in expected.get("required_gap_types", []):
        if gap_type not in gap_types:
            fail(case_id, f"missing gap type: {gap_type}")
    gaps_text = text(gaps)
    for phrase in expected.get("gaps_must_not_contain", []):
        if phrase.casefold() in gaps_text:
            fail(case_id, f"resolved phrase remains a gap: {phrase}")

    roles = {item.get("role") for item in result.get("role_implications", [])}
    for role in expected.get("roles_present", []):
        if role not in roles:
            fail(case_id, f"missing role implication: {role}")

    pattern = expected.get("role_implications_must_not_match")
    if pattern and re.search(pattern, text(result.get("role_implications", []))):
        fail(case_id, f"role implication matches forbidden pattern: {pattern}")

    shared_id = expected.get("shared_decision_id")
    if shared_id:
        implication_ids = {item.get("decision_id") for item in result.get("role_implications", [])}
        if implication_ids != {shared_id}:
            fail(case_id, f"role implications do not share decision {shared_id}")

    owner_rule = expected.get("action_owner")
    if owner_rule:
        matches = [item for item in result.get("actions", []) if owner_rule["contains"].casefold() in item.get("action", "").casefold()]
        if len(matches) != 1 or matches[0].get("owner") != owner_rule["equals"]:
            fail(case_id, "missing-owner action contract failed")

    required_edges = set(expected.get("required_dependency_edges", []))
    if required_edges:
        actual_edges = {f"{item.get('from')}>{item.get('to')}" for item in result.get("dependencies", [])}
        if not required_edges <= actual_edges:
            fail(case_id, f"missing dependency edges: {sorted(required_edges - actual_edges)}")

    allowed_statuses = set(expected.get("allowed_check_statuses", []))
    if allowed_statuses:
        actual_statuses = {item.get("status") for item in result.get("understanding_checks", [])}
        if not actual_statuses or not actual_statuses <= allowed_statuses:
            fail(case_id, f"unexpected understanding-check statuses: {sorted(actual_statuses)}")

    for rule in expected.get("required_maturity", []):
        matches = [item for item in result.get("decision_maturity", []) if rule["contains"].casefold() in item.get("statement", "").casefold()]
        if len(matches) != 1 or matches[0].get("level") != rule["level"]:
            fail(case_id, f"maturity contract failed for: {rule['contains']}")

    guardrails_text = text([
        guardrail
        for role in result.get("roles", [])
        for guardrail in role.get("guardrails", [])
    ])
    for phrase in expected.get("guardrails_must_contain", []):
        if phrase.casefold() not in guardrails_text:
            fail(case_id, f"missing guardrail: {phrase}")
    for phrase in expected.get("guardrails_must_not_contain", []):
        if phrase.casefold() in guardrails_text:
            fail(case_id, f"unsupported guardrail found: {phrase}")

    comparisons = result.get("comparisons", [])
    required_profiles = set(expected.get("comparison_profiles", []))
    if required_profiles:
        actual_profiles = {item.get("profile") for item in comparisons}
        if not required_profiles <= actual_profiles:
            fail(case_id, f"missing comparison profiles: {sorted(required_profiles - actual_profiles)}")
    if expected.get("kickoff_penalty_stronger_than_strategy"):
        by_type = {item.get("meeting_type"): item for item in comparisons}
        strategy_penalty = by_type.get("STRATEGY_CO_CREATION", {}).get("missing_deadline_penalty")
        kickoff_penalty = by_type.get("PROJECT_KICKOFF", {}).get("missing_deadline_penalty")
        if not isinstance(strategy_penalty, (int, float)) or not isinstance(kickoff_penalty, (int, float)) or kickoff_penalty <= strategy_penalty:
            fail(case_id, "kickoff deadline penalty is not stronger than strategy penalty")

    print(f"PASS: {case_id} — {case['name']}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: run_adversarial_contracts.py tests/adversarial-contracts.json")
        return 2
    path = Path(sys.argv[1])
    suite = json.loads(path.read_text(encoding="utf-8"))
    cases = suite.get("cases", [])
    ids = [case.get("id") for case in cases]
    expected_ids = [f"T{number:02d}" for number in range(16)]
    if ids != expected_ids:
        fail("SUITE", f"case IDs must be exactly {expected_ids}")
    for case in cases:
        evaluate(case)
    print(f"ALL {len(cases)} ADVERSARIAL CONTRACTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
