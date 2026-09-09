# Intent: Rehearsal and band nits
Author: Linus McManamey. Status: accepted. Risk: low.

## Problem
Five nits left open by the review of dogfood-fixes-round-two:
1. `deploy.rehearse` discards the exit status of `git worktree add` and `git worktree remove`, so a
   failed add reports a guessed reason and a failed remove leaves a stale `.git/worktrees` entry
   plus a full checkout in the temp dir with no signal.
2. The rehearsal runs the rollback at the worktree top level; when the project root is a
   subdirectory of the repository the command gets a different cwd than a real rollback would.
3. Rehearsal commits stay in the object store as dangling objects until git gc.
4. `maintain.tier` raises a bare `KeyError` for an unknown `bad` when called by anything other
   than `watch`.
5. The pre-bash hook treats `prod` as a gated environment alias, but `deploy.check` rejects
   `prod` as unknown, so hook and mechanic disagree on what gated means.

## Proposed outcome
1. `project.run_git` returns the full result; `rehearse` fails with git's own stderr when the
   worktree cannot be created and, after recording the rollback result, fails when it cannot be
   removed, naming the leftover path.
2. The rollback runs in the worktree at the same relative path as the project root within the
   repository.
3. Documented as accepted behaviour: dangling objects are pruned by git's own gc; no code change.
4. One owner for the `bad` check: the bands.toml parser raises a `Blocked` naming the metric;
   `tier` stays a pure function (revised from "tier raises Blocked" during `/simplify`).
5. The hook matches only environment names configured at the `gate` tier; the `prod` literal goes.
   A project that calls its environment `prod` lists it in `[deploy.environments]`.

## Affected users and systems
`scripts/sdlc/project.py`, `scripts/sdlc/deploy.py`, `scripts/sdlc/maintain.py`,
`scripts/sdlc/hooks.py`, their tests, `README.md`, `commands/deploy.md`.

## Constraints
Stdlib only. `project.git` keeps its string-returning signature for existing callers. Behaviour
of `deploy.check`, `deploy.record` and the band thresholds unchanged.

## Open questions
none
