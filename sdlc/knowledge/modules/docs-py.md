---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d7a57e7ce569fd72 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d046c71e8661e436 }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/project.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- archify_present() (scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (scripts/sdlc/docs.py:L108)
- install_archify() (scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (scripts/sdlc/docs.py:L119)
- mechanic() (scripts/sdlc/docs.py:L129)
- CLI handler for `docs <action> <stage>`: the skipped verdict comes before any… (scripts/sdlc/docs.py:L130)
- docs_dir() (scripts/sdlc/docs.py:L147)
- sources() (scripts/sdlc/docs.py:L151)
- sha256() (scripts/sdlc/docs.py:L155)
- source_bytes() (scripts/sdlc/docs.py:L162)
- The bytes a document describes: a missing source is empty, and an artifact's… (scripts/sdlc/docs.py:L163)
- digests() (scripts/sdlc/docs.py:L169)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L170)
- receipt_of() (scripts/sdlc/docs.py:L181)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (scripts/sdlc/docs.py:L182)
- validation() (scripts/sdlc/docs.py:L193)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (scripts/sdlc/docs.py:L194)
- render() (scripts/sdlc/docs.py:L206)
- check() (scripts/sdlc/docs.py:L239)
- The stage document exists and was delivered from the sources as they are now… (scripts/sdlc/docs.py:L240)
- open() (scripts/sdlc/docs.py:L258)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L259)
- documents() (scripts/sdlc/docs.py:L270)
- One bullet per delivered stage document, with its receipt's validation line;… (scripts/sdlc/docs.py:L271)
- cfg() (scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (scripts/sdlc/docs.py:L39)
- enabled() (scripts/sdlc/docs.py:L47)
- skill_dir() (scripts/sdlc/docs.py:L57)
- installed() (scripts/sdlc/docs.py:L61)
- version() (scripts/sdlc/docs.py:L65)
- version_tuple() (scripts/sdlc/docs.py:L73)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (scripts/sdlc/docs.py:L74)
- node_version() (scripts/sdlc/docs.py:L79)
- Major version of the `node` on PATH, or None when absent or unparseable. (scripts/sdlc/docs.py:L80)
- node_problem() (scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (scripts/sdlc/docs.py:L89)
- tooling() (scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (scripts/sdlc/docs.py:L98)
- when_enabled() (scripts/sdlc/project.py:L101)
- Gate a layer's public mechanics on `enabled(root)`; `default` is the verdict… (scripts/sdlc/project.py:L102)
- rel() (scripts/sdlc/project.py:L119)
- read_json() (scripts/sdlc/project.py:L236)
- StepSkipped (scripts/sdlc/project.py:L89)
- This step does not apply here; later steps still run. (scripts/sdlc/project.py:L90)

# Depends on
- [build.py](/modules/build-py.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [deploy.py](/modules/deploy-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
