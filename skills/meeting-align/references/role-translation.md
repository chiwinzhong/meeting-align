# Role translation

## Principle

Translate one shared decision into relevant professional implications. Do not create separate truths for separate functions.

## Translation sequence

For each role:

1. select only the decisions, actions, dependencies, and risks that affect the role;
2. distinguish what the meeting explicitly assigned from what execution logically requires;
3. label the latter `EXECUTION_IMPLICATION`;
4. preserve unknown deadline or definition-of-done fields;
5. identify inputs the role needs and downstream roles that depend on it;
6. produce the six-question brief and one understanding check.

## Professional depth

When reliable role evidence exists, adapt the amount of context for:

- executive or decision-maker;
- professional lead;
- experienced executor;
- junior executor.

Never infer intelligence or competence. If depth is uncertain, write for a competent general professional.

## Common role emphasis

| Domain | Typical meaning to surface |
| --- | --- |
| Product | user scope, priority, acceptance, trade-offs, sequencing |
| Engineering | technical scope, environments, dependencies, reliability, test conditions |
| Design | user states, observable quality, assets, review owner, handoff |
| Marketing | audience, claim, channel, launch state, required product truth |
| Sales | target accounts, demo state, promise boundaries, customer feedback loop |
| Operations | process owner, handoff, service level, exception path |
| Finance | budget, approval, timing, commercial assumption, reporting |
| Legal / compliance | regulated claim, review gate, evidence, jurisdiction, authority |
| HR / people | affected population, policy owner, privacy, communication, escalation |

The table suggests questions; it does not create meeting facts.

## Dependency language

Write dependencies in directional form:

```text
Role A needs [input] from Role B by [time] so that [action] can meet [definition of done].
```

If any element is missing, preserve it as `not yet defined` and consider an alignment gap.
