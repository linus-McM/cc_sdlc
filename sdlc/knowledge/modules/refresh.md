---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:05:50Z" }
stale_after: "2026-09-23T03:05:50Z"
source_commit: f99c31fe37e72ede2fd21532a6ffb7137b40bc9e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- concept_files() (scripts/sdlc/knowledge.py:L1005)
- check() (scripts/sdlc/knowledge.py:L1018)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1019)
- policy_findings() (scripts/sdlc/knowledge.py:L1046)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1047)
- publish() (scripts/sdlc/knowledge.py:L1066)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1067)
- split_document() (scripts/sdlc/knowledge.py:L149)
- bundle_dir() (scripts/sdlc/knowledge.py:L188)
- tool() (scripts/sdlc/knowledge.py:L237)
- build_bundle() (scripts/sdlc/knowledge.py:L363)
- verified_events() (scripts/sdlc/knowledge.py:L465)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L466)
- is_stale() (scripts/sdlc/knowledge.py:L471)
- bundle_counts() (scripts/sdlc/knowledge.py:L508)
- plugin_version() (scripts/sdlc/knowledge.py:L551)
- content_keys() (scripts/sdlc/knowledge.py:L798)
- signature() (scripts/sdlc/knowledge.py:L802)
- Content identity: the builder's keys (present on either side) plus the body;… (scripts/sdlc/knowledge.py:L803)
- last_modified() (scripts/sdlc/knowledge.py:L810)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L811)
- refresh() (scripts/sdlc/knowledge.py:L922)
- now_iso() (scripts/sdlc/project.py:L219)

# Depends on
- [append_log](/modules/append-log.md)
- [band_concepts](/modules/band-concepts.md)
- [bump_version.py](/modules/bump-version-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
