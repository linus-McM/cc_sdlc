---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:08:45Z" }
stale_after: "2026-09-23T02:08:45Z"
source_commit: 0794a80b6291964cd26930a809a8678a9c9b1311
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:08:42+10:00", digest: d25de13fe5bc18ee }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- Present (scripts/sdlc/docs.py:L100)
- A truthy present-check result that carries the detail to report (the installed… (scripts/sdlc/docs.py:L101)
- archify_present() (scripts/sdlc/docs.py:L104)
- Present when the skill is installed (no subprocess); StepSkipped when docs are… (scripts/sdlc/docs.py:L105)
- install_archify() (scripts/sdlc/docs.py:L117)
- stage_of() (scripts/sdlc/docs.py:L127)
- target() (scripts/sdlc/docs.py:L133)
- The feature the document belongs to; maintain documents belong to the project,… (scripts/sdlc/docs.py:L134)
- docs_dir() (scripts/sdlc/docs.py:L138)
- sources() (scripts/sdlc/docs.py:L142)
- rel() (scripts/sdlc/docs.py:L147)
- digests() (scripts/sdlc/docs.py:L151)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L152)
- receipt_of() (scripts/sdlc/docs.py:L163)
- The last line of `deliver --json` output that decodes as a JSON object. (scripts/sdlc/docs.py:L164)
- validation() (scripts/sdlc/docs.py:L175)
- render() (scripts/sdlc/docs.py:L181)
- check() (scripts/sdlc/docs.py:L214)
- The stage document exists and was delivered from the sources as they are now. (scripts/sdlc/docs.py:L215)
- open() (scripts/sdlc/docs.py:L233)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L234)
- documents() (scripts/sdlc/docs.py:L252)
- PR-body bullets: one per delivered stage document, with its receipt's… (scripts/sdlc/docs.py:L253)
- cfg() (scripts/sdlc/docs.py:L36)
- enabled() (scripts/sdlc/docs.py:L40)
- when_enabled() (scripts/sdlc/docs.py:L44)
- skill_dir() (scripts/sdlc/docs.py:L55)
- installed() (scripts/sdlc/docs.py:L60)
- version() (scripts/sdlc/docs.py:L64)
- version_tuple() (scripts/sdlc/docs.py:L71)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (scripts/sdlc/docs.py:L72)
- node_version() (scripts/sdlc/docs.py:L76)
- Major version of the `node` on PATH, or None when absent or unparseable. (scripts/sdlc/docs.py:L77)
- tooling() (scripts/sdlc/docs.py:L85)
- Why Archify cannot run here, or None when it can. (scripts/sdlc/docs.py:L86)
- StepSkipped (scripts/sdlc/knowledge.py:L328)
- This step does not apply here; later steps still run. (scripts/sdlc/knowledge.py:L329)

# Depends on
- [fail](/modules/fail.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
