---
type: Module
title: packs.py
description: "Graphify community 57: plugin/scripts/sdlc/packs.py, plugin/scripts/sdlc/project.py, sdlc/graph-selected-repomix-context-packs/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 976267a001f822d8 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: spec, resource: sdlc/graph-selected-repomix-context-packs/spec.md, last_modified: "2026-09-26T09:27:53+10:00", digest: 39b0915a5020a08c }
---

# Files
- `plugin/scripts/sdlc/packs.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/graph-selected-repomix-context-packs/spec.md`

# Symbols
- packs.py (plugin/scripts/sdlc/packs.py:L1)
- Graph-selected Repomix context packs: one commit-pinned snapshot per stage that… (plugin/scripts/sdlc/packs.py:L1)
- secret_rule() (plugin/scripts/sdlc/packs.py:L102)
- The EXCLUDE pattern `path` matches, ignoring case (`SERVER.PEM` is still a key). (plugin/scripts/sdlc/packs.py:L103)
- git_ignored() (plugin/scripts/sdlc/packs.py:L111)
- Files git would ignore, tracked or not (`--no-index`). (plugin/scripts/sdlc/packs.py:L112)
- admit() (plugin/scripts/sdlc/packs.py:L118)
- Split the selection into files Repomix may read and exclusions with the rule… (plugin/scripts/sdlc/packs.py:L119)
- switched_off() (plugin/scripts/sdlc/packs.py:L171)
- SDLC_PACKS=off: packs and their gates skip visibly (tests default to it; the… (plugin/scripts/sdlc/packs.py:L172)
- off() (plugin/scripts/sdlc/packs.py:L176)
- The visible skip verdict when packs do not apply: layer off (SDLC_KNOWLEDGE /… (plugin/scripts/sdlc/packs.py:L177)
- repomix_on_path() (plugin/scripts/sdlc/packs.py:L184)
- missing_repomix() (plugin/scripts/sdlc/packs.py:L188)
- repomix_present() (plugin/scripts/sdlc/packs.py:L193)
- install_repomix() (plugin/scripts/sdlc/packs.py:L199)
- update_repomix() (plugin/scripts/sdlc/packs.py:L203)
- packs_dir() (plugin/scripts/sdlc/packs.py:L324)
- store() (plugin/scripts/sdlc/packs.py:L328)
- packs_dir, created with a `*` .gitignore on first use so nothing in it is ever… (plugin/scripts/sdlc/packs.py:L329)
- latest() (plugin/scripts/sdlc/packs.py:L415)
- The newest manifest for a slug and stage whose pack file still exists. (plugin/scripts/sdlc/packs.py:L416)
- require() (plugin/scripts/sdlc/packs.py:L422)
- The gate for a stage in GATED: ok (visibly skipped) when packs are off;… (plugin/scripts/sdlc/packs.py:L423)
- review_changes() (plugin/scripts/sdlc/packs.py:L439)
- Files the test pack seeds from and must cover: the branch diff against… (plugin/scripts/sdlc/packs.py:L440)
- covered() (plugin/scripts/sdlc/packs.py:L447)
- section_tokens() (plugin/scripts/sdlc/packs.py:L52)
- changed_since() (plugin/scripts/sdlc/packs.py:L56)
- Committed text files changed in `spec` (a git range); deleted, binary (numstat… (plugin/scripts/sdlc/packs.py:L57)
- plan_seeds() (plugin/scripts/sdlc/packs.py:L64)
- maintain_seeds() (plugin/scripts/sdlc/packs.py:L68)
- ran() (plugin/scripts/sdlc/project.py:L106)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (plugin/scripts/sdlc/project.py:L107)
- Design (sdlc/graph-selected-repomix-context-packs/spec.md:L121)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [build](/modules/build.md)
- [build.py](/modules/build-py.md)
- [cfg](/modules/cfg.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [select](/modules/select.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [accept](/modules/accept.md)
- [build](/modules/build.md)
- [check](/modules/check.md)
- [conftest.py](/modules/conftest-py.md)
- [git](/modules/git.md)
- [Path](/modules/path.md)
- [select](/modules/select.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
