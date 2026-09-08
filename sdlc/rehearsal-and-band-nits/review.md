# Review: Rehearsal and band nits
Reviewer: sdlc:reviewer agent. Status: done. Scope: git diff main...HEAD, three passes per REVIEW.md.

## Bugs
- Important: scripts/sdlc/deploy.py:86 with the try/finally gone, `build.run_cmd(Path(tmp) / prefix, cmd)` raised `FileNotFoundError` when the project's path did not exist in the HEAD checkout (subdirectory project not yet committed), so the user saw a traceback and the worktree entry leaked. Addressed in step `rehearse-uncommitted-path`: the directory is checked first, the worktree removed, and a `Blocked` verdict says to commit the path (`test_deploy_rehearse_runs_at_project_path` covers both halves).
- Nit: scripts/sdlc/deploy.py:89 the `leftover` note named the temp path, which `TemporaryDirectory` has already deleted; only the `.git/worktrees` entry survives. Addressed: the note carries git's stderr and the `git worktree prune` hint only.

## Security
- Nit: scripts/sdlc/hooks.py:112 dropping the `prod` literal means projects on the default config whose release script accepts `prod` lose pre-bash coverage of `./deploy.sh prod` unless they list `prod = "gate"`. Addressed: README says so next to the rule.
- `--show-prefix` cwd: reviewer confirmed no traversal or injection route; git never returns `..` or an absolute prefix.

## Compliance
- Nit: sdlc/rehearsal-and-band-nits/intent.md:24 proposed outcome 4 still said `tier` raises `Blocked`. Addressed: intent revised to name the parser as the single owner.
- Nit: sdlc/rehearsal-and-band-nits/plan.md:46 Risks still described the `--show-toplevel` approach. Addressed: rewritten to record the `--show-prefix` change and the uncommitted-path finding.
- Nit: tests/test_hooks.py:114 `test_pre_bash_gated_names_come_from_config_only` took `toml_config` but wrote `.sdlc.toml` by hand. Addressed: uses the fixture.

Nits: 5 of 5 reported. Requirements 1-7 confirmed by reviewer and verifier; TDD ordering slip on steps 2 and 3 already recorded in plan.md.
