---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc/artifacts.py, scripts/sdlc/build.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T03:17:42Z" }
stale_after: "2026-09-23T03:17:42Z"
source_commit: 218a4937bbfd93cc3d6ae744243e90dacb2bf072
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-09T10:28:52+10:00", digest: e0aa4bc15a604e1d }
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 13fece25897d5a38 }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: ba620d207f00af60 }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/build.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (scripts/hook.py:L2)
- artifacts.py (scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (scripts/sdlc/artifacts.py:L1)
- matches() (scripts/sdlc/artifacts.py:L100)
- title() (scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (scripts/sdlc/artifacts.py:L35)
- sections() (scripts/sdlc/artifacts.py:L39)
- set_section() (scripts/sdlc/artifacts.py:L44)
- set_meta() (scripts/sdlc/artifacts.py:L54)
- validate() (scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (scripts/sdlc/artifacts.py:L63)
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- list_items() (scripts/sdlc/artifacts.py:L79)
- Paths from a bulleted or comma-separated section body, annotations stripped. (scripts/sdlc/artifacts.py:L80)
- glob_regex() (scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (scripts/sdlc/artifacts.py:L93)
- build.py (scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (scripts/sdlc/build.py:L1)
- run_cmd() (scripts/sdlc/build.py:L15)
- cycles() (scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (scripts/sdlc/build.py:L24)
- tdd() (scripts/sdlc/build.py:L35)
- planned_files() (scripts/sdlc/build.py:L57)
- is_sdlc_owned() (scripts/sdlc/build.py:L62)
- sync() (scripts/sdlc/build.py:L66)
- fix() (scripts/sdlc/build.py:L78)
- gated() (scripts/sdlc/deploy.py:L45)
- Environments at the `gate` tier in a `[deploy]` config table. (scripts/sdlc/deploy.py:L46)
- hooks.py (scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (scripts/sdlc/hooks.py:L1)
- release_hit() (scripts/sdlc/hooks.py:L101)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (scripts/sdlc/hooks.py:L102)
- pre_bash() (scripts/sdlc/hooks.py:L120)
- post_edit() (scripts/sdlc/hooks.py:L129)
- is_commit() (scripts/sdlc/hooks.py:L142)
- post_bash() (scripts/sdlc/hooks.py:L147)
- After a commit: say when an index has fallen further behind than the configured… (scripts/sdlc/hooks.py:L148)
- main() (scripts/sdlc/hooks.py:L181)
- deny() (scripts/sdlc/hooks.py:L25)
- context() (scripts/sdlc/hooks.py:L35)
- rel_path() (scripts/sdlc/hooks.py:L39)
- active_feature() (scripts/sdlc/hooks.py:L52)
- pre_edit() (scripts/sdlc/hooks.py:L59)
- command_lines() (scripts/sdlc/hooks.py:L77)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (scripts/sdlc/hooks.py:L78)
- tokens() (scripts/sdlc/hooks.py:L90)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (scripts/sdlc/hooks.py:L91)

# Depends on
- [append_log](/modules/append-log.md)
- [band_concepts](/modules/band-concepts.md)
- [docs.py](/modules/docs-py.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)

# Inferred
- [docs.py](/modules/docs-py.md)
- [status](/modules/status.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
