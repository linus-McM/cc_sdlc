# Plan: Dogfood fixes round two
From: spec.md (2026-09-08). Status: accepted. Risk: low.

## Files that change
- scripts/sdlc/maintain.py
- scripts/sdlc/deploy.py
- scripts/sdlc/hooks.py
- tests/test_maintain.py
- tests/test_deploy.py
- tests/test_hooks.py
- templates/bands.toml
- sdlc/bands.toml (new)
- commands/maintain.md
- commands/deploy.md

## Order of work
1. Step `bands-side` (failing first): `tests/test_maintain.py::test_tier_one_sided_bands_ignore_the_good_side`
   asserts `tier([*BASE, 20.0], bad="low") == 0`, `tier([*BASE, 20.0], bad="high") == 3`,
   `tier([*BASE, 0.0], bad="high") == 0`, and the 2σ and 1σ rules likewise;
   `test_watch_reads_bad_side_and_rejects_unknown` writes bands.toml with `bad = "low"` for a
   rising metric (tier 0) and `bad = "sideways"` (verdict `ok: false` naming the metric).
   Then `maintain.tier` gains `bad`, `watch` validates and passes it.
2. Step `rehearse-worktree` (failing first): `tests/test_deploy.py::test_deploy_rehearse_runs_in_throwaway_worktree`
   configures rollback `git revert --no-edit HEAD`, records HEAD, runs rehearse, asserts ok,
   exit 0, HEAD unchanged, porcelain empty, one worktree listed;
   `test_deploy_rehearse_needs_git` deletes `.git` (a non-git tmp dir) and expects a verdict.
   Then `deploy.rehearse` runs in a detached worktree with try/finally removal.
3. Step `hook-outside-root` (failing first): `tests/test_hooks.py::test_hooks_ignore_paths_outside_root`
   asserts `pre_edit` and `post_edit` return None for `/private/tmp/elsewhere.py` even with a
   protected glob `**` and an accepted plan. Then `rel_path` returns None outside root.
4. Docs and template: `templates/bands.toml` gains a `bad` line per metric with the comment;
   `sdlc/bands.toml` for this repo (`tests_passed`, `bad = "low"`); `commands/maintain.md` and
   `commands/deploy.md` one sentence each. `sdlc build sync`, `/simplify`, `sdlc build sync`.
   Outcome of `/simplify`: the 3σ rule is `beyond(1, 1, 3)` so the side logic lives in one
   place; `rehearse` uses `tempfile.TemporaryDirectory` (drops `shutil`); the Western Electric
   test cases are one shared `HIGH_CASES` list driving both the two-sided and one-sided tests;
   a duplicate deploy.json assert dropped. Skipped: lifting the worktree into a `project.worktree`
   context manager (one caller today; lift when `maintain` calls the rollback).

## Risks
- Could break: `tier` callers passing positional args (only `watch`); the signature keeps
  `window` second. Bands without `bad` are unchanged because the default is `both`.
- Riskiest step: 2. `git worktree add` on a repo with uncommitted changes still works (it
  checks out HEAD), but a rollback command that expects the working tree state (not HEAD) will
  behave differently in the worktree. Documented in commands/deploy.md.
- Rejected: dry-run rollback commands (`--no-commit && --abort`): the rehearsal would then not
  prove the real command. Rejected: running the rehearsal on a copy of the directory without git
  (rollbacks in this plugin are git-shaped).
- Gotcha met while planning: `sdlc build new` overwrites an existing plan.md with the template;
  write the plan after `build new`, not before.

## Proof
- `uv run pytest -q`: 71 passed (66 existing + 5 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py maintain watch tests_passed` prints `"tier": 0`.
- `python3 scripts/sdlc.py deploy rehearse` on this branch leaves `git log --oneline -1` unchanged.
