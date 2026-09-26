---
type: Module
title: packs.py
description: "Graphify community 57: plugin/scripts/sdlc/packs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
---

# Files
- `plugin/scripts/sdlc/packs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- packs.py (plugin/scripts/sdlc/packs.py:L1)
- Graph-selected Repomix context packs: one commit-pinned snapshot per stage that… (plugin/scripts/sdlc/packs.py:L1)
- switched_off() (plugin/scripts/sdlc/packs.py:L171)
- SDLC_PACKS=off: packs and their gates skip visibly (tests default to it; the… (plugin/scripts/sdlc/packs.py:L172)
- off() (plugin/scripts/sdlc/packs.py:L176)
- The visible skip verdict when packs do not apply: layer off (SDLC_KNOWLEDGE /… (plugin/scripts/sdlc/packs.py:L177)
- repomix_on_path() (plugin/scripts/sdlc/packs.py:L184)
- missing_repomix() (plugin/scripts/sdlc/packs.py:L188)
- repomix_present() (plugin/scripts/sdlc/packs.py:L193)
- install_repomix() (plugin/scripts/sdlc/packs.py:L199)
- update_repomix() (plugin/scripts/sdlc/packs.py:L203)
- ran() (plugin/scripts/sdlc/project.py:L106)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (plugin/scripts/sdlc/project.py:L107)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build](/modules/build.md)
- [build.py](/modules/build-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fresh_graph](/modules/fresh-graph.md)
- [git](/modules/git.md)
- [hooks.py](/modules/hooks-py.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [require](/modules/require.md)
- [review](/modules/review.md)
- [run_repomix](/modules/run-repomix.md)

# Inferred
- [fresh_graph](/modules/fresh-graph.md)
- [Path](/modules/path.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
