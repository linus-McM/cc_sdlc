---
type: Module
title: Path
description: "Graphify community 79: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:52:55Z" }
stale_after: "2026-09-23T01:52:55Z"
source_commit: 06b2fae3d2c8f481dffdfc5f50898b33373030eb
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L200)
- state_path() (scripts/sdlc/knowledge.py:L209)
- read_state() (scripts/sdlc/knowledge.py:L213)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L214)
- write_state() (scripts/sdlc/knowledge.py:L221)
- write_ignore() (scripts/sdlc/knowledge.py:L374)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- bundle_present() (scripts/sdlc/knowledge.py:L383)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L384)
- pointer_present() (scripts/sdlc/knowledge.py:L393)
- graph_commit() (scripts/sdlc/knowledge.py:L455)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L463)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L464)
- artifacts_agree() (scripts/sdlc/knowledge.py:L475)
- behind() (scripts/sdlc/knowledge.py:L491)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L492)
- staleness() (scripts/sdlc/knowledge.py:L499)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L500)
- status() (scripts/sdlc/knowledge.py:L536)
- load_graph() (scripts/sdlc/knowledge.py:L568)
- community_labels() (scripts/sdlc/knowledge.py:L579)
- read_json() (scripts/sdlc/project.py:L173)

# Depends on
- [cfg](/modules/cfg.md)
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [run](/modules/run.md)

# Inferred
- [cli.py](/modules/cli-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
