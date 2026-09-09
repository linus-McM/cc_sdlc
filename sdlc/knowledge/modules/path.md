---
type: Module
title: Path
description: "Graphify community 89: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T03:17:42Z" }
stale_after: "2026-09-23T03:17:42Z"
source_commit: 218a4937bbfd93cc3d6ae744243e90dacb2bf072
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L192)
- skill_path() (scripts/sdlc/knowledge.py:L196)
- state_path() (scripts/sdlc/knowledge.py:L200)
- read_state() (scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L205)
- write_state() (scripts/sdlc/knowledge.py:L212)
- install_graphify() (scripts/sdlc/knowledge.py:L319)
- install_skill() (scripts/sdlc/knowledge.py:L323)
- write_ignore() (scripts/sdlc/knowledge.py:L349)
- build_graph() (scripts/sdlc/knowledge.py:L354)
- bundle_present() (scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L359)
- pointer_present() (scripts/sdlc/knowledge.py:L368)
- graph_commit() (scripts/sdlc/knowledge.py:L439)
- artifacts_agree() (scripts/sdlc/knowledge.py:L459)
- behind() (scripts/sdlc/knowledge.py:L475)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L476)
- staleness() (scripts/sdlc/knowledge.py:L483)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L484)
- load_graph() (scripts/sdlc/knowledge.py:L555)
- review_counts() (scripts/sdlc/knowledge.py:L660)
- feature_status() (scripts/sdlc/knowledge.py:L668)
- feature_concepts() (scripts/sdlc/knowledge.py:L680)
- ran() (scripts/sdlc/project.py:L93)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/project.py:L94)

# Depends on
- [band_concepts](/modules/band-concepts.md)
- [docs.py](/modules/docs-py.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [docs.py](/modules/docs-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
