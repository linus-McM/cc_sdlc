---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:48:10Z" }
stale_after: "2026-09-23T01:48:10Z"
source_commit: f5370acaa20694aba335e2e3cab1cee4dc0582a5
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (scripts/sdlc/knowledge.py:L1017)
- check() (scripts/sdlc/knowledge.py:L1030)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1031)
- policy_findings() (scripts/sdlc/knowledge.py:L1058)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1059)
- publish() (scripts/sdlc/knowledge.py:L1078)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1079)
- split_document() (scripts/sdlc/knowledge.py:L149)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- verified_events() (scripts/sdlc/knowledge.py:L481)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L482)
- is_stale() (scripts/sdlc/knowledge.py:L487)
- bundle_counts() (scripts/sdlc/knowledge.py:L524)
- now_iso() (scripts/sdlc/knowledge.py:L559)
- plugin_version() (scripts/sdlc/knowledge.py:L564)
- content_keys() (scripts/sdlc/knowledge.py:L810)
- signature() (scripts/sdlc/knowledge.py:L814)
- Content identity: the builder's keys (present on either side) plus the body;… (scripts/sdlc/knowledge.py:L815)
- last_modified() (scripts/sdlc/knowledge.py:L822)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L823)
- refresh() (scripts/sdlc/knowledge.py:L934)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [communities](/modules/communities.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
