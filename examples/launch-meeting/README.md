# Launch meeting demo

This entire example is fictional. It exists to demonstrate MeetingAlign's meeting-type detection, maturity tracking, traceability, role translation, guardrails, gap detection, and output contract without exposing a real organization or meeting.

Read in this order:

1. [Transcript](transcript.md)
2. [Meeting Type](meeting-type.md)
3. [Meeting Truth](meeting-truth.md)
4. [Host View](host-view.md)
5. [Alignment Gaps](alignment-gaps.md)
6. [Role Briefs](roles/)
7. [Understanding Checks](understanding-checks.md)
8. [Machine-readable package](meeting-align.json)

Validate the package:

```bash
python3 skills/meeting-align/scripts/validate_meeting_align.py \
  examples/launch-meeting/meeting-align.json
```
