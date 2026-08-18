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

## Risk levels

- `high`: can cause a materially wrong, public, expensive, regulated, or irreversible action;
- `medium`: can cause rework, missed coordination, or a delayed handoff;
- `low`: worth recording but unlikely to change near-term execution.

Do not inflate risk to make the output look more useful.

## Explanatory Alignment Score

Use a 100-point starting total with these maximums:

| Component | Maximum |
| --- | ---: |
| Decision clarity | 20 |
| Ownership clarity | 20 |
| Deadline clarity | 15 |
| Definition-of-done clarity | 20 |
| Dependency clarity | 15 |
| Cross-role clarity | 10 |

For each component:

1. report the awarded points;
2. cite the missing or conflicting fields behind deductions;
3. show which clarification would improve the component;
4. avoid decimal precision unless a deterministic calculation requires it.

Interpret the score only as the clarity of this meeting record for execution. It is not a measure of meeting quality, culture, employee performance, or organizational maturity.
