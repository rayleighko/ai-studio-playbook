# Decision table (for the relay session)

Workers post `decision request:` on the board with options (a/b/c) and their recommendation. The relay decides on its next tick if **all** of the following are true:

1. **Reversible:** a branch change, an rc-branch-only merge, a data/feature-flag change, a test or script change.
2. **The shipped/demo build is untouched.**
3. **Nothing goes public**, nothing touches main, no force push.
4. None of the criteria below conflict.

## Criteria (in order)
1. Whatever the owner already decided on the board or in the session wins.
2. Merge safety: 0 conflicts, 0 failing tests, 0 changes to other people's files.
3. The product's stated goals (e.g. first-hour feel, art quality) are protected.
4. Prefer the option backed by measurement (sim, tests, captures) over opinion.
5. Otherwise the worker's recommendation, if it states a reason.

## Goes up to the coordinator / owner
- Anything visual the owner must see, big rule changes, anything that costs money, publishing, account actions.
- Anything that fails one of the "relay may decide" checks.
- HOLD topics: odds, prices, economy numbers, rewards, ads.

## Format
`decision(relay): <link> → (b), confidence high, reversible [criteria 2, 4]`
