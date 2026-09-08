# Spec: Rehearsal and band nits
From: intent.md (2026-09-08). Status: accepted. Risk: low.

## Requirements
1. `project.run_git(root, *args)` returns the `subprocess.CompletedProcess`; `project.git` is unchanged in signature and behaviour (stdout, trailing newline stripped).
2. `deploy.rehearse` fails with a `Blocked` whose reason contains git's stderr when `git worktree add` exits non-zero (no git checkout, no commits).
3. When `git worktree remove` exits non-zero after the rollback ran, `rehearse` still records the rollback result in deploy.json, then fails with a reason naming the leftover worktree path.
4. The rollback runs with cwd = worktree joined with the project root's path relative to `git rev-parse --show-toplevel`; when the project root is the repo top level that is the worktree itself.
5. Dangling rehearsal commits are accepted behaviour, documented in `commands/deploy.md` as pruned by git's own gc; no code change.
6. `maintain.tier` raises a `Blocked` naming the allowed values for an unknown `bad`; `watch` keeps its metric-naming check.
7. `hooks.release_hit` matches env tokens only against environments at the `gate` tier; `prod` is no longer a built-in alias. README and the hook docstring say so.

## Design
- `project.py`: `run_git` does the `subprocess.run`; `git` becomes `run_git(...).stdout.rstrip("\n")`.
- `deploy.py` `rehearse`: `added = p.run_git(root, "worktree", "add", "--detach", tmp, "HEAD")`; on non-zero `fail(f"rollback rehearsal could not create a worktree: {added.stderr.strip()}")`. cwd is `worktree / root.resolve().relative_to(Path(p.git(root, "rev-parse", "--show-toplevel")).resolve())`. In `finally`, `removed = p.run_git(root, "worktree", "remove", "--force", tmp)`. After writing deploy.json, if `removed.returncode` is non-zero, `fail(f"rehearsal worktree left behind at {tmp}: {removed.stderr.strip()}", **result)`. The `.git` existence check goes away.
- `maintain.py` `tier`: `signs = SIDES.get(bad) or fail(f"bad must be one of {sorted(SIDES)}, not {bad!r}")`.
- `hooks.py` `release_hit`: `names = set(gated)`; docstring drops "or prod".
- Docs: README pre-bash bullet drops "(or `prod`)"; `commands/deploy.md` rehearse paragraph says dangling objects are pruned by gc and that the rollback runs at the project's own path inside the worktree.

## Concerns
none. No auth, PII, payments, migration or infra.

## Open questions
none carried from intent.md.

## Proof
- `tests/test_deploy.py`: `test_deploy_rehearse_needs_git` asserts git's stderr text appears in the reason (requirement 2); `test_deploy_rehearse_reports_leftover_worktree` makes removal fail by having the rollback command create a nested untracked directory that `--force` still removes, so instead it monkeypatches `project.run_git` to return a non-zero result for the remove call and asserts deploy.json is written and the reason names the path (requirement 3); `test_deploy_rehearse_runs_at_project_path` uses a project root that is a subdirectory of the repo and a rollback of `pwd`, asserting the tail ends with the subdirectory name (requirement 4).
- `tests/test_maintain.py`: `test_tier_rejects_unknown_side` (requirement 6).
- `tests/test_hooks.py`: `bin/deploy prod` moves from the denied list to the allowed list; a config naming `prod` at the gate tier makes it denied again (requirement 7).
- `uv run pytest`, ruff, `claude plugin validate --strict .` green.
