---
type: Module
title: read_json
description: "Graphify community 82: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:56Z" }
stale_after: "2026-09-23T00:28:56Z"
source_commit: e46d381e2f64fa96bbb6eee6115eba30499cfe2e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L200)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- plugin_version() (scripts/sdlc/knowledge.py:L564)
- load_graph() (scripts/sdlc/knowledge.py:L568)
- community_labels() (scripts/sdlc/knowledge.py:L579)
- read_json() (scripts/sdlc/project.py:L173)

# Depends on
- [fail](/modules/fail.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
