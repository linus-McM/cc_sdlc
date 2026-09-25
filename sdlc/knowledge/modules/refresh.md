---
type: Module
title: refresh
description: "Graphify community 11: plugin/README.md, plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 2e559b282f80c004 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- Knowledge (Graphify + OKF) (plugin/README.md:L36)
- concept_files() (plugin/scripts/sdlc/knowledge.py:L1005)
- check() (plugin/scripts/sdlc/knowledge.py:L1018)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (plugin/scripts/sdlc/knowledge.py:L1019)
- policy_findings() (plugin/scripts/sdlc/knowledge.py:L1046)
- Organisational rules, stricter than the spec and reported apart from it. (plugin/scripts/sdlc/knowledge.py:L1047)
- publish() (plugin/scripts/sdlc/knowledge.py:L1066)
- Append a verification event to the feature's concept; only a human: actor… (plugin/scripts/sdlc/knowledge.py:L1067)
- split_document() (plugin/scripts/sdlc/knowledge.py:L149)
- when_enabled() (plugin/scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (plugin/scripts/sdlc/knowledge.py:L164)
- bundle_dir() (plugin/scripts/sdlc/knowledge.py:L188)
- tool() (plugin/scripts/sdlc/knowledge.py:L237)
- build_bundle() (plugin/scripts/sdlc/knowledge.py:L363)
- verified_events() (plugin/scripts/sdlc/knowledge.py:L465)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (plugin/scripts/sdlc/knowledge.py:L466)
- is_stale() (plugin/scripts/sdlc/knowledge.py:L471)
- bundle_counts() (plugin/scripts/sdlc/knowledge.py:L508)
- plugin_version() (plugin/scripts/sdlc/knowledge.py:L551)
- load_graph() (plugin/scripts/sdlc/knowledge.py:L555)
- content_keys() (plugin/scripts/sdlc/knowledge.py:L798)
- last_modified() (plugin/scripts/sdlc/knowledge.py:L810)
- Last commit date per source path from one `git log --name-only` over all of… (plugin/scripts/sdlc/knowledge.py:L811)
- refresh() (plugin/scripts/sdlc/knowledge.py:L922)
- now_iso() (plugin/scripts/sdlc/project.py:L229)
- Data flow (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L195)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Components](/modules/components.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [rehearse](/modules/rehearse.md)
- [status](/modules/status.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- [Path](/modules/path.md)
- [status](/modules/status.md)

# Features
- no feature plan names these files
