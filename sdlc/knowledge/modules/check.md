---
type: Module
title: check
description: "Graphify community 23: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c333272d4dfcf4c6 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/archify-stage-documentation/review.md`

# Symbols
- sha256() (plugin/scripts/sdlc/docs.py:L155)
- source_bytes() (plugin/scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (plugin/scripts/sdlc/docs.py:L164)
- digests() (plugin/scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (plugin/scripts/sdlc/docs.py:L176)
- check() (plugin/scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (plugin/scripts/sdlc/docs.py:L246)
- documents() (plugin/scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (plugin/scripts/sdlc/docs.py:L280)
- rel() (plugin/scripts/sdlc/project.py:L132)
- archify-stage-documentation/review.md (sdlc/archify-stage-documentation/review.md:L1)
- Review: Archify stage documentation (sdlc/archify-stage-documentation/review.md:L1)
- Compliance (sdlc/archify-stage-documentation/review.md:L15)
- Second pass (after review-fixes) (sdlc/archify-stage-documentation/review.md:L22)
- Bugs (sdlc/archify-stage-documentation/review.md:L4)

# Depends on
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [read_json](/modules/read-json.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build](/modules/build.md)
- [cfg](/modules/cfg.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-11.md)
- [packs.py](/modules/packs-py.md)
- [StepSkipped](/modules/stepskipped.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
