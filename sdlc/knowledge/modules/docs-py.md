---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:33Z" }
stale_after: "2026-09-23T03:02:33Z"
source_commit: 7a6549e2e0a57fe6fe0b1257011d2e78bce58136
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 10270177466cde0a }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
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
- source_bytes() (scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (scripts/sdlc/docs.py:L164)
- digests() (scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L176)
- receipt_of() (scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (scripts/sdlc/docs.py:L188)
- validation() (scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (scripts/sdlc/docs.py:L200)
- render() (scripts/sdlc/docs.py:L212)
- check() (scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (scripts/sdlc/docs.py:L246)
- open() (scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L265)
- documents() (scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (scripts/sdlc/docs.py:L280)
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
- rel() (scripts/sdlc/project.py:L119)
- read_json() (scripts/sdlc/project.py:L237)

# Depends on
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [deploy.py](/modules/deploy-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
