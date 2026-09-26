---
type: Module
title: refresh
description: "Graphify community 35: plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- concept_files() (plugin/scripts/sdlc/knowledge.py:L1009)
- check() (plugin/scripts/sdlc/knowledge.py:L1022)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (plugin/scripts/sdlc/knowledge.py:L1023)
- publish() (plugin/scripts/sdlc/knowledge.py:L1070)
- Append a verification event to the feature's concept; only a human: actor… (plugin/scripts/sdlc/knowledge.py:L1071)
- split_document() (plugin/scripts/sdlc/knowledge.py:L149)
- when_enabled() (plugin/scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (plugin/scripts/sdlc/knowledge.py:L164)
- bundle_dir() (plugin/scripts/sdlc/knowledge.py:L188)
- build_bundle() (plugin/scripts/sdlc/knowledge.py:L363)
- verified_events() (plugin/scripts/sdlc/knowledge.py:L469)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (plugin/scripts/sdlc/knowledge.py:L470)
- bundle_counts() (plugin/scripts/sdlc/knowledge.py:L512)
- plugin_version() (plugin/scripts/sdlc/knowledge.py:L555)
- link() (plugin/scripts/sdlc/knowledge.py:L619)
- content_keys() (plugin/scripts/sdlc/knowledge.py:L802)
- last_modified() (plugin/scripts/sdlc/knowledge.py:L814)
- Last commit date per source path from one `git log --name-only` over all of… (plugin/scripts/sdlc/knowledge.py:L815)
- reconcile() (plugin/scripts/sdlc/knowledge.py:L894)
- Concept files nothing generated any more: tombstone when every source is… (plugin/scripts/sdlc/knowledge.py:L895)
- refresh() (plugin/scripts/sdlc/knowledge.py:L926)
- now_iso() (plugin/scripts/sdlc/project.py:L232)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [knowledge.py](/modules/knowledge-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path-13.md)
- [project.py](/modules/project-py.md)
- [review](/modules/review.md)
- [status](/modules/status.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- [hooks.py](/modules/hooks-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
