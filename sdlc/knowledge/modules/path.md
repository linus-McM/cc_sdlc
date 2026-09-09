---
type: Module
title: Path
description: "Graphify community 72: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:22:28Z" }
stale_after: "2026-09-23T02:22:28Z"
source_commit: 596440e8a2a56052df06112cb01e32437adfaa8c
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- graph_path() (scripts/sdlc/knowledge.py:L192)
- state_path() (scripts/sdlc/knowledge.py:L200)
- read_state() (scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L205)
- write_state() (scripts/sdlc/knowledge.py:L212)
- install_graphify() (scripts/sdlc/knowledge.py:L319)
- write_ignore() (scripts/sdlc/knowledge.py:L349)
- build_graph() (scripts/sdlc/knowledge.py:L354)
- bundle_present() (scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L359)
- pointer_present() (scripts/sdlc/knowledge.py:L368)
- graph_commit() (scripts/sdlc/knowledge.py:L433)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L441)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L442)
- artifacts_agree() (scripts/sdlc/knowledge.py:L453)
- behind() (scripts/sdlc/knowledge.py:L469)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L470)
- staleness() (scripts/sdlc/knowledge.py:L477)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L478)
- status() (scripts/sdlc/knowledge.py:L514)
- load_graph() (scripts/sdlc/knowledge.py:L549)
- review_counts() (scripts/sdlc/knowledge.py:L654)
- feature_status() (scripts/sdlc/knowledge.py:L662)
- feature_concepts() (scripts/sdlc/knowledge.py:L674)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [band_concepts](/modules/band-concepts.md)
- [cfg](/modules/cfg.md)
- [conftest.py](/modules/conftest-py.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
