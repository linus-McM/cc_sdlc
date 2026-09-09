---
type: Module
title: refresh
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:35:57Z" }
stale_after: "2026-09-22T22:35:57Z"
source_commit: c6f9a22e23b0bee7134aa1e1709c5feef8673f82
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:35:54+10:00", digest: 5ed472fa5f0e7275 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- policy_findings() (scripts/sdlc/knowledge.py:L1017)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1018)
- publish() (scripts/sdlc/knowledge.py:L1037)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1038)
- split_document() (scripts/sdlc/knowledge.py:L149)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L179)
- bundle_dir() (scripts/sdlc/knowledge.py:L183)
- build_bundle() (scripts/sdlc/knowledge.py:L366)
- bootstrap() (scripts/sdlc/knowledge.py:L398)
- verified_events() (scripts/sdlc/knowledge.py:L457)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L458)
- is_stale() (scripts/sdlc/knowledge.py:L463)
- bundle_counts() (scripts/sdlc/knowledge.py:L492)
- status() (scripts/sdlc/knowledge.py:L504)
- now_iso() (scripts/sdlc/knowledge.py:L527)
- plugin_version() (scripts/sdlc/knowledge.py:L532)
- signature() (scripts/sdlc/knowledge.py:L775)
- Content identity: the builder's own keys plus the body; provenance and trust… (scripts/sdlc/knowledge.py:L776)
- last_modified() (scripts/sdlc/knowledge.py:L783)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L784)
- append_log() (scripts/sdlc/knowledge.py:L847)
- refresh() (scripts/sdlc/knowledge.py:L895)
- concept_files() (scripts/sdlc/knowledge.py:L976)
- check() (scripts/sdlc/knowledge.py:L989)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L990)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [ran](/modules/ran.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
