---
type: Module
title: Path
description: "Graphify community 72: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:35:57Z" }
stale_after: "2026-09-22T22:35:57Z"
source_commit: c6f9a22e23b0bee7134aa1e1709c5feef8673f82
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:35:54+10:00", digest: 5ed472fa5f0e7275 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L187)
- state_path() (scripts/sdlc/knowledge.py:L196)
- read_state() (scripts/sdlc/knowledge.py:L200)
- write_state() (scripts/sdlc/knowledge.py:L204)
- write_ignore() (scripts/sdlc/knowledge.py:L352)
- build_graph() (scripts/sdlc/knowledge.py:L357)
- bundle_present() (scripts/sdlc/knowledge.py:L361)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L362)
- pointer_present() (scripts/sdlc/knowledge.py:L371)
- graph_commit() (scripts/sdlc/knowledge.py:L431)
- artifacts_agree() (scripts/sdlc/knowledge.py:L451)
- behind() (scripts/sdlc/knowledge.py:L467)
- staleness() (scripts/sdlc/knowledge.py:L474)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L475)
- load_graph() (scripts/sdlc/knowledge.py:L536)
- community_labels() (scripts/sdlc/knowledge.py:L547)
- communities() (scripts/sdlc/knowledge.py:L556)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L557)
- concepts_for() (scripts/sdlc/knowledge.py:L982)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L983)
- read_json() (scripts/sdlc/project.py:L173)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
