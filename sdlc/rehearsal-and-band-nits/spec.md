# Spec: Rehearsal and band nits
From: intent.md (2026-09-08). Status: accepted. Risk: low.

## Requirements
1. `project.run_git(root, *args)` returns the `subprocess.CompletedProcess`; `project.git` is unchanged in signature and behaviour (stdout, trailing newline stripped).
2. `deploy.rehearse` fails with a `Blocked` whose reason contains git's stderr when `git worktree add` exits non-zero (no git checkout, no commits).
3. When `git worktree remove` exits non-zero after the rollback ran, `rehearse` records the rollback result in deploy.json with a `leftover` note (git's stderr and a `git worktree prune` hint; the temp directory itself is already gone, only the `.git/worktrees` entry survives), then fails with that note as the reason. A project path missing at HEAD (uncommitted subdirectory) is refused with a verdict before the rollback runs, and the worktree is removed. A failed rollback still owns the verdict when both fail.
4. The rollback runs with cwd = worktree joined with `git rev-parse --show-prefix` of the project root; at the repo top level the prefix is empty and cwd is the worktree itself.
5. Dangling rehearsal commits are accepted behaviour, documented in `commands/deploy.md` as pruned by git's own gc; no code change.
6. `maintain.bands` (the config parser) is the single owner of the `bad` check and raises a `Blocked` naming the metric; `tier` stays a pure numeric function and raises `KeyError` for a programming error. Revised during `/simplify` from "tier raises Blocked": two owners for one config key was the smell.
7. `hooks.release_hit` matches env tokens only against environments at the `gate` tier; `prod` is no longer a built-in alias. README and the hook docstring say so.

## Design
- `project.py`: `run_git` does the `subprocess.run`; `git` becomes `run_git(...).stdout.rstrip("\n")`.
- `deploy.py` `rehearse`: `prefix = p.git(root, "rev-parse", "--show-prefix")` before the worktree exists; `added = p.run_git(root, "worktree", "add", "--detach", tmp, "HEAD")`, on non-zero `fail` with git's stderr; straight-line `result = build.run_cmd(Path(tmp) / prefix, cmd)` then `removed = p.run_git(root, "worktree", "remove", "--force", tmp)` (nothing in between can raise, so no try/finally). A failed removal is written into `result["leftover"]` before deploy.json is saved; the exit check fails first, then the leftover check. The `.git` existence check goes away.
- `maintain.py`: `bands()` validates `bad` for every configured metric; `tier` keeps `SIDES[bad]`; `watch` has no check of its own.
- `hooks.py` `release_hit`: `names = set(gated)`; docstring drops "or prod".
- Docs: README pre-bash bullet drops "(or `prod`)"; `commands/deploy.md` rehearse paragraph says dangling objects are pruned by gc and that the rollback runs at the project's own path inside the worktree.

## Concerns
none. No auth, PII, payments, migration or infra.

## Open questions
none carried from intent.md.

## Proof
- `tests/test_deploy.py`: `test_deploy_rehearse_needs_git` asserts git's stderr text appears in the reason (requirement 2); `test_deploy_rehearse_reports_leftover_worktree` makes removal fail by having the rollback command create a nested untracked directory that `--force` still removes, so instead it monkeypatches `project.run_git` to return a non-zero result for the remove call and asserts deploy.json is written and the reason names the path (requirement 3); `test_deploy_rehearse_runs_at_project_path` uses a project root that is a subdirectory of the repo and a rollback of `pwd`, asserting the tail ends with the subdirectory name (requirement 4).
- `tests/test_maintain.py`: `test_tier_rejects_unknown_side` asserts `KeyError`; `test_watch_reads_bad_side_and_rejects_unknown` covers the `bands()` verdict (requirement 6).
- `tests/test_hooks.py`: `bin/deploy prod` moves from the denied list to the allowed list; a config naming `prod` at the gate tier makes it denied again (requirement 7).
- `uv run pytest`, ruff, `claude plugin validate --strict .` green.
