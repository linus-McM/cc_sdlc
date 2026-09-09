---
type: Module
title: Path
description: "Graphify community 89: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:33Z" }
stale_after: "2026-09-23T03:02:33Z"
source_commit: 7a6549e2e0a57fe6fe0b1257011d2e78bce58136
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L192)
- state_path() (scripts/sdlc/knowledge.py:L200)
- read_state() (scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L205)
- write_state() (scripts/sdlc/knowledge.py:L212)
- write_ignore() (scripts/sdlc/knowledge.py:L349)
- build_graph() (scripts/sdlc/knowledge.py:L354)
- bundle_present() (scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L359)
- graph_commit() (scripts/sdlc/knowledge.py:L439)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L447)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L448)
- artifacts_agree() (scripts/sdlc/knowledge.py:L459)
- behind() (scripts/sdlc/knowledge.py:L475)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L476)
- staleness() (scripts/sdlc/knowledge.py:L483)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L484)
- status() (scripts/sdlc/knowledge.py:L520)
- load_graph() (scripts/sdlc/knowledge.py:L555)
- community_labels() (scripts/sdlc/knowledge.py:L566)

# Depends on
- [cfg](/modules/cfg.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
