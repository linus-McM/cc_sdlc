---
type: Module
title: pathlib
description: "Graphify community 20: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- artifacts.py (plugin/scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (plugin/scripts/sdlc/artifacts.py:L1)
- matches() (plugin/scripts/sdlc/artifacts.py:L100)
- sections() (plugin/scripts/sdlc/artifacts.py:L39)
- set_section() (plugin/scripts/sdlc/artifacts.py:L44)
- validate() (plugin/scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (plugin/scripts/sdlc/artifacts.py:L63)
- glob_regex() (plugin/scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (plugin/scripts/sdlc/artifacts.py:L93)
- deploy.py (plugin/scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (plugin/scripts/sdlc/deploy.py:L1)
- testing.py (plugin/scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (plugin/scripts/sdlc/testing.py:L1)

# Depends on
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-5.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [render](/modules/render.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
