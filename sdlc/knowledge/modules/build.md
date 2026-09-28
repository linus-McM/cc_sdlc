---
type: Module
title: build
description: "Graphify community 72: plugin/scripts/sdlc/packs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 976267a001f822d8 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
---

# Files
- `plugin/scripts/sdlc/packs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- build() (plugin/scripts/sdlc/packs.py:L230)
- Select, guard and pack the files a stage's agents need; see the module… (plugin/scripts/sdlc/packs.py:L231)
- write_pack() (plugin/scripts/sdlc/packs.py:L267)
- Walk the ladder into a temp file, then write the manifest and move the pack… (plugin/scripts/sdlc/packs.py:L268)
- verdict_of() (plugin/scripts/sdlc/packs.py:L301)
- ladder() (plugin/scripts/sdlc/packs.py:L312)
- Step down the ladder, recording every rung tried with its tokens and dropped… (plugin/scripts/sdlc/packs.py:L313)
- prune() (plugin/scripts/sdlc/packs.py:L337)
- run_bandit() (plugin/scripts/sdlc/packs.py:L349)
- run_repomix() (plugin/scripts/sdlc/packs.py:L373)
- Pack `files` into `out` with the plugin's config (secret check forced on); the… (plugin/scripts/sdlc/packs.py:L374)
- suspicious() (plugin/scripts/sdlc/packs.py:L388)
- Files Repomix's secret check flagged, read from its Security Check block only… (plugin/scripts/sdlc/packs.py:L389)
- scan_output() (plugin/scripts/sdlc/packs.py:L401)
- Refuse unless the output holds exactly the requested files; verdicts name… (plugin/scripts/sdlc/packs.py:L402)
- run_cmd() (plugin/scripts/sdlc/project.py:L198)
- Run an external tool without a shell; never raises on a non-zero exit. A… (plugin/scripts/sdlc/project.py:L199)

# Depends on
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-44.md)
- [packs.py](/modules/packs-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [select](/modules/select.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
