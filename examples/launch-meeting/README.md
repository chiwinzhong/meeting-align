# Launch meeting demo

This entire example is fictional. It exists to demonstrate MeetingAlign's traceability, role translation, gap detection, and output contract without exposing a real organization or meeting.

Read in this order:

1. [Transcript](transcript.md)
2. [Meeting Truth](meeting-truth.md)
3. [Host View](host-view.md)
4. [Alignment Gaps](alignment-gaps.md)
5. [Role Briefs](roles/)
6. [Understanding Checks](understanding-checks.md)
7. [Machine-readable package](meeting-align.json)

Validate the package:

```bash
python3 skills/meeting-align/scripts/validate_meeting_align.py \
  examples/launch-meeting/meeting-align.json
```
