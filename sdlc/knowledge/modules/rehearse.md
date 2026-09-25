---
type: Module
title: rehearse
description: "Graphify community 16: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py, sdlc/rehearsal-and-band-nits/intent.md, sdlc/rehear"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5fbfef41a758468b }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-19T23:30:10+10:00", digest: dbfb47118be6302a }
  - { id: test_maintain, resource: tests/test_maintain.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 5e6dbf325688ebe8 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/rehearsal-and-band-nits/intent.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/spec.md`
- `tests/test_deploy.py`
- `tests/test_maintain.py`

# Symbols
- rehearse() (plugin/scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (plugin/scripts/sdlc/deploy.py:L77)
- release_hit() (plugin/scripts/sdlc/hooks.py:L102)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (plugin/scripts/sdlc/hooks.py:L103)
- bands() (plugin/scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (plugin/scripts/sdlc/maintain.py:L55)
- run_git() (plugin/scripts/sdlc/project.py:L207)
- git() (plugin/scripts/sdlc/project.py:L211)
- Proposed outcome (sdlc/rehearsal-and-band-nits/intent.md:L17)
- Order of work (sdlc/rehearsal-and-band-nits/plan.md:L15)
- rehearsal-and-band-nits/spec.md (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Spec: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Design (sdlc/rehearsal-and-band-nits/spec.md:L13)
- Concerns (sdlc/rehearsal-and-band-nits/spec.md:L20)
- Open questions (sdlc/rehearsal-and-band-nits/spec.md:L23)
- Proof (sdlc/rehearsal-and-band-nits/spec.md:L26)
- Requirements (sdlc/rehearsal-and-band-nits/spec.md:L4)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)
- test_tier_rejects_unknown_side() (tests/test_maintain.py:L28)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-23.md)
- [project.py](/modules/project-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work-23.md)
- [test_deploy.py](/modules/test-deploy-py.md)
- [test_maintain.py](/modules/test-maintain-py.md)
- [watch](/modules/watch.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
