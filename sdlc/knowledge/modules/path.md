---
type: Module
title: Path
description: "Graphify community 72: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
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
- graph_commit() (scripts/sdlc/knowledge.py:L462)
- artifacts_agree() (scripts/sdlc/knowledge.py:L482)
- behind() (scripts/sdlc/knowledge.py:L498)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L499)
- staleness() (scripts/sdlc/knowledge.py:L506)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L507)
- load_graph() (scripts/sdlc/knowledge.py:L578)
- community_labels() (scripts/sdlc/knowledge.py:L589)
- index_lines() (scripts/sdlc/knowledge.py:L879)
- `* [Title](link) - description` per concept, sorted by title; sub-indexes link… (scripts/sdlc/knowledge.py:L880)
- write_indexes() (scripts/sdlc/knowledge.py:L886)
- read_json() (scripts/sdlc/project.py:L191)

# Depends on
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
