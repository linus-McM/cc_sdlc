---
type: Module
title: watch
description: "Graphify community 16: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/intent.md, sdlc/dogfood-fixes-round-two/plan.md, sdl"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:35:55+10:00", digest: d2d3493a1ed08434 }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: intent, resource: sdlc/dogfood-fixes-round-two/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5054c3634f2f4d06 }
  - { id: plan, resource: sdlc/dogfood-fixes-round-two/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 74b29c1ae00f8ef4 }
  - { id: review, resource: sdlc/dogfood-fixes-round-two/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: a4e885eac6b6172a }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 5fbfef41a758468b }
  - { id: plan, resource: sdlc/rehearsal-and-band-nits/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 688912ed38722c04 }
  - { id: pr-body, resource: sdlc/rehearsal-and-band-nits/pr-body.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94cd9c8ea7275a8 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/intent.md`
- `sdlc/dogfood-fixes-round-two/plan.md`
- `sdlc/dogfood-fixes-round-two/review.md`
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/intent.md`
- `sdlc/rehearsal-and-band-nits/plan.md`
- `sdlc/rehearsal-and-band-nits/pr-body.md`
- `sdlc/rehearsal-and-band-nits/spec.md`

# Symbols
- rehearse() (plugin/scripts/sdlc/deploy.py:L81)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (plugin/scripts/sdlc/deploy.py:L82)
- tier() (plugin/scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (plugin/scripts/sdlc/maintain.py:L25)
- beyond() (plugin/scripts/sdlc/maintain.py:L41)
- bands() (plugin/scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (plugin/scripts/sdlc/maintain.py:L55)
- watch() (plugin/scripts/sdlc/maintain.py:L72)
- run_git() (plugin/scripts/sdlc/project.py:L210)
- Affected users and systems (sdlc/dogfood-fixes-round-two/intent.md:L21)
- Risks (sdlc/dogfood-fixes-round-two/plan.md:L40)
- Bugs (sdlc/dogfood-fixes-round-two/review.md:L4)
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
- [build](/modules/build.md)
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [pre_bash](/modules/pre-bash.md)
- [select](/modules/select.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
