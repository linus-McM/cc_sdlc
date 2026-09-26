---
type: Module
title: findings
description: "Graphify community 94: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T15:51:45+10:00", digest: 68b187c7a3220c0b }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- validate() (plugin/scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (plugin/scripts/sdlc/artifacts.py:L63)
- count() (plugin/scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (plugin/scripts/sdlc/testing.py:L51)
- findings() (plugin/scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (plugin/scripts/sdlc/testing.py:L56)

# Depends on
- [fail](/modules/fail.md)
- [review](/modules/review.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
