---
type: Module
title: docs.py
description: "Graphify community 85: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c333272d4dfcf4c6 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/archify-stage-documentation/review.md`

# Symbols
- docs.py (plugin/scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (plugin/scripts/sdlc/docs.py:L1)
- mechanic() (plugin/scripts/sdlc/docs.py:L129)
- CLI handler for `docs <action> <stage>`: the skipped verdict comes before any… (plugin/scripts/sdlc/docs.py:L130)
- sources() (plugin/scripts/sdlc/docs.py:L151)
- sha256() (plugin/scripts/sdlc/docs.py:L155)
- source_bytes() (plugin/scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (plugin/scripts/sdlc/docs.py:L164)
- digests() (plugin/scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (plugin/scripts/sdlc/docs.py:L176)
- receipt_of() (plugin/scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (plugin/scripts/sdlc/docs.py:L188)
- render() (plugin/scripts/sdlc/docs.py:L212)
- check() (plugin/scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (plugin/scripts/sdlc/docs.py:L246)
- rel() (plugin/scripts/sdlc/project.py:L129)
- Compliance (sdlc/archify-stage-documentation/review.md:L15)

# Depends on
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [Order of work](/modules/order-of-work.md)
- [StepSkipped](/modules/stepskipped.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
