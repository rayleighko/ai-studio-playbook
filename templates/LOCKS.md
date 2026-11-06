# Locks (one machine, many sessions)

Use a dedicated issue. Post one line to take a lock and one to release it.

- `SCREEN taken <role> HH:MM ~N min — <what>` / `SCREEN free <role> HH:MM`
  For captures, play-tests, anything that needs the visible display or input focus.
- `RAM taken <role> HH:MM ~N min ~X GB — <what>` / `RAM free <role> HH:MM`
  For builds, test suites and GPU jobs. Start only with **≥6 GB physical free** and no other RAM lock (or when both jobs fit in the commit limit).

Rules:
- Estimate the minutes. If you run over, post an update.
- Background waiters may take the lock automatically, but must release it on exit (also on crash: use a finally/trap).
- Never kill another session's process. Kill only by PID, only your own.
- Stop-words in your guard scripts must match the start of a line, not any substring.
