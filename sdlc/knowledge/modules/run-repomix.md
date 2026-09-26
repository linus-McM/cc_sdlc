---
type: Module
title: run_repomix
description: "Graphify community 72: plugin/scripts/sdlc/packs.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
---

# Files
- `plugin/scripts/sdlc/packs.py`

# Symbols
- ladder() (plugin/scripts/sdlc/packs.py:L312)
- Step down the ladder, recording every rung tried with its tokens and dropped… (plugin/scripts/sdlc/packs.py:L313)
- run_repomix() (plugin/scripts/sdlc/packs.py:L373)
- Pack `files` into `out` with the plugin's config (secret check forced on); the… (plugin/scripts/sdlc/packs.py:L374)
- suspicious() (plugin/scripts/sdlc/packs.py:L388)
- Files Repomix's secret check flagged, read from its Security Check block only… (plugin/scripts/sdlc/packs.py:L389)
- scan_output() (plugin/scripts/sdlc/packs.py:L401)
- Refuse unless the output holds exactly the requested files; verdicts name… (plugin/scripts/sdlc/packs.py:L402)

# Depends on
- [fail](/modules/fail.md)
- [git](/modules/git.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
