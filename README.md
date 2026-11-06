# ai-studio-playbook (draft, private)

Templates for running several AI coding sessions as a small game studio on one machine, with one human making the calls.

| File | What it is |
|---|---|
| `templates/DECISION_TABLE.md` | what the relay may decide alone, and what goes up |
| `templates/LOCKS.md` | screen and RAM lock protocol |
| `templates/RELAY_PROMPT.md` | the relay session's standing prompt |
| `templates/SESSION_KICKOFF.md` | kickoff prompt skeleton for a worker session |
| `templates/QUEUE.md` | per-session queue file, so a session never idles between prompts |
| `templates/speed.py` | nightly silence metrics from the coordination board |
| `POST.md` / `POST_ko.md` | write-up draft (EN) and Korean summary |
| `site/waitlist.html` | waitlist page draft |

## Setup in 5 minutes
1. Create one GitHub issue as the **board** and one as the **locks** issue.
2. Copy `templates/` into your repo's `docs/`.
3. Start one session per role with `SESSION_KICKOFF.md`, filled in.
4. Start the relay last with `RELAY_PROMPT.md`.
5. Run `speed.py` nightly and change one rule for the biggest gap.

Status: draft. Not public. Secrets, account names and internal paths removed.
