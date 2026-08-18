# Security policy

## Reporting a vulnerability

Do not open a public issue containing sensitive meeting data, credentials, private links, or reproducible secrets.

Use GitHub's private vulnerability reporting for this repository when available. If it is not available, contact the repository owner through a private channel listed on the owner's GitHub profile and include only the minimum information required to reproduce the issue.

## Data boundary

The open Skill does not require a hosted MeetingAlign service and does not transmit data by itself. The agent environment, transcription tool, model provider, storage system, and integrations selected by the user may process data under their own policies. Review them before using real meetings.

Never commit real meeting transcripts, credentials, access tokens, customer data, personal data, regulated information, or unredacted internal decisions to this repository.
