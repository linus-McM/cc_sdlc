---
type: Module
title: read_json
description: "Graphify community 82: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:34Z" }
stale_after: "2026-09-23T00:28:34Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:18:34+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- plugin_version() (scripts/sdlc/knowledge.py:L532)
- load_graph() (scripts/sdlc/knowledge.py:L536)
- is_code() (scripts/sdlc/knowledge.py:L540)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L541)
- community_labels() (scripts/sdlc/knowledge.py:L547)
- communities() (scripts/sdlc/knowledge.py:L556)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L557)
- read_json() (scripts/sdlc/project.py:L173)

# Depends on
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
