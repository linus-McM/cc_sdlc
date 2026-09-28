---
type: Module
title: pathlib
description: "Graphify community 6: plugin/scripts/sdlc/__init__.py, plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/stages.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: __init__, resource: plugin/scripts/sdlc/__init__.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 0a6aea3cd6840dbf }
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:35:55+10:00", digest: d2d3493a1ed08434 }
  - { id: stages, resource: plugin/scripts/sdlc/stages.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 3de65600923a55b5 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 68b187c7a3220c0b }
---

# Files
- `plugin/scripts/sdlc/__init__.py`
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/stages.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- __init__.py (plugin/scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (plugin/scripts/sdlc/__init__.py:L1)
- artifacts.py (plugin/scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (plugin/scripts/sdlc/artifacts.py:L1)
- matches() (plugin/scripts/sdlc/artifacts.py:L100)
- meta() (plugin/scripts/sdlc/artifacts.py:L49)
- glob_regex() (plugin/scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (plugin/scripts/sdlc/artifacts.py:L93)
- deploy.py (plugin/scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (plugin/scripts/sdlc/deploy.py:L1)
- stages.py (plugin/scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (plugin/scripts/sdlc/stages.py:L1)
- prerequisite() (plugin/scripts/sdlc/stages.py:L19)
- new() (plugin/scripts/sdlc/stages.py:L54)
- testing.py (plugin/scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (plugin/scripts/sdlc/testing.py:L1)

# Depends on
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cfg](/modules/cfg.md)
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-44.md)
- [packs.py](/modules/packs-py.md)
- [pre_bash](/modules/pre-bash.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [watch](/modules/watch.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
