---
type: Module
title: watch
description: "Graphify community 16: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/spec.md, sdlc/rehearsa"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5fbfef41a758468b }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: pr-body, resource: sdlc/rehearsal-and-band-nits/pr-body.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94cd9c8ea7275a8 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/intent.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/pr-body.md`
- `sdlc/rehearsal-and-band-nits/spec.md`

# Symbols
- rehearse() (plugin/scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (plugin/scripts/sdlc/deploy.py:L77)
- release_hit() (plugin/scripts/sdlc/hooks.py:L102)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (plugin/scripts/sdlc/hooks.py:L103)
- tier() (plugin/scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (plugin/scripts/sdlc/maintain.py:L25)
- beyond() (plugin/scripts/sdlc/maintain.py:L41)
- bands() (plugin/scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (plugin/scripts/sdlc/maintain.py:L55)
- readings() (plugin/scripts/sdlc/maintain.py:L64)
- watch() (plugin/scripts/sdlc/maintain.py:L72)
- run_git() (plugin/scripts/sdlc/project.py:L207)
- git() (plugin/scripts/sdlc/project.py:L211)
- Design (sdlc/dogfood-fixes-round-two/spec.md:L13)
- rehearsal-and-band-nits/intent.md (sdlc/rehearsal-and-band-nits/intent.md:L1)
- Intent: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/intent.md:L1)
- Proposed outcome (sdlc/rehearsal-and-band-nits/intent.md:L17)
- Affected users and systems (sdlc/rehearsal-and-band-nits/intent.md:L29)
- Open questions (sdlc/rehearsal-and-band-nits/intent.md:L37)
- Problem (sdlc/rehearsal-and-band-nits/intent.md:L4)
- Order of work (sdlc/rehearsal-and-band-nits/plan.md:L15)
- Why (sdlc/rehearsal-and-band-nits/pr-body.md:L3)
- Design (sdlc/rehearsal-and-band-nits/spec.md:L13)
- Requirements (sdlc/rehearsal-and-band-nits/spec.md:L4)

# Depends on
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [rel_path](/modules/rel-path.md)
- [StepSkipped](/modules/stepskipped.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [rel_path](/modules/rel-path.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Features
- no feature plan names these files
