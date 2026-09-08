---
type: Module
title: artifacts.py
description: "Graphify community 68: scripts/sdlc/artifacts.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:28:38Z" }
stale_after: "2026-09-22T22:28:38Z"
source_commit: 639850475d5980649e4dd44aed6fdad796bd7f4c
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T07:44:17+10:00", digest: 3e063b545e7dd897 }
---

# Files
- `scripts/sdlc/artifacts.py`

# Symbols
- artifacts.py (scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (scripts/sdlc/artifacts.py:L1)
- title() (scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (scripts/sdlc/artifacts.py:L35)
- sections() (scripts/sdlc/artifacts.py:L39)
- set_section() (scripts/sdlc/artifacts.py:L44)
- set_meta() (scripts/sdlc/artifacts.py:L54)
- validate() (scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (scripts/sdlc/artifacts.py:L63)
- list_items() (scripts/sdlc/artifacts.py:L74)
- Paths from a bulleted or comma-separated section body, annotations stripped. (scripts/sdlc/artifacts.py:L75)
- render() (scripts/sdlc/artifacts.py:L83)
- glob_regex() (scripts/sdlc/artifacts.py:L87)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (scripts/sdlc/artifacts.py:L88)
- matches() (scripts/sdlc/artifacts.py:L95)

# Depends on
- [knowledge.py](/modules/knowledge-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
