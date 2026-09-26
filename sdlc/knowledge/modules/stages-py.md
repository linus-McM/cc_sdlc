---
type: Module
title: stages.py
description: "Graphify community 22: plugin/commands/deploy.md, plugin/commands/maintain.md, plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/stages.py, sdlc/graphify-and-okf-knowle"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: deploy, resource: plugin/commands/deploy.md, last_modified: "2026-09-24T11:36:09+10:00", digest: d0459d52d6b53867 }
  - { id: maintain, resource: plugin/commands/maintain.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 9d250885cd480f68 }
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 6cee45ef1d7a0ebb }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 79822cdce593996c }
  - { id: plan, resource: sdlc/graphify-and-okf-knowledge-base-integration/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 31d2c88298eefdb1 }
---

# Files
- `plugin/commands/deploy.md`
- `plugin/commands/maintain.md`
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/stages.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/plan.md`

# Symbols
- deploy.md (plugin/commands/deploy.md:L1)
- pr (plugin/commands/deploy.md:L14)
- readiness <env> (plugin/commands/deploy.md:L17)
- check <env> (plugin/commands/deploy.md:L20)
- rehearse (plugin/commands/deploy.md:L26)
- docs  (the stage document; required before `deploy record`) (plugin/commands/deploy.md:L29)
- record <env> (plugin/commands/deploy.md:L32)
- maintain.md (plugin/commands/maintain.md:L1)
- watch (plugin/commands/maintain.md:L16)
- docs  (the bands document; never gates a watch) (plugin/commands/maintain.md:L22)
- propose <metric> (plugin/commands/maintain.md:L25)
- lesson "<text>" (plugin/commands/maintain.md:L28)
- meta() (plugin/scripts/sdlc/artifacts.py:L49)
- status() (plugin/scripts/sdlc/artifacts.py:L58)
- lifecycle() (plugin/scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (plugin/scripts/sdlc/cli.py:L19)
- stages.py (plugin/scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (plugin/scripts/sdlc/stages.py:L1)
- status() (plugin/scripts/sdlc/stages.py:L105)
- prerequisite() (plugin/scripts/sdlc/stages.py:L18)
- accepted() (plugin/scripts/sdlc/stages.py:L27)
- gated() (plugin/scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (plugin/scripts/sdlc/stages.py:L33)
- create_feature() (plugin/scripts/sdlc/stages.py:L42)
- new() (plugin/scripts/sdlc/stages.py:L53)
- check() (plugin/scripts/sdlc/stages.py:L75)
- next_for() (plugin/scripts/sdlc/stages.py:L95)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (plugin/scripts/sdlc/stages.py:L96)
- graphify-and-okf-knowledge-base-integration/plan.md (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L1)
- Plan: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L1)
- Risks (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L206)
- Proof (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L232)
- Files that change (sdlc/graphify-and-okf-knowledge-base-integration/plan.md:L4)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [cli.py](/modules/cli-py.md)
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-5.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [render](/modules/render.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)
- [rehearse](/modules/rehearse.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
