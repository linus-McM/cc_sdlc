---
type: Module
title: Path
description: "Graphify community 75: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 7fce16edc7c795cc }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (scripts/sdlc/knowledge.py:L1030)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1031)
- graph_path() (scripts/sdlc/knowledge.py:L200)
- state_path() (scripts/sdlc/knowledge.py:L209)
- read_state() (scripts/sdlc/knowledge.py:L213)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L214)
- write_state() (scripts/sdlc/knowledge.py:L221)
- write_ignore() (scripts/sdlc/knowledge.py:L374)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- bundle_present() (scripts/sdlc/knowledge.py:L383)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L384)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- pointer_present() (scripts/sdlc/knowledge.py:L393)
- graph_commit() (scripts/sdlc/knowledge.py:L462)
- artifacts_agree() (scripts/sdlc/knowledge.py:L482)
- behind() (scripts/sdlc/knowledge.py:L498)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L499)
- staleness() (scripts/sdlc/knowledge.py:L506)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L507)
- load_graph() (scripts/sdlc/knowledge.py:L575)
- review_counts() (scripts/sdlc/knowledge.py:L680)
- feature_status() (scripts/sdlc/knowledge.py:L688)

# Depends on
- [cfg](/modules/cfg.md)
- [deploy.py](/modules/deploy-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [cli.py](/modules/cli-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
