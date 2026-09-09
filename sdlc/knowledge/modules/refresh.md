---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:34Z" }
stale_after: "2026-09-23T00:28:34Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:18:34+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- policy_findings() (scripts/sdlc/knowledge.py:L1018)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1019)
- publish() (scripts/sdlc/knowledge.py:L1038)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1039)
- split_document() (scripts/sdlc/knowledge.py:L149)
- bundle_dir() (scripts/sdlc/knowledge.py:L183)
- verified_events() (scripts/sdlc/knowledge.py:L457)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L458)
- is_stale() (scripts/sdlc/knowledge.py:L463)
- bundle_counts() (scripts/sdlc/knowledge.py:L492)
- now_iso() (scripts/sdlc/knowledge.py:L527)
- signature() (scripts/sdlc/knowledge.py:L775)
- Content identity: the builder's own keys plus the body; provenance and trust… (scripts/sdlc/knowledge.py:L776)
- last_modified() (scripts/sdlc/knowledge.py:L783)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L784)
- append_log() (scripts/sdlc/knowledge.py:L847)
- refresh() (scripts/sdlc/knowledge.py:L895)
- concept_files() (scripts/sdlc/knowledge.py:L977)
- check() (scripts/sdlc/knowledge.py:L990)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L991)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [render](/modules/render.md)
- [status](/modules/status.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
