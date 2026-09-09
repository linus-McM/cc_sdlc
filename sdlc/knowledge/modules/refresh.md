---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:59:02Z" }
stale_after: "2026-09-23T01:59:02Z"
source_commit: e0523eb3d807827869c761a89aea8117eb781e36
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
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L182)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L183)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- bootstrap() (scripts/sdlc/knowledge.py:L420)
- verified_events() (scripts/sdlc/knowledge.py:L481)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L482)
- is_stale() (scripts/sdlc/knowledge.py:L487)
- bundle_counts() (scripts/sdlc/knowledge.py:L524)
- status() (scripts/sdlc/knowledge.py:L536)
- now_iso() (scripts/sdlc/knowledge.py:L559)
- last_modified() (scripts/sdlc/knowledge.py:L822)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L823)
- append_log() (scripts/sdlc/knowledge.py:L886)
- refresh() (scripts/sdlc/knowledge.py:L934)

# Depends on
- [band_concepts](/modules/band-concepts.md)
- [Digests](/modules/digests.md)
- [knowledge.py](/modules/knowledge-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_state](/modules/read-state.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
