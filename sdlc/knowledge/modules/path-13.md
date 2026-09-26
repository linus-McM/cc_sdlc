---
type: Module
title: Path
description: "Graphify community 13: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- graph_path() (plugin/scripts/sdlc/knowledge.py:L192)
- skill_path() (plugin/scripts/sdlc/knowledge.py:L196)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)
- tool() (plugin/scripts/sdlc/knowledge.py:L237)
- install_skill() (plugin/scripts/sdlc/knowledge.py:L323)
- build_graph() (plugin/scripts/sdlc/knowledge.py:L354)
- bundle_present() (plugin/scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (plugin/scripts/sdlc/knowledge.py:L359)
- graph_commit() (plugin/scripts/sdlc/knowledge.py:L443)
- staleness() (plugin/scripts/sdlc/knowledge.py:L487)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L488)
- load_graph() (plugin/scripts/sdlc/knowledge.py:L559)
- community_labels() (plugin/scripts/sdlc/knowledge.py:L570)
- communities() (plugin/scripts/sdlc/knowledge.py:L579)
- Graphify code communities big enough for a Module concept, with a stable slug… (plugin/scripts/sdlc/knowledge.py:L580)

# Depends on
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [docs.py](/modules/docs-py.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
