# Plan: Rehearsal and band nits
From: spec.md (2026-09-08). Status: accepted. Risk: low.

## Files that change
- scripts/sdlc/project.py
- scripts/sdlc/deploy.py
- scripts/sdlc/maintain.py
- scripts/sdlc/hooks.py
- tests/test_deploy.py
- tests/test_maintain.py
- tests/test_hooks.py
- README.md
- commands/deploy.md

## Order of work
One step at a time: write the step's test, `build red`, implement, `build green`, then the next.
1. Step `git-exit`: `tests/test_deploy.py::test_deploy_rehearse_needs_git` gains an assert that
   git's stderr (`not a git repository`) is in the reason; new
   `test_deploy_rehearse_reports_leftover_worktree` monkeypatches `sdlc.project.run_git` so the
   `worktree remove` call returns returncode 1 with stderr `boom`, then asserts deploy.json has
   the rollback result and the verdict is `ok: false` naming the temp path.
   Then `project.run_git` and the `rehearse` changes for requirements 1-3.
2. Step `rehearse-cwd`: `test_deploy_rehearse_runs_at_project_path` creates `repo/app` as the
   project root (its own `.sdlc.toml`, `sdlc/feat` artifacts copied) with rollback `pwd`, runs
   the CLI with `root=repo/app`, asserts the tail ends with `/app`. Then the cwd computation.
3. Step `tier-blocked`: `tests/test_maintain.py::test_tier_rejects_unknown_side` asserts
   `m.tier([*BASE, 1.0], bad="sideways")` raises `Blocked` whose message lists the sides.
   Then `SIDES.get(bad) or fail(...)`.
4. Step `hook-prod-alias`: `tests/test_hooks.py` moves `bin/deploy prod` and `bin/deploy prod/`
   to the allowed side and adds a case where `toml_config(deploy={"environments": {"prod": "gate"}})`
   makes `bin/deploy prod` denied. Then `names = set(gated)` and the docstring.
5. Docs: README pre-bash bullet, `commands/deploy.md` rehearse paragraph (gc note, cwd note).
   `sdlc build sync`, `/simplify`, `sdlc build sync`.

## Risks
- Could break: callers of `project.git` (unchanged signature); `test_deploy_rehearse_needs_git`
  relies on git's stderr wording `not a git repository`, stable across git versions.
- Riskiest step: 2. `git rev-parse --show-toplevel` returns a resolved path; the project root
  must be resolved the same way or `relative_to` raises. Both sides go through `Path.resolve()`.
- Rejected: `git gc --prune=now` after every rehearsal (touches the shared object store and is
  slow); a `prod` alias table in config (one more thing to configure; naming the env is enough).

## Proof
- `uv run pytest -q`: 76 passed (72 existing + 4 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py deploy rehearse` on this branch: ok, HEAD unchanged, one worktree listed.
