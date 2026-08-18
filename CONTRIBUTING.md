# Contributing

MeetingAlign welcomes issues and pull requests that improve decision traceability, role translation, gap detection, multilingual behavior, privacy, and evaluation.

## Useful contributions

- synthetic or fully authorized difficult transcripts;
- false-positive or missed alignment gaps;
- cases where proposals were mistaken for decisions;
- role-translation edge cases;
- multilingual meeting examples;
- validator and schema improvements;
- privacy-preserving evaluation methods.

Do not submit confidential meeting data, personal information, credentials, customer records, or material you do not have authority to publish.

## Development checks

```bash
python3 tools/validate_skill_package.py
python3 skills/meeting-align/scripts/validate_meeting_align.py \
  examples/launch-meeting/meeting-align.json
python3 skills/meeting-align/scripts/run_contract_tests.py \
  examples/launch-meeting/meeting-align.json
```

Pull requests should explain what changed, why the change improves alignment rather than output volume, which failure case it addresses, and how it was tested.
