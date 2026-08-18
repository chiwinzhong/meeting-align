# Evaluation protocol

MeetingAlign should be evaluated as an interpretation-and-control layer, not as a generic summarizer. The public preview makes no causal business-performance claim.

## Level 1 — Contract correctness

Run the included deterministic checks:

```bash
python3 skills/meeting-align/scripts/validate_meeting_align.py \
  examples/launch-meeting/meeting-align.json
python3 skills/meeting-align/scripts/run_contract_tests.py \
  examples/launch-meeting/meeting-align.json
```

The package passes only when decisions point to allowed evidence, required action fields are visible, AI suggestions do not become decisions, and silence is not counted as alignment.

## Level 2 — Human review against a transcript

Use two reviewers who did not generate the package. For each high-impact item, record:

| Measure | Question |
| --- | --- |
| Decision precision | Does the output preserve exactly what was decided? |
| Evidence traceability | Can the reviewer locate the supporting passage? |
| Decision/proposal separation | Are rejected, deferred, and merely suggested options kept out of decisions? |
| Action completeness | Are owner, deadline, definition of done, and dependencies explicit or visibly missing? |
| Gap precision | Would resolving this gap materially change execution? |
| Gap recall | Did the output miss an ambiguity that later caused different interpretations? |
| Cross-role consistency | Do all briefs preserve the same decision and scope? |
| Unsupported-content rate | How many output claims lack transcript support? |

Reviewers should resolve disagreements and retain both the initial score and the adjudicated result.

## Level 3 — Field validation

With consent, compare MeetingAlign-assisted meetings with a pre-agreed baseline. Useful operational measures include:

- time from meeting end to reviewed action package;
- percentage of role briefs corrected by recipients;
- unresolved owner, deadline, or definition-of-done fields after confirmation;
- rework attributable to different interpretations;
- time spent in follow-up clarification;
- participant-reported confidence that scope and acceptance criteria are shared.

Do not claim improvement from a single anecdote. Publish sample size, meeting type, comparison method, missing data, and adverse cases.

## Failure log

For every material miss, record:

1. the source passage;
2. the generated interpretation;
3. why it was wrong or incomplete;
4. the correction;
5. whether a rule, validator, example, or human-review step should change.

Never use the Alignment Score to evaluate individual employees.
