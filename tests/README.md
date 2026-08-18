# Adversarial contracts

`adversarial-contracts.json` contains eleven synthetic golden cases covering the audio gate, decision classification, rejected work, role translation, ambiguity resolution, ownership, dependencies, cognitive labeling, confirmation, and shared-decision consistency.

Run:

```bash
python3 tools/run_adversarial_contracts.py tests/adversarial-contracts.json
```

These deterministic fixtures verify that the documented expected results remain internally consistent. They do not prove that every model or runtime will generate those results from the source text. Generative performance requires a separately reported forward evaluation against held-out transcripts.

Never add a real person's name, recording metadata, or meeting content unless every necessary publication authorization has been documented. Prefer synthetic or fully anonymized cases.
