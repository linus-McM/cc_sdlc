---
type: Module
title: refresh
description: "Graphify community 12: plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- concept_files() (plugin/scripts/sdlc/knowledge.py:L1005)
- concepts_for() (plugin/scripts/sdlc/knowledge.py:L1011)
- Project-relative module concept paths describing `rel`, from the file map the… (plugin/scripts/sdlc/knowledge.py:L1012)
- check() (plugin/scripts/sdlc/knowledge.py:L1018)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (plugin/scripts/sdlc/knowledge.py:L1019)
- publish() (plugin/scripts/sdlc/knowledge.py:L1066)
- Append a verification event to the feature's concept; only a human: actor… (plugin/scripts/sdlc/knowledge.py:L1067)
- split_document() (plugin/scripts/sdlc/knowledge.py:L149)
- when_enabled() (plugin/scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (plugin/scripts/sdlc/knowledge.py:L164)
- cfg() (plugin/scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (plugin/scripts/sdlc/knowledge.py:L175)
- bundle_dir() (plugin/scripts/sdlc/knowledge.py:L188)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)
- verified_events() (plugin/scripts/sdlc/knowledge.py:L465)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (plugin/scripts/sdlc/knowledge.py:L466)
- bundle_counts() (plugin/scripts/sdlc/knowledge.py:L508)
- status() (plugin/scripts/sdlc/knowledge.py:L520)
- last_modified() (plugin/scripts/sdlc/knowledge.py:L810)
- Last commit date per source path from one `git log --name-only` over all of… (plugin/scripts/sdlc/knowledge.py:L811)
- append_log() (plugin/scripts/sdlc/knowledge.py:L874)
- refresh() (plugin/scripts/sdlc/knowledge.py:L922)
- now_iso() (plugin/scripts/sdlc/project.py:L229)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [Path](/modules/path-13.md)
- [reconcile](/modules/reconcile.md)
- [rehearse](/modules/rehearse.md)
- [render](/modules/render.md)
- [StepSkipped](/modules/stepskipped.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
