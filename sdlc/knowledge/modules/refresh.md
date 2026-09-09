---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:29:56Z" }
stale_after: "2026-09-23T01:29:56Z"
source_commit: b6e8d5897548ac1aeadd713c4fd9bf19fac3d435
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- render() (scripts/sdlc/artifacts.py:L88)
- concept_files() (scripts/sdlc/knowledge.py:L1017)
- check() (scripts/sdlc/knowledge.py:L1030)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1031)
- publish() (scripts/sdlc/knowledge.py:L1078)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1079)
- split_document() (scripts/sdlc/knowledge.py:L149)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- write_pointer() (scripts/sdlc/knowledge.py:L398)
- verified_events() (scripts/sdlc/knowledge.py:L481)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L482)
- bundle_counts() (scripts/sdlc/knowledge.py:L524)
- now_iso() (scripts/sdlc/knowledge.py:L559)
- plugin_version() (scripts/sdlc/knowledge.py:L564)
- link() (scripts/sdlc/knowledge.py:L628)
- content_keys() (scripts/sdlc/knowledge.py:L810)
- signature() (scripts/sdlc/knowledge.py:L814)
- Content identity: the builder's keys (present on either side) plus the body;… (scripts/sdlc/knowledge.py:L815)
- last_modified() (scripts/sdlc/knowledge.py:L822)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L823)
- append_log() (scripts/sdlc/knowledge.py:L886)
- reconcile() (scripts/sdlc/knowledge.py:L902)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L903)
- refresh() (scripts/sdlc/knowledge.py:L934)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [feature_concepts](/modules/feature-concepts.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
