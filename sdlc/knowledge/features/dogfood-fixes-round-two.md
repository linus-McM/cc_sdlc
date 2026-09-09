---
type: Feature
title: Dogfood fixes round two
description: "Three rough edges surfaced while the first two features went through the pipeline:"
resource: sdlc/dogfood-fixes-round-two
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:18:38Z" }
stale_after: "2026-09-23T00:18:38Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: intent, resource: sdlc/dogfood-fixes-round-two/intent.md, last_modified: "2026-09-08T13:05:24+10:00", digest: 5054c3634f2f4d06 }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-08T13:19:02+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: plan, resource: sdlc/dogfood-fixes-round-two/plan.md, last_modified: "2026-09-08T13:19:02+10:00", digest: 74b29c1ae00f8ef4 }
  - { id: review, resource: sdlc/dogfood-fixes-round-two/review.md, last_modified: "2026-09-08T13:19:02+10:00", digest: a4e885eac6b6172a }
---

# Problem
Three rough edges surfaced while the first two features went through the pipeline:
1. `maintain watch` uses two-sided Western Electric rules, so a metric that improves
   (`tests_passed` rising from 61 to 66) trips a tier 3 breach and would propose an incident.
2. `deploy rehearse` runs `deploy.rollback` in the working checkout. On this repo the command is
   `git revert --no-edit HEAD`, so the rehearsal really reverted the last commit twice and had to be
   undone by hand with `git reset --hard HEAD~1`.
3. The post-edit plan-sync hook flags files outside the repository (a scratchpad script) because
   `rel_path` falls back to the absolute path when the file is not under the project root.

# Outcome
1. `sdlc/bands.toml` accepts `bad = "low" | "high" | "both"` per metric (default `both`); only
   points on the bad side count toward a tier. `tests_passed` with `bad = "low"` stays at tier 0.
2. `deploy rehearse` runs the rollback command in a temporary detached git worktree of HEAD and
   removes it afterwards; the branch, index and working tree of the project are untouched.
3. Edits to paths outside the project root are ignored by both edit hooks.

# Requirements
1. `maintain.tier(values, window, bad="both")` counts a point toward a rule only when it lies on the bad side: `bad = "high"` ignores points below the mean, `bad = "low"` ignores points above it, `"both"` is today's behaviour. The zero-variance case follows the same rule.
2. `sdlc/bands.toml` accepts `bad` per metric; `watch` passes it to `tier`; an unknown value fails with a `Blocked` verdict naming the metric.
3. This repo's `sdlc/bands.toml` declares `tests_passed` with `bad = "low"`, and `maintain watch` on the current readings reports tier 0.
4. `deploy rehearse` runs `deploy.rollback` inside a temporary detached git worktree of HEAD (`git worktree add --detach`), records `cmd`, `exit`, `tail` and `ts` in deploy.json as today, and removes the worktree afterwards even when the command fails. HEAD, the index and the working tree of the project are unchanged after a rehearsal whose rollback is `git revert --no-edit HEAD`. Not isolated, and documented as such: the object store, tags, other branches, remotes and anything outside git.
5. When the project is not a git checkout, `deploy rehearse` fails with a `Blocked` verdict saying a git checkout is needed.
6. `hooks.rel_path` judges a path by its lexical name inside the project (`..` collapsed, symlinks not followed) and falls back to the resolved path; only a path that leaves the project returns None, so `pre_edit` and `post_edit` stay silent for outside edits but still guard an in-repo symlink to an outside file.
7. `templates/bands.toml` documents `bad`; `commands/maintain.md` mentions it; `commands/deploy.md` says the rehearsal runs in a throwaway worktree.

# Files
- `commands/deploy.md`
- `commands/maintain.md`
- `scripts/sdlc/deploy.py` in [deploy.py](/modules/deploy-py.md)
- `scripts/sdlc/hooks.py` in [status](/modules/status.md)
- `scripts/sdlc/maintain.py` in [maintain.py](/modules/maintain-py.md)
- `sdlc/bands.toml`
- `templates/bands.toml`
- `tests/test_deploy.py` in [run](/modules/run.md)
- `tests/test_hooks.py` in [test_hooks.py](/modules/test-hooks-py.md)
- `tests/test_maintain.py` in [test_maintain.py](/modules/test-maintain-py.md)

# Review
- Important: 2, Nit: 5

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev, staging
