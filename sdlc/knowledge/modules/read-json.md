---
type: Module
title: read_json
description: "Graphify community 20: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/stages.py, plugin/scripts/sdlc/testing.py, sdlc/status-next-pointer/review.md, sdlc/status-nex"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:35:55+10:00", digest: d2d3493a1ed08434 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 3de65600923a55b5 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 68b187c7a3220c0b }
  - { id: review, resource: sdlc/status-next-pointer/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: f6fa7c95be7b4059 }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 21a434a2e5ea4acf }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/stages.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/status-next-pointer/review.md`
- `sdlc/status-next-pointer/spec.md`

# Symbols
- state() (plugin/scripts/sdlc/deploy.py:L17)
- production() (plugin/scripts/sdlc/deploy.py:L21)
- The feature's production deployments, oldest first. (plugin/scripts/sdlc/deploy.py:L22)
- released() (plugin/scripts/sdlc/deploy.py:L26)
- readiness() (plugin/scripts/sdlc/deploy.py:L30)
- Reasons the feature is not ready for any environment; empty when ready. (plugin/scripts/sdlc/deploy.py:L31)
- read_json() (plugin/scripts/sdlc/project.py:L250)
- next_for() (plugin/scripts/sdlc/stages.py:L97)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (plugin/scripts/sdlc/stages.py:L98)
- report() (plugin/scripts/sdlc/testing.py:L14)
- status-next-pointer/review.md (sdlc/status-next-pointer/review.md:L1)
- Review: Status next pointer (sdlc/status-next-pointer/review.md:L1)
- Compliance (sdlc/status-next-pointer/review.md:L11)
- Bugs (sdlc/status-next-pointer/review.md:L4)
- Security (sdlc/status-next-pointer/review.md:L8)
- Design (sdlc/status-next-pointer/spec.md:L13)

# Depends on
- [fail](/modules/fail.md)
- [git](/modules/git.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [build](/modules/build.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
