---
type: Module
title: cfg
description: "Graphify community 59: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:16:29Z" }
stale_after: "2026-10-10T06:16:29Z"
source_commit: def844e9ac23d4fb2eaffa6f82398a364dfbbac4
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (plugin/scripts/sdlc/knowledge.py:L1015)
- Project-relative module concept paths describing `rel`, from the file map the… (plugin/scripts/sdlc/knowledge.py:L1016)
- cfg() (plugin/scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (plugin/scripts/sdlc/knowledge.py:L175)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)

# Depends on
- [check](/modules/check.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [publish](/modules/publish.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
