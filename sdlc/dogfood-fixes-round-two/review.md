# Review: Dogfood fixes round two
Reviewer: sdlc:reviewer agent. Status: done. Scope: git diff sdlc/release-hook-hardening...HEAD, three passes per REVIEW.md.

## Bugs
- Nit: scripts/sdlc/deploy.py:84 the rollback now runs at the worktree top level; when the project root is a subdirectory of the repo the command's cwd differs from before. Not addressed; documented risk.
- Nit: scripts/sdlc/deploy.py:89 `worktree remove` exit status is discarded, so a failed removal leaves a stale `.git/worktrees` entry without a signal. Not addressed.
- Nit: scripts/sdlc/maintain.py:72 `bad` was validated only for metrics with readings, so a typo on a band without readings stayed silent. Addressed: every configured band is validated before readings are read.
- Nits withheld: 2 (`git worktree add` stderr dropped; `tier` raises `KeyError` for callers other than `watch`).

## Security
- Important: scripts/sdlc/hooks.py:42 `rel_path` resolved symlinks before the root test, so an in-repo symlink to an outside file (`linked.py -> ../outside_secret.py`) returned None and both guards went silent, where the old fallback denied it. Addressed in step `rel-path-symlink`: the path is judged by its lexical in-repo name first (`..` collapsed, links kept) and only a path that leaves the project returns None (`test_hooks_judge_symlinks_by_their_in_repo_name`).
- Important: commands/deploy.md:20 claimed the rehearsal leaves "the checkout, index and branch untouched", which reads as a safety guarantee the worktree does not give: objects, tags, other branches, remotes and anything outside git are shared and run for real (verified by the reviewer with `git tag` surviving `worktree remove`). Addressed by correcting the docs and spec to name exactly what is and is not isolated; the mechanic cannot do better without a clone, which would still share remotes.
- Nit: scripts/sdlc/deploy.py:87 rehearsal commits stay as dangling objects until gc. Documented in commands/deploy.md; not otherwise addressed.

## Compliance
- Nit: sdlc/dogfood-fixes-round-two/tdd.jsonl:1 three `red` entries were recorded before any `green` because all three steps' tests were written before the first implementation, so the steps were not the per-step red→green cycles plan.md describes. Accurate; recorded in plan.md Risks as a process slip.

Nits: 5 reported, 2 withheld. Requirements 1-7 confirmed by reviewer and verifier.
