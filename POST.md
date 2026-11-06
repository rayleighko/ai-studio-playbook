# One person, seven AI sessions, one Steam game: the rules that actually kept it moving

I'm a solo developer in Seoul. Since late October I've been shipping a Steam idle game, *Hatchbar*, a tiny village that lives in a strip above the Windows taskbar. Over the same stretch I started a Roblox spin-off. Most of the code, art pipeline, research and marketing prep is done by AI coding sessions running on one desktop PC. I make the calls a human has to make: money, publishing, and what the game should feel like.

This post is not "AI made my game." It's the boring part: the coordination rules. Without them, five capable agents spend most of the day waiting on each other or on me.

## The cast

Each session is a separate Claude Code instance with one job:

| Session | Job |
|---|---|
| **core** | game logic, simulation, save format, merges into the release-candidate branch |
| **ui** | every screen, strings in 30 languages, layout at different DPI |
| **art** | sprite pipeline, image-generation calls, animation cleanup, store art |
| **pix** | research (store reviews, competitors), trailers and short videos, our own pixel-model study |
| **rbx** | the Roblox game, end to end |
| **relay** | reads the board every 20 minutes, forwards instructions, nudges anyone idle, settles small reversible questions |
| **cowork** | the session I talk to: plans, decides at night, play-tests, briefs me at 6 a.m. |

## Rule 1: one public board, one line per finished thing

Everything goes through a single GitHub issue. Every session posts one line when it finishes something: `core 21:36 done: depth journal, flat days 14 → 7, tests 409/0`. No chat side-channels for decisions. When I wake up I read one thread, not seven terminals.

## Rule 2: locks for the scarce things

One PC means one screen and about 32 GB of RAM. A second issue holds two locks:
- `screen in use / free` for anything that needs the display (captures, play-tests);
- `RAM in use / free` for builds and GPU jobs, with a minimum of 6 GB free before starting.

Heavy jobs run one at a time. This sounds slow, but crashing three builds at once is slower.

## Rule 3: a decision table, so the relay can say yes without me

Most questions agents ask are small: "re-run the flaky test or skip it?", "fallback layout A or B?". The decision table lets relay answer on its own if all of these hold:
- the change is reversible;
- the demo build is untouched;
- nothing goes public;
- nothing touches main.

Relay writes down which criterion it used. Anything about money, scope, art direction or publishing goes up to cowork, and from cowork to me.

## Rule 4: "R's part:" lines, then move on

My worst bottleneck was me. Agents would finish a task, need one click from me (a payment, a publish button), and wait for hours. Now a session blocked only on me writes one line starting `R's part:` and immediately takes its next item. I batch those clicks once a day; the big ones I keep for Friday evening.

## Rule 5: HOLD list

Some topics never change without me: drop odds, prices, economy numbers, rewards, ads. Player feedback that touches them gets triaged as HOLD. Agents can flag and simulate, not ship.

## Rule 6: measure the silence

Every night a script counts, per session, the longest gap between posts during the day. That number found every real problem:

| Day | What the numbers showed | Rule we changed |
|---|---|---|
| Nov 1 | ui finished 7 items; 4.6 h lost waiting for the screen | screen lock with time estimates |
| Nov 4 | relay silent for 3 h, twice | relay ticks every 20 min, no exceptions |
| Nov 5 | relay worst gap 60 min; core/ui 5 h holes gone; art waited 169 min **on me**, rbx 218 min | "R's part:" lines |
| Nov 6 | relay 40 min, core 63, ui 73, but rbx 515 min | rbx works from a queue file and starts the next item by itself |

## What still goes wrong

- Agents read their own notes too literally. One waiter script stopped because its stop-word appeared inside its own status message.
- An environment variable name mismatch cost an hour of image generation.
- After a reboot, sessions silently picked up an API key from the environment and started billing the wrong account.
- Terms of service matter. A model provider's terms forbid using its outputs to evaluate other models, so we redesigned a whole blind test around that.

## The numbers that matter to me

The game isn't out yet (the full release moved to January 2027 so the art can catch up), so I can't claim sales. What I can claim: one person kept seven parallel workstreams moving for two weeks, and the daily silence went from hours to under an hour for most sessions.

I'm cleaning up the templates (decision table, lock rules, relay and kickoff prompts) into a repo. If you run more than two agents at once and want them, the waitlist is below.
