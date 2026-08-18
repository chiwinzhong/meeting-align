# Alignment gaps

An alignment gap is an ambiguity that can materially change execution. It is not every vague phrase in a conversation.

MeetingAlign looks for:

- vague time, quality, completion, or scope;
- missing owners or authorities;
- missing acceptance criteria;
- conflicting interpretations;
- hidden dependencies or handoffs;
- affected roles that were not represented;
- decisions that drift during the meeting.

Each gap records the source phrase, what the meeting already clarified, what remains undefined, the likely consequence, the appropriate clarifier when known, and an evidence pointer.

The objective is the smallest useful gap set. Too many low-impact warnings create a second form of misalignment: nobody knows what to resolve first.
