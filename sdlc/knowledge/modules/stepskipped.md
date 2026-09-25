---
type: Module
title: StepSkipped
description: "Graphify community 30: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/review.md"
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
- install_archify() (plugin/scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (plugin/scripts/sdlc/docs.py:L119)
- source_bytes() (plugin/scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (plugin/scripts/sdlc/docs.py:L164)
- validation() (plugin/scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (plugin/scripts/sdlc/docs.py:L200)
- count() (plugin/scripts/sdlc/docs.py:L204)
- documents() (plugin/scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (plugin/scripts/sdlc/docs.py:L280)
- This step does not apply here; later steps still run. (plugin/scripts/sdlc/project.py:L100)
- run_cmd() (plugin/scripts/sdlc/project.py:L195)
- Run an external tool without a shell; never raises on a non-zero exit. A… (plugin/scripts/sdlc/project.py:L196)
- StepSkipped (plugin/scripts/sdlc/project.py:L99)
- archify-stage-documentation/review.md (sdlc/archify-stage-documentation/review.md:L1)
- Review: Archify stage documentation (sdlc/archify-stage-documentation/review.md:L1)
- Security (sdlc/archify-stage-documentation/review.md:L11)
- Second pass (after review-fixes) (sdlc/archify-stage-documentation/review.md:L22)
- Bugs (sdlc/archify-stage-documentation/review.md:L4)

# Depends on
- [check](/modules/check.md)
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [read_json](/modules/read-json.md)

# Inferred
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-5.md)
- [Path](/modules/path.md)

# Features
- no feature plan names these files
