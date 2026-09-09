---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 947ee5e4755318f1 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 7fce16edc7c795cc }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- Present when the skill is installed (no subprocess); StepSkipped when docs are… (scripts/sdlc/docs.py:L100)
- install_archify() (scripts/sdlc/docs.py:L112)
- stage_of() (scripts/sdlc/docs.py:L122)
- target() (scripts/sdlc/docs.py:L128)
- The feature the document belongs to; maintain documents belong to the project,… (scripts/sdlc/docs.py:L129)
- docs_dir() (scripts/sdlc/docs.py:L133)
- sources() (scripts/sdlc/docs.py:L137)
- rel() (scripts/sdlc/docs.py:L142)
- digests() (scripts/sdlc/docs.py:L146)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L147)
- receipt_of() (scripts/sdlc/docs.py:L158)
- The last line of `deliver --json` output that decodes as a JSON object. (scripts/sdlc/docs.py:L159)
- validation() (scripts/sdlc/docs.py:L170)
- render() (scripts/sdlc/docs.py:L176)
- check() (scripts/sdlc/docs.py:L209)
- The stage document exists and was delivered from the sources as they are now. (scripts/sdlc/docs.py:L210)
- open() (scripts/sdlc/docs.py:L228)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L229)
- documents() (scripts/sdlc/docs.py:L247)
- PR-body bullets: one per delivered stage document, with its receipt's… (scripts/sdlc/docs.py:L248)
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
- Present (scripts/sdlc/docs.py:L95)
- A truthy present-check result that carries the detail to report (the installed… (scripts/sdlc/docs.py:L96)
- archify_present() (scripts/sdlc/docs.py:L99)
- StepSkipped (scripts/sdlc/knowledge.py:L328)
- This step does not apply here; later steps still run. (scripts/sdlc/knowledge.py:L329)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
