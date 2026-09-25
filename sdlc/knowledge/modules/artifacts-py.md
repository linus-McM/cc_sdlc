---
type: Module
title: artifacts.py
description: "Graphify community 20: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- artifacts.py (plugin/scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (plugin/scripts/sdlc/artifacts.py:L1)
- matches() (plugin/scripts/sdlc/artifacts.py:L100)
- title() (plugin/scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (plugin/scripts/sdlc/artifacts.py:L35)
- sections() (plugin/scripts/sdlc/artifacts.py:L39)
- meta() (plugin/scripts/sdlc/artifacts.py:L49)
- status() (plugin/scripts/sdlc/artifacts.py:L58)
- validate() (plugin/scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (plugin/scripts/sdlc/artifacts.py:L63)
- glob_regex() (plugin/scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (plugin/scripts/sdlc/artifacts.py:L93)
- pr_body() (plugin/scripts/sdlc/deploy.py:L134)
- Changes to existing behaviour (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L270)

# Depends on
- [append_log](/modules/append-log.md)
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-5.md)
- [status](/modules/status.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [pathlib](/modules/pathlib.md)

# Features
- no feature plan names these files
