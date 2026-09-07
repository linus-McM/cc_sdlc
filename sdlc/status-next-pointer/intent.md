# Intent: Status next pointer
Author: Linus McManamey. Status: accepted. Risk: low.

## Problem
`sdlc status` lists artifact states (accepted, draft, present, missing) but never says which
command comes next. Claude and the engineer have to reason about the pipeline order themselves
each time they resume a feature, and every other verdict in the plugin already carries a `next`
field, so `status` is the odd one out.

## Proposed outcome
`sdlc status` returns a `next` field naming the single command to run next, derived from the
artifact states: the first unaccepted stage artifact, then `/sdlc:test` until test-report.json
and review.md exist, then `/sdlc:deploy` until deploy.json records a production release, then
`/sdlc:maintain`. Resuming a feature becomes "run status, follow next".

## Affected users and systems
Claude sessions driving `/sdlc:*` commands; engineers reading the status verdict;
`scripts/sdlc/stages.py` (`status`) and its tests. No other stage changes.

## Constraints
Pure Python, stdlib only, deterministic. Must not change existing `artifacts` keys in the
status verdict. `next` values are limited to the six `/sdlc:<stage>` commands so markdown
commands can follow them verbatim.

## Open questions
none
