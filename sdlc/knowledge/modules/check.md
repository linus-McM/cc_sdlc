---
type: Module
title: check
description: "Graphify community 85: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/review.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
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
- mechanic() (plugin/scripts/sdlc/docs.py:L129)
- CLI handler for `docs <action> <stage>`: the skipped verdict comes before any… (plugin/scripts/sdlc/docs.py:L130)
- handler() (plugin/scripts/sdlc/docs.py:L132)
- sha256() (plugin/scripts/sdlc/docs.py:L155)
- digests() (plugin/scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (plugin/scripts/sdlc/docs.py:L176)
- check() (plugin/scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (plugin/scripts/sdlc/docs.py:L246)
- rel() (plugin/scripts/sdlc/project.py:L129)
- Compliance (sdlc/archify-stage-documentation/review.md:L15)

# Depends on
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [accept](/modules/accept.md)
- [Order of work](/modules/order-of-work.md)

# Features
- no feature plan names these files
