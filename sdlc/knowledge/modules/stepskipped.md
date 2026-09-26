---
type: Module
title: StepSkipped
description: "Graphify community 30: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/plan.md, sdlc/archify-stage-documentation/review.md, sdlc/archify-stage-documentati"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c333272d4dfcf4c6 }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/archify-stage-documentation/plan.md`
- `sdlc/archify-stage-documentation/review.md`
- `sdlc/archify-stage-documentation/spec.md`

# Symbols
- archify_present() (plugin/scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (plugin/scripts/sdlc/docs.py:L108)
- install_archify() (plugin/scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (plugin/scripts/sdlc/docs.py:L119)
- handler() (plugin/scripts/sdlc/docs.py:L132)
- validation() (plugin/scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (plugin/scripts/sdlc/docs.py:L200)
- count() (plugin/scripts/sdlc/docs.py:L204)
- enabled() (plugin/scripts/sdlc/docs.py:L47)
- version() (plugin/scripts/sdlc/docs.py:L65)
- This step does not apply here; later steps still run. (plugin/scripts/sdlc/project.py:L100)
- StepFailed (plugin/scripts/sdlc/project.py:L95)
- An install step exited non-zero or left its expected result missing. (plugin/scripts/sdlc/project.py:L96)
- StepSkipped (plugin/scripts/sdlc/project.py:L99)
- Risks (sdlc/archify-stage-documentation/plan.md:L144)
- archify-stage-documentation/review.md (sdlc/archify-stage-documentation/review.md:L1)
- Review: Archify stage documentation (sdlc/archify-stage-documentation/review.md:L1)
- Security (sdlc/archify-stage-documentation/review.md:L11)
- Second pass (after review-fixes) (sdlc/archify-stage-documentation/review.md:L22)
- Bugs (sdlc/archify-stage-documentation/review.md:L4)
- Design (sdlc/archify-stage-documentation/spec.md:L96)

# Depends on
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
