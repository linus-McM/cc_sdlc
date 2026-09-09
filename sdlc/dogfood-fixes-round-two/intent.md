# Intent: Dogfood fixes round two
Author: Linus McManamey. Status: accepted. Risk: low.

## Problem
Three rough edges surfaced while the first two features went through the pipeline:
1. `maintain watch` uses two-sided Western Electric rules, so a metric that improves
   (`tests_passed` rising from 61 to 66) trips a tier 3 breach and would propose an incident.
2. `deploy rehearse` runs `deploy.rollback` in the working checkout. On this repo the command is
   `git revert --no-edit HEAD`, so the rehearsal really reverted the last commit twice and had to be
   undone by hand with `git reset --hard HEAD~1`.
3. The post-edit plan-sync hook flags files outside the repository (a scratchpad script) because
   `rel_path` falls back to the absolute path when the file is not under the project root.

## Proposed outcome
1. `sdlc/bands.toml` accepts `bad = "low" | "high" | "both"` per metric (default `both`); only
   points on the bad side count toward a tier. `tests_passed` with `bad = "low"` stays at tier 0.
2. `deploy rehearse` runs the rollback command in a temporary detached git worktree of HEAD and
   removes it afterwards; the branch, index and working tree of the project are untouched.
3. Edits to paths outside the project root are ignored by both edit hooks.

## Affected users and systems
`scripts/sdlc/maintain.py` (`tier`, `watch`), `scripts/sdlc/deploy.py` (`rehearse`),
`scripts/sdlc/hooks.py` (`rel_path`), `templates/bands.toml`, `commands/maintain.md`,
`commands/deploy.md`, `sdlc/bands.toml` (new, this repo), tests for each.

## Constraints
Stdlib only. Rehearsal must still record exit code and tail in deploy.json and must still be the
same command `maintain` would run for real. No change to tier thresholds or rule spans. Existing
bands without `bad` behave exactly as before.

## Open questions
none
