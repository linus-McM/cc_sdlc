---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:22:28Z" }
stale_after: "2026-09-23T02:22:28Z"
source_commit: 596440e8a2a56052df06112cb01e32437adfaa8c
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 37c8f72da04d26bf }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 418f9277e7848a02 }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/project.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- The installed version as the step's detail (no subprocess); StepSkipped when… (scripts/sdlc/docs.py:L100)
- install_archify() (scripts/sdlc/docs.py:L110)
- docs_dir() (scripts/sdlc/docs.py:L125)
- sources() (scripts/sdlc/docs.py:L129)
- sha256() (scripts/sdlc/docs.py:L133)
- digests() (scripts/sdlc/docs.py:L137)
- Per-source sha256 plus one digest over `<path>\\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L138)
- receipt_of() (scripts/sdlc/docs.py:L149)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (scripts/sdlc/docs.py:L150)
- validation() (scripts/sdlc/docs.py:L161)
- One line from the receipt's `validation` block: `9/9 showcase, 0 errors, 0… (scripts/sdlc/docs.py:L162)
- render() (scripts/sdlc/docs.py:L168)
- check() (scripts/sdlc/docs.py:L200)
- The stage document exists, is the bytes Archify delivered, and was delivered… (scripts/sdlc/docs.py:L201)
- open() (scripts/sdlc/docs.py:L219)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L220)
- documents() (scripts/sdlc/docs.py:L235)
- One bullet per delivered stage document, with its receipt's validation line;… (scripts/sdlc/docs.py:L236)
- cfg() (scripts/sdlc/docs.py:L35)
- enabled() (scripts/sdlc/docs.py:L39)
- skill_dir() (scripts/sdlc/docs.py:L49)
- installed() (scripts/sdlc/docs.py:L53)
- version() (scripts/sdlc/docs.py:L57)
- version_tuple() (scripts/sdlc/docs.py:L65)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (scripts/sdlc/docs.py:L66)
- node_version() (scripts/sdlc/docs.py:L71)
- Major version of the `node` on PATH, or None when absent or unparseable. (scripts/sdlc/docs.py:L72)
- node_problem() (scripts/sdlc/docs.py:L80)
- Why Node cannot run Archify here, or None. (scripts/sdlc/docs.py:L81)
- tooling() (scripts/sdlc/docs.py:L89)
- Why Archify cannot run here, or None when it can. (scripts/sdlc/docs.py:L90)
- archify_present() (scripts/sdlc/docs.py:L99)
- rel() (scripts/sdlc/project.py:L119)
- read_json() (scripts/sdlc/project.py:L234)
- StepSkipped (scripts/sdlc/project.py:L89)
- This step does not apply here; later steps still run. (scripts/sdlc/project.py:L90)

# Depends on
- [Blocked](/modules/blocked.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
