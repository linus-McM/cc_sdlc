---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/docs.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:15:53+10:00", digest: 2a12b2cd99c9ad5c }
---

# Files
- `scripts/sdlc/docs.py`

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
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (scripts/sdlc/docs.py:L164)
- validation() (scripts/sdlc/docs.py:L175)
- One line from the receipt's `validation` block: `9/9 showcase, 0 errors, 0… (scripts/sdlc/docs.py:L176)
- render() (scripts/sdlc/docs.py:L182)
- check() (scripts/sdlc/docs.py:L215)
- The stage document exists and was delivered from the sources as they are now. (scripts/sdlc/docs.py:L216)
- open() (scripts/sdlc/docs.py:L234)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L235)
- documents() (scripts/sdlc/docs.py:L253)
- PR-body bullets: one per delivered stage document, with its receipt's… (scripts/sdlc/docs.py:L254)
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

# Depends on
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
