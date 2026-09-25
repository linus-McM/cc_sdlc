---
type: Module
title: docs.py
description: "Graphify community 1: docs/knowledge-measurement.md, plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py, sdlc/archify-stage-documentation/plan.md, sdlc/archify"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: knowledge-measurement, resource: docs/knowledge-measurement.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 873b51012167b471 }
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c333272d4dfcf4c6 }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
---

# Files
- `docs/knowledge-measurement.md`
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/archify-stage-documentation/plan.md`
- `sdlc/archify-stage-documentation/review.md`
- `sdlc/archify-stage-documentation/spec.md`

# Symbols
- knowledge-measurement.md (docs/knowledge-measurement.md:L1)
- Knowledge layer token measurement (docs/knowledge-measurement.md:L1)
- After a rename and a deletion (docs/knowledge-measurement.md:L20)
- What the numbers say (docs/knowledge-measurement.md:L33)
- Same commit (this repo at 6398504: 159 files, 46 concepts, 697 graph nodes) (docs/knowledge-measurement.md:L9)
- docs.py (plugin/scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (plugin/scripts/sdlc/docs.py:L1)
- archify_present() (plugin/scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (plugin/scripts/sdlc/docs.py:L108)
- install_archify() (plugin/scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (plugin/scripts/sdlc/docs.py:L119)
- mechanic() (plugin/scripts/sdlc/docs.py:L129)
- CLI handler for `docs <action> <stage>`: the skipped verdict comes before any… (plugin/scripts/sdlc/docs.py:L130)
- handler() (plugin/scripts/sdlc/docs.py:L132)
- docs_dir() (plugin/scripts/sdlc/docs.py:L147)
- sources() (plugin/scripts/sdlc/docs.py:L151)
- sha256() (plugin/scripts/sdlc/docs.py:L155)
- source_bytes() (plugin/scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (plugin/scripts/sdlc/docs.py:L164)
- digests() (plugin/scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (plugin/scripts/sdlc/docs.py:L176)
- receipt_of() (plugin/scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (plugin/scripts/sdlc/docs.py:L188)
- validation() (plugin/scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (plugin/scripts/sdlc/docs.py:L200)
- count() (plugin/scripts/sdlc/docs.py:L204)
- render() (plugin/scripts/sdlc/docs.py:L212)
- check() (plugin/scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (plugin/scripts/sdlc/docs.py:L246)
- open() (plugin/scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (plugin/scripts/sdlc/docs.py:L265)
- documents() (plugin/scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (plugin/scripts/sdlc/docs.py:L280)
- cfg() (plugin/scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (plugin/scripts/sdlc/docs.py:L39)
- enabled() (plugin/scripts/sdlc/docs.py:L47)
- skill_dir() (plugin/scripts/sdlc/docs.py:L57)
- installed() (plugin/scripts/sdlc/docs.py:L61)
- version() (plugin/scripts/sdlc/docs.py:L65)
- node_version() (plugin/scripts/sdlc/docs.py:L79)
- Major version of the `node` on PATH, or None when absent or unparseable. (plugin/scripts/sdlc/docs.py:L80)
- node_problem() (plugin/scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (plugin/scripts/sdlc/docs.py:L89)
- tooling() (plugin/scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (plugin/scripts/sdlc/docs.py:L98)
- This step does not apply here; later steps still run. (plugin/scripts/sdlc/project.py:L100)
- rel() (plugin/scripts/sdlc/project.py:L129)
- run_cmd() (plugin/scripts/sdlc/project.py:L195)
- Run an external tool without a shell; never raises on a non-zero exit. A… (plugin/scripts/sdlc/project.py:L196)
- StepSkipped (plugin/scripts/sdlc/project.py:L99)
- review() (plugin/scripts/sdlc/testing.py:L66)
- The test stage's exit: valid findings plus a fresh stage document. (plugin/scripts/sdlc/testing.py:L67)
- Risks (sdlc/archify-stage-documentation/plan.md:L144)
- archify-stage-documentation/review.md (sdlc/archify-stage-documentation/review.md:L1)
- Review: Archify stage documentation (sdlc/archify-stage-documentation/review.md:L1)
- Security (sdlc/archify-stage-documentation/review.md:L11)
- Compliance (sdlc/archify-stage-documentation/review.md:L15)
- Second pass (after review-fixes) (sdlc/archify-stage-documentation/review.md:L22)
- Bugs (sdlc/archify-stage-documentation/review.md:L4)
- Requirements (sdlc/archify-stage-documentation/spec.md:L4)
- Design (sdlc/archify-stage-documentation/spec.md:L96)

# Depends on
- [Blocked](/modules/blocked.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [Components](/modules/components.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [pathlib](/modules/pathlib.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [status](/modules/status.md)
- [watch](/modules/watch.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
