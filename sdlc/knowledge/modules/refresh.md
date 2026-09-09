---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d046c71e8661e436 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- check() (scripts/sdlc/knowledge.py:L1012)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1013)
- policy_findings() (scripts/sdlc/knowledge.py:L1040)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1041)
- publish() (scripts/sdlc/knowledge.py:L1060)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1061)
- split_document() (scripts/sdlc/knowledge.py:L149)
- bundle_dir() (scripts/sdlc/knowledge.py:L188)
- tool() (scripts/sdlc/knowledge.py:L237)
- build_bundle() (scripts/sdlc/knowledge.py:L363)
- verified_events() (scripts/sdlc/knowledge.py:L459)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L460)
- is_stale() (scripts/sdlc/knowledge.py:L465)
- bundle_counts() (scripts/sdlc/knowledge.py:L502)
- plugin_version() (scripts/sdlc/knowledge.py:L545)
- content_keys() (scripts/sdlc/knowledge.py:L792)
- signature() (scripts/sdlc/knowledge.py:L796)
- Content identity: the builder's keys (present on either side) plus the body;… (scripts/sdlc/knowledge.py:L797)
- last_modified() (scripts/sdlc/knowledge.py:L804)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L805)
- refresh() (scripts/sdlc/knowledge.py:L916)
- concept_files() (scripts/sdlc/knowledge.py:L999)
- now_iso() (scripts/sdlc/project.py:L218)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [band_concepts](/modules/band-concepts.md)
- [build.py](/modules/build-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
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
