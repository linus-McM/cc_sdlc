---
type: Module
title: Order of work
description: "Graphify community 25: sdlc/dogfood-fixes-round-two/plan.md, sdlc/dogfood-fixes-round-two/spec.md, sdlc/rehearsal-and-band-nits/plan.md, sdlc/rehearsal-and-band-nits/review.md, sdlc/rehearsal-and-band"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: plan, resource: sdlc/dogfood-fixes-round-two/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 74b29c1ae00f8ef4 }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: review, resource: sdlc/rehearsal-and-band-nits/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 370e4dd8c100bf71 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `sdlc/dogfood-fixes-round-two/plan.md`
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/review.md`
- `sdlc/rehearsal-and-band-nits/spec.md`
- `tests/test_deploy.py`
- `tests/test_maintain.py`

# Symbols
- Order of work (sdlc/dogfood-fixes-round-two/plan.md:L16)
- Proof (sdlc/dogfood-fixes-round-two/spec.md:L25)
- rehearsal-and-band-nits/plan.md (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Plan: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/plan.md:L1)
- Order of work (sdlc/rehearsal-and-band-nits/plan.md:L15)
- Files that change (sdlc/rehearsal-and-band-nits/plan.md:L4)
- Risks (sdlc/rehearsal-and-band-nits/plan.md:L43)
- Proof (sdlc/rehearsal-and-band-nits/plan.md:L54)
- Bugs (sdlc/rehearsal-and-band-nits/review.md:L4)
- Proof (sdlc/rehearsal-and-band-nits/spec.md:L26)
- test_deploy_rehearse_runs_in_throwaway_worktree() (tests/test_deploy.py:L56)
- test_deploy_rehearse_needs_git() (tests/test_deploy.py:L66)
- test_deploy_rehearse_reports_leftover_worktree() (tests/test_deploy.py:L72)
- flaky() (tests/test_deploy.py:L75)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L28)
- test_tier_one_sided_bands_ignore_the_good_side() (tests/test_maintain.py:L33)

# Depends on
- [docs.py](/modules/docs-py.md)
- [git](/modules/git.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [conftest.py](/modules/conftest-py.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [Path](/modules/path.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
