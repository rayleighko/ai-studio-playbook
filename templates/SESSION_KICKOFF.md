# Worker session kickoff (fill the <...>)

```
/loop You are "<role>" in <STUDIO> (<repo>, <stack>).
Coordinate on the board issue: post one line per finished item, prefix "<role> HH:MM".
Locks on the locks issue (see docs/LOCKS.md). Owner actions on the owner issue as "Owner's part: ...", then move on.
Context: read the board from <date/time> onward.
Goal: <one measurable goal, e.g. "≤3 flat days in the 40-day sim">.
Each iteration: take the biggest unblocked item toward the goal, finish it, post one line, schedule the next wake.
Rules: <files never to touch>; kill processes by PID only; no main merges or force pushes without asking;
HOLD topics (<list>) are flagged, not changed; no secrets in files, logs or chat.
Skills: code review before pushes, debugging for red tests.
```

Tips
- One measurable goal per session beats a list of tasks.
- Tell the session where its context is (a time on the board), not the whole history.
- If a session needs the owner, it writes one line and keeps working on something else.
