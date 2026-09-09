---
type: Feature
title: Rehearsal and band nits
description: "Five nits left open by the review of dogfood-fixes-round-two:"
resource: sdlc/rehearsal-and-band-nits
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-08T15:54:44+10:00", digest: 5fbfef41a758468b }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-08T15:54:44+10:00", digest: b81cd9d3882a7703 }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-08T15:54:44+10:00", digest: 688912ed38722c04 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-08T15:54:44+10:00", digest: 370e4dd8c100bf71 }
---

# Problem
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

# Outcome
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

# Requirements
1. `project.run_git(root, *args)` returns the `subprocess.CompletedProcess`; `project.git` is unchanged in signature and behaviour (stdout, trailing newline stripped).
2. `deploy.rehearse` fails with a `Blocked` whose reason contains git's stderr when `git worktree add` exits non-zero (no git checkout, no commits).
3. When `git worktree remove` exits non-zero after the rollback ran, `rehearse` records the rollback result in deploy.json with a `leftover` note (git's stderr and a `git worktree prune` hint; the temp directory itself is already gone, only the `.git/worktrees` entry survives), then fails with that note as the reason. A project path missing at HEAD (uncommitted subdirectory) is refused with a verdict before the rollback runs, and the worktree is removed. A failed rollback still owns the verdict when both fail.
4. The rollback runs with cwd = worktree joined with `git rev-parse --show-prefix` of the project root; at the repo top level the prefix is empty and cwd is the worktree itself.
5. Dangling rehearsal commits are accepted behaviour, documented in `commands/deploy.md` as pruned by git's own gc; no code change.
6. `maintain.bands` (the config parser) is the single owner of the `bad` check and raises a `Blocked` naming the metric; `tier` stays a pure numeric function and raises `KeyError` for a programming error. Revised during `/simplify` from "tier raises Blocked": two owners for one config key was the smell.
7. `hooks.release_hit` matches env tokens only against environments at the `gate` tier; `prod` is no longer a built-in alias. README and the hook docstring say so.

# Files
- `README.md`
- `commands/deploy.md`
- `scripts/sdlc/deploy.py` in [deploy.py](/modules/deploy-py.md)
- `scripts/sdlc/hooks.py` in [hooks.py](/modules/hooks-py.md)
- `scripts/sdlc/maintain.py` in [maintain.py](/modules/maintain-py.md)
- `scripts/sdlc/project.py` in [cli.py](/modules/cli-py.md)
- `tests/test_deploy.py` in [test_deploy.py](/modules/test-deploy-py.md)
- `tests/test_hooks.py` in [test_hooks.py](/modules/test-hooks-py.md)
- `tests/test_maintain.py` in [test_maintain.py](/modules/test-maintain-py.md)

# Review
- Important: 1, Nit: 5

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev, staging

# Documents
- none
