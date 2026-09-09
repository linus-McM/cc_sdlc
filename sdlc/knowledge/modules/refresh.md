---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (scripts/sdlc/knowledge.py:L1028)
- check() (scripts/sdlc/knowledge.py:L1041)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1042)
- publish() (scripts/sdlc/knowledge.py:L1089)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1090)
- split_document() (scripts/sdlc/knowledge.py:L149)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L182)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L183)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- bootstrap() (scripts/sdlc/knowledge.py:L421)
- verified_events() (scripts/sdlc/knowledge.py:L488)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L489)
- bundle_counts() (scripts/sdlc/knowledge.py:L531)
- status() (scripts/sdlc/knowledge.py:L543)
- now_iso() (scripts/sdlc/knowledge.py:L569)
- content_keys() (scripts/sdlc/knowledge.py:L821)
- last_modified() (scripts/sdlc/knowledge.py:L833)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L834)
- append_log() (scripts/sdlc/knowledge.py:L897)
- refresh() (scripts/sdlc/knowledge.py:L945)

# Depends on
- [bump_version.py](/modules/bump-version-py.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [feature_concepts](/modules/feature-concepts.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_state](/modules/read-state.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
