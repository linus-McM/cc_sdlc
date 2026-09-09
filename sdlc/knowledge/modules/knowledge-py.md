---
type: Module
title: knowledge.py
description: "Graphify community 86: scripts/sdlc/artifacts.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- uv_install_command() (scripts/sdlc/knowledge.py:L295)
- find_uv() (scripts/sdlc/knowledge.py:L300)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (scripts/sdlc/knowledge.py:L301)
- install_uv() (scripts/sdlc/knowledge.py:L315)
- install_graphify() (scripts/sdlc/knowledge.py:L319)
- write_ignore() (scripts/sdlc/knowledge.py:L349)
- pointer_present() (scripts/sdlc/knowledge.py:L368)
- scalar() (scripts/sdlc/knowledge.py:L43)
- flow() (scripts/sdlc/knowledge.py:L53)
- link() (scripts/sdlc/knowledge.py:L609)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- head_first() (scripts/sdlc/knowledge.py:L617)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L618)
- review_counts() (scripts/sdlc/knowledge.py:L654)
- feature_status() (scripts/sdlc/knowledge.py:L662)
- feature_concepts() (scripts/sdlc/knowledge.py:L674)
- render_concept() (scripts/sdlc/knowledge.py:L835)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L836)
- reconcile() (scripts/sdlc/knowledge.py:L884)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L885)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [band_concepts](/modules/band-concepts.md)
- [Blocked](/modules/blocked.md)
- [bump_version.py](/modules/bump-version-py.md)
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [staleness](/modules/staleness.md)
- [status](/modules/status.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [append_log](/modules/append-log.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)
- [staleness](/modules/staleness.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
