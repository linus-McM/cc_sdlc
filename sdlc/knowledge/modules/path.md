---
type: Module
title: Path
description: "Graphify community 79: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:59:02Z" }
stale_after: "2026-09-23T01:59:02Z"
source_commit: e0523eb3d807827869c761a89aea8117eb781e36
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L200)
- skill_path() (scripts/sdlc/knowledge.py:L204)
- tool() (scripts/sdlc/knowledge.py:L246)
- StepFailed (scripts/sdlc/knowledge.py:L324)
- ran() (scripts/sdlc/knowledge.py:L332)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/knowledge.py:L333)
- install_graphify() (scripts/sdlc/knowledge.py:L344)
- install_skill() (scripts/sdlc/knowledge.py:L348)
- write_ignore() (scripts/sdlc/knowledge.py:L374)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- bundle_present() (scripts/sdlc/knowledge.py:L383)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L384)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- pointer_present() (scripts/sdlc/knowledge.py:L393)
- graph_commit() (scripts/sdlc/knowledge.py:L455)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L463)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L464)
- artifacts_agree() (scripts/sdlc/knowledge.py:L475)
- behind() (scripts/sdlc/knowledge.py:L491)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L492)
- staleness() (scripts/sdlc/knowledge.py:L499)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L500)
- load_graph() (scripts/sdlc/knowledge.py:L568)
- community_labels() (scripts/sdlc/knowledge.py:L579)

# Depends on
- [project.py](/modules/project-py.md)
- [read_state](/modules/read-state.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
