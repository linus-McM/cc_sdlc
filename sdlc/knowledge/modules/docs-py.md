---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:01:32Z" }
stale_after: "2026-09-23T02:01:32Z"
source_commit: d8d61950c58abafa13a30ef68be4741e547839ef
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T11:58:59+10:00", digest: b1ccc5da69ea4135 }
---

# Files
- `scripts/sdlc/docs.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- target() (scripts/sdlc/docs.py:L101)
- The feature the document belongs to; maintain documents belong to the project,… (scripts/sdlc/docs.py:L102)
- docs_dir() (scripts/sdlc/docs.py:L106)
- sources() (scripts/sdlc/docs.py:L110)
- rel() (scripts/sdlc/docs.py:L115)
- digests() (scripts/sdlc/docs.py:L119)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L120)
- receipt_of() (scripts/sdlc/docs.py:L131)
- The last line of `deliver --json` output that decodes as a JSON object. (scripts/sdlc/docs.py:L132)
- validation() (scripts/sdlc/docs.py:L143)
- render() (scripts/sdlc/docs.py:L149)
- check() (scripts/sdlc/docs.py:L182)
- The stage document exists and was delivered from the sources as they are now. (scripts/sdlc/docs.py:L183)
- open() (scripts/sdlc/docs.py:L201)
- cfg() (scripts/sdlc/docs.py:L36)
- enabled() (scripts/sdlc/docs.py:L40)
- when_enabled() (scripts/sdlc/docs.py:L44)
- skill_dir() (scripts/sdlc/docs.py:L55)
- installed() (scripts/sdlc/docs.py:L60)
- version() (scripts/sdlc/docs.py:L64)
- node_version() (scripts/sdlc/docs.py:L71)
- Major version of the `node` on PATH, or None when absent or unparseable. (scripts/sdlc/docs.py:L72)
- tooling() (scripts/sdlc/docs.py:L80)
- Why Archify cannot run here, or None when it can. (scripts/sdlc/docs.py:L81)
- stage_of() (scripts/sdlc/docs.py:L95)

# Depends on
- [fail](/modules/fail.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
