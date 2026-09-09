---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:08:45Z" }
stale_after: "2026-09-23T02:08:45Z"
source_commit: 0794a80b6291964cd26930a809a8678a9c9b1311
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (scripts/sdlc/knowledge.py:L1028)
- check() (scripts/sdlc/knowledge.py:L1041)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1042)
- policy_findings() (scripts/sdlc/knowledge.py:L1069)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1070)
- publish() (scripts/sdlc/knowledge.py:L1089)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1090)
- split_document() (scripts/sdlc/knowledge.py:L149)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- verified_events() (scripts/sdlc/knowledge.py:L488)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L489)
- is_stale() (scripts/sdlc/knowledge.py:L494)
- bundle_counts() (scripts/sdlc/knowledge.py:L531)
- status() (scripts/sdlc/knowledge.py:L543)
- now_iso() (scripts/sdlc/knowledge.py:L569)
- last_modified() (scripts/sdlc/knowledge.py:L833)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L834)
- append_log() (scripts/sdlc/knowledge.py:L897)
- refresh() (scripts/sdlc/knowledge.py:L945)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [read_state](/modules/read-state.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
