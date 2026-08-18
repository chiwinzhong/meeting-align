# Alignment gaps and explanatory score

## Materiality test

Flag a gap only when different interpretations could change at least one of:

- scope;
- owner;
- timing;
- quality or acceptance;
- dependency or handoff;
- customer or public promise;
- cost, compliance, or irreversible action.

## Gap categories

- `VAGUE_TIME`
- `VAGUE_QUALITY`
- `VAGUE_COMPLETION`
- `MISSING_OWNER`
- `MISSING_DEADLINE`
- `MISSING_DEFINITION_OF_DONE`
- `CONFLICTING_INTERPRETATION`
- `HIDDEN_DEPENDENCY`
- `MISSING_PARTICIPANT`
- `AUTHORITY_AMBIGUITY`
- `DECISION_DRIFT`
- `MATURITY_MISMATCH`
- `READINESS_MISMATCH`

## Risk levels

- `high`: can cause a materially wrong, public, expensive, regulated, or irreversible action;
- `medium`: can cause rework, missed coordination, or a delayed handoff;
- `low`: worth recording but unlikely to change near-term execution.

Do not inflate risk to make the output look more useful.

## Meeting-type-aware explanatory scores

Select a profile before weighting components.

### Kickoff and execution profile

| Component | Maximum |
| --- | ---: |
| Decision clarity | 20 |
| Ownership clarity | 20 |
| Deadline clarity | 15 |
| Definition-of-done clarity | 20 |
| Dependency clarity | 15 |
| Cross-role clarity | 10 |

### Strategy and co-creation profile

Emphasize direction clarity, strategic boundaries, maturity visibility, open-question visibility, role complementarity, next validation, and cross-role readiness risk. Do not heavily penalize missing deadlines that are not yet appropriate.

For each component:

1. report the awarded points;
2. cite the missing or conflicting fields behind deductions;
3. show which clarification would improve the component;
4. avoid decimal precision unless a deterministic calculation requires it.

When useful, show two indicators:

- **Alignment Score** — how aligned the outcome is for its meeting type;
- **Execution Readiness** — whether action can proceed without another material decision.

Interpret either score only as an explanatory view of this meeting record. It is not a measure of meeting quality, culture, employee performance, or organizational maturity.
