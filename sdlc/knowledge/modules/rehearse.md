---
type: Module
title: rehearse
description: "Graphify community 90: plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/spec.md, sdlc/rehearsal-and-band-nits/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
  - { id: spec, resource: sdlc/rehearsal-and-band-nits/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: b81cd9d3882a7703 }
---

# Files
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/spec.md`
- `sdlc/rehearsal-and-band-nits/spec.md`

# Symbols
- rehearse() (plugin/scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (plugin/scripts/sdlc/deploy.py:L77)
- ensure_config() (plugin/scripts/sdlc/project.py:L165)
- run_git() (plugin/scripts/sdlc/project.py:L207)
- git() (plugin/scripts/sdlc/project.py:L211)
- head_commit() (plugin/scripts/sdlc/project.py:L215)
- author() (plugin/scripts/sdlc/project.py:L219)
- changed_files() (plugin/scripts/sdlc/project.py:L223)
- Staged, unstaged and untracked paths in one git call, limited to `paths` when… (plugin/scripts/sdlc/project.py:L224)
- Design (sdlc/dogfood-fixes-round-two/spec.md:L13)
- rehearsal-and-band-nits/spec.md (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Spec: Rehearsal and band nits (sdlc/rehearsal-and-band-nits/spec.md:L1)
- Design (sdlc/rehearsal-and-band-nits/spec.md:L13)
- Concerns (sdlc/rehearsal-and-band-nits/spec.md:L20)
- Open questions (sdlc/rehearsal-and-band-nits/spec.md:L23)
- Requirements (sdlc/rehearsal-and-band-nits/spec.md:L4)

# Depends on
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work-45.md)
- [post_edit](/modules/post-edit.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
