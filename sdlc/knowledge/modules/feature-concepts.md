---
type: Module
title: feature_concepts
description: "Graphify community 15: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- slugify() (plugin/scripts/sdlc/artifacts.py:L30)
- first_line() (plugin/scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (plugin/scripts/sdlc/artifacts.py:L75)
- as_actor() (plugin/scripts/sdlc/knowledge.py:L1060)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (plugin/scripts/sdlc/knowledge.py:L1061)
- is_code() (plugin/scripts/sdlc/knowledge.py:L559)
- Graphify tags code, document and rationale nodes; only code communities become… (plugin/scripts/sdlc/knowledge.py:L560)
- communities() (plugin/scripts/sdlc/knowledge.py:L575)
- Graphify code communities big enough for a Module concept, with a stable slug… (plugin/scripts/sdlc/knowledge.py:L576)
- god_nodes() (plugin/scripts/sdlc/knowledge.py:L595)
- The most connected code nodes by degree, from the graph already in memory (what… (plugin/scripts/sdlc/knowledge.py:L596)
- concept() (plugin/scripts/sdlc/knowledge.py:L606)
- section() (plugin/scripts/sdlc/knowledge.py:L619)
- module_concepts() (plugin/scripts/sdlc/knowledge.py:L629)
- review_counts() (plugin/scripts/sdlc/knowledge.py:L660)
- feature_status() (plugin/scripts/sdlc/knowledge.py:L668)
- feature_concepts() (plugin/scripts/sdlc/knowledge.py:L680)
- hub_concepts() (plugin/scripts/sdlc/knowledge.py:L709)
- first_sentence() (plugin/scripts/sdlc/knowledge.py:L737)
- lesson_concepts() (plugin/scripts/sdlc/knowledge.py:L741)
- band_concepts() (plugin/scripts/sdlc/knowledge.py:L770)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [check](/modules/check.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)
- [watch](/modules/watch.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
