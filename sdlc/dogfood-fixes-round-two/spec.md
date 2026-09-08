# Spec: Dogfood fixes round two
From: intent.md (2026-09-08). Status: accepted. Risk: low.

## Requirements
1. `maintain.tier(values, window, bad="both")` counts a point toward a rule only when it lies on the bad side: `bad = "high"` ignores points below the mean, `bad = "low"` ignores points above it, `"both"` is today's behaviour. The zero-variance case follows the same rule.
2. `sdlc/bands.toml` accepts `bad` per metric; `watch` passes it to `tier`; an unknown value fails with a `Blocked` verdict naming the metric.
3. This repo's `sdlc/bands.toml` declares `tests_passed` with `bad = "low"`, and `maintain watch` on the current readings reports tier 0.
4. `deploy rehearse` runs `deploy.rollback` inside a temporary detached git worktree of HEAD (`git worktree add --detach`), records `cmd`, `exit`, `tail` and `ts` in deploy.json as today, and removes the worktree afterwards even when the command fails. HEAD, the index and the working tree of the project are unchanged after a rehearsal whose rollback is `git revert --no-edit HEAD`.
5. When the project is not a git checkout, `deploy rehearse` fails with a `Blocked` verdict saying a git checkout is needed.
6. `hooks.rel_path` returns None for a path outside the project root, so `pre_edit` and `post_edit` stay silent for such edits.
7. `templates/bands.toml` documents `bad`; `commands/maintain.md` mentions it; `commands/deploy.md` says the rehearsal runs in a throwaway worktree.

## Design
- `maintain.py`: `tier` gains `bad: str = "both"`. Signs to test: `(1,)` for high, `(-1,)` for low, `(1, -1)` for both. `beyond(n, k, limit)` becomes `any(sum(x * s > limit for x in tail) >= k for s in signs)`; the 3σ check `any(z[-1] * s > 3 for s in signs)`; zero variance `any((values[-1] - mean) * s > 0 for s in signs)`. `DEFAULT_BAND` gains `"bad": "both"`; `watch` validates `bad in ("low", "high", "both")` via `project.fail` and passes it through.
- `deploy.py`: `rehearse` creates `tempfile.mkdtemp()`, runs `git worktree add --detach <dir> HEAD` through `project.git`; if the worktree is not created, `fail("rollback rehearsal needs a git checkout")`. Runs `build.run_cmd(worktree, cmd)` inside a `try/finally` that runs `git worktree remove --force <dir>`. Result recorded exactly as before.
- `hooks.py`: `rel_path` returns None in the `except ValueError` branch.
- Docs and template one line each.

## Concerns
none. No auth, PII, payments, migration or infra. The rehearsal now touches only a throwaway worktree, which is strictly safer than before.

## Open questions
none carried from intent.md.

## Proof
- `tests/test_maintain.py`: `test_tier_one_sided_bands_ignore_the_good_side`, `test_watch_reads_bad_side_and_rejects_unknown` (requirements 1-2).
- `tests/test_deploy.py`: `test_deploy_rehearse_runs_in_throwaway_worktree` with rollback `git revert --no-edit HEAD` asserting HEAD unchanged, `git status --porcelain` empty, `git worktree list` back to one entry, deploy.json rollback exit 0 (requirement 4); `test_deploy_rehearse_needs_git` (requirement 5).
- `tests/test_hooks.py`: `test_hooks_ignore_paths_outside_root` (requirement 6).
- `python3 scripts/sdlc.py maintain watch tests_passed` on this repo prints tier 0 (requirement 3).
- `uv run pytest`, ruff, `claude plugin validate --strict .` green.
