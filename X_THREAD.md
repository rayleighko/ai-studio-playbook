# X thread draft (Oddhatch account)

1/
I'm one developer in Seoul making a Steam game. Most of the work is done by 7 AI coding sessions on one PC.

The hard part wasn't the code. It was stopping 7 agents from waiting on each other, and on me.

Here are the rules that worked 🧵

2/
One board. Every session posts one line per finished thing on a single GitHub issue:
"core 21:36 done: depth journal, flat days 14 → 7, tests 409/0"
I read one thread in the morning, not seven terminals.

3/
Locks for scarce things. One screen, ~32 GB RAM.
"RAM taken core ~25 min ~3 GB" / "RAM free"
Heavy jobs run one at a time. Slower on paper, faster than crashing three builds.

4/
A decision table. A relay session answers small questions alone if the change is reversible, the demo build is untouched, nothing goes public, nothing touches main.
Money, art direction and publishing go up to me.

5/
"Owner's part" lines. My worst bottleneck was me: agents waited hours for one click.
Now a blocked session writes one line and takes its next item. I batch the clicks.

6/
Measure the silence. Every night a script counts each session's longest quiet gap.
Nov 4: relay silent 3 h → 20-min ticks
Nov 5: waiting on me 218 min → owner's-part lines
Nov 6: one session 515 min → a queue file it pulls from by itself

7/
Still breaks: agents read notes too literally, env var names drift, and one reboot switched sessions to the wrong billing.

Templates (decision table, lock rules, relay + kickoff prompts, the silence script):
<GITHUB_REPO_URL>
Star it if you run 2+ agents. The game: store.steampowered.com/app/5384580
