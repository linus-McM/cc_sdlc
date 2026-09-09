---
type: Module
title: read_json
description: "Graphify community 72: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:08:45Z" }
stale_after: "2026-09-23T02:08:45Z"
source_commit: 0794a80b6291964cd26930a809a8678a9c9b1311
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- plugin_version() (scripts/sdlc/knowledge.py:L574)
- load_graph() (scripts/sdlc/knowledge.py:L578)
- is_code() (scripts/sdlc/knowledge.py:L582)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L583)
- community_labels() (scripts/sdlc/knowledge.py:L589)
- communities() (scripts/sdlc/knowledge.py:L598)
- Graphify code communities big enough for a Module concept, with a stable slug… (scripts/sdlc/knowledge.py:L599)
- read_json() (scripts/sdlc/project.py:L191)

# Depends on
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
