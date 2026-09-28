---
type: Module
title: git
description: "Graphify community 2: plugin/README.md, plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/testing.py, sdlc/archify-stage-documentation"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-29T08:42:51+10:00", digest: c7e6b88df8690ad4 }
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 68b187c7a3220c0b }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/testing.py`
- `sdlc/archify-stage-documentation/plan.md`

# Symbols
- plugin/README.md (plugin/README.md:L1)
- sdlc — AI-native SDLC plugin for Claude Code (plugin/README.md:L1)
- Guardrails (hooks/hooks.json) (plugin/README.md:L16)
- Checkpoints (plugin/README.md:L23)
- Stage documents (Archify) (plugin/README.md:L57)
- Install (plugin/README.md:L76)
- sections() (plugin/scripts/sdlc/artifacts.py:L39)
- validate() (plugin/scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (plugin/scripts/sdlc/artifacts.py:L63)
- planned_files() (plugin/scripts/sdlc/build.py:L57)
- sync() (plugin/scripts/sdlc/build.py:L66)
- ensure_config() (plugin/scripts/sdlc/project.py:L168)
- git() (plugin/scripts/sdlc/project.py:L214)
- head_commit() (plugin/scripts/sdlc/project.py:L218)
- author() (plugin/scripts/sdlc/project.py:L222)
- changed_files() (plugin/scripts/sdlc/project.py:L226)
- Staged, unstaged and untracked paths in one git call, limited to `paths` when… (plugin/scripts/sdlc/project.py:L227)
- findings() (plugin/scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (plugin/scripts/sdlc/testing.py:L56)
- review() (plugin/scripts/sdlc/testing.py:L66)
- The test stage's exit: valid findings plus a fresh stage document. (plugin/scripts/sdlc/testing.py:L67)
- Risks (sdlc/archify-stage-documentation/plan.md:L144)

# Depends on
- [cfg](/modules/cfg.md)
- [check](/modules/check.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work.md)
- [packs.py](/modules/packs-py.md)
- [select](/modules/select.md)
- [watch](/modules/watch.md)
- [workflows.py](/modules/workflows-py.md)

# Inferred
- [accept](/modules/accept.md)
- [bootstrap](/modules/bootstrap.md)
- [build](/modules/build.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [maintain.py](/modules/maintain-py.md)
- [packs.py](/modules/packs-py.md)
- [StepSkipped](/modules/stepskipped.md)
- [watch](/modules/watch.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
