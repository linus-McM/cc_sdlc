---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/artifacts.py, scripts/sdlc/build.py, scripts/sdlc/deploy.py, scripts/sdlc/evals.py, scripts/sdlc/maintain.py, scripts/sdlc/project.py, scripts/sdlc/stages.py, script"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:59:02Z" }
stale_after: "2026-09-23T01:59:02Z"
source_commit: e0523eb3d807827869c761a89aea8117eb781e36
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 25657fb47810c34d }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: maintain, resource: scripts/sdlc/maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 75052069898694d5 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 54e5024a991ef45d }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T08:32:17+10:00", digest: b3939b3fb17f6e1d }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/build.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/maintain.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`
- `scripts/sdlc/testing.py`

# Symbols
- artifacts.py (scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (scripts/sdlc/artifacts.py:L1)
- matches() (scripts/sdlc/artifacts.py:L100)
- title() (scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (scripts/sdlc/artifacts.py:L35)
- sections() (scripts/sdlc/artifacts.py:L39)
- set_section() (scripts/sdlc/artifacts.py:L44)
- meta() (scripts/sdlc/artifacts.py:L49)
- set_meta() (scripts/sdlc/artifacts.py:L54)
- status() (scripts/sdlc/artifacts.py:L58)
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
- rehearse() (scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (scripts/sdlc/deploy.py:L77)
- evals.py (scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (scripts/sdlc/evals.py:L1)
- run_eval() (scripts/sdlc/evals.py:L15)
- run() (scripts/sdlc/evals.py:L32)
- maintain.py (scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (scripts/sdlc/maintain.py:L1)
- ingest() (scripts/sdlc/maintain.py:L109)
- lesson() (scripts/sdlc/maintain.py:L117)
- tier() (scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (scripts/sdlc/maintain.py:L25)
- bands() (scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (scripts/sdlc/maintain.py:L55)
- readings() (scripts/sdlc/maintain.py:L64)
- watch() (scripts/sdlc/maintain.py:L72)
- propose() (scripts/sdlc/maintain.py:L95)
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- config() (scripts/sdlc/project.py:L102)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (scripts/sdlc/project.py:L103)
- ensure_config() (scripts/sdlc/project.py:L116)
- home() (scripts/sdlc/project.py:L122)
- features() (scripts/sdlc/project.py:L129)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L130)
- feature() (scripts/sdlc/project.py:L135)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L136)
- run_cmd() (scripts/sdlc/project.py:L146)
- Run an external tool without a shell; never raises on a non-zero exit. (scripts/sdlc/project.py:L147)
- run_git() (scripts/sdlc/project.py:L152)
- git() (scripts/sdlc/project.py:L156)
- head_commit() (scripts/sdlc/project.py:L160)
- author() (scripts/sdlc/project.py:L164)
- changed_files() (scripts/sdlc/project.py:L168)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L169)
- today() (scripts/sdlc/project.py:L174)
- read_jsonl() (scripts/sdlc/project.py:L178)
- append_jsonl() (scripts/sdlc/project.py:L182)
- read_json() (scripts/sdlc/project.py:L188)
- write_json() (scripts/sdlc/project.py:L197)
- fail() (scripts/sdlc/project.py:L80)
- attempt() (scripts/sdlc/project.py:L84)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (scripts/sdlc/project.py:L85)
- merge() (scripts/sdlc/project.py:L92)
- stages.py (scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (scripts/sdlc/stages.py:L1)
- status() (scripts/sdlc/stages.py:L104)
- prerequisite() (scripts/sdlc/stages.py:L18)
- next_command() (scripts/sdlc/stages.py:L23)
- accepted() (scripts/sdlc/stages.py:L27)
- gated() (scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (scripts/sdlc/stages.py:L33)
- create_feature() (scripts/sdlc/stages.py:L42)
- new() (scripts/sdlc/stages.py:L53)
- check() (scripts/sdlc/stages.py:L75)
- accept() (scripts/sdlc/stages.py:L86)
- next_for() (scripts/sdlc/stages.py:L94)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L95)
- run() (scripts/sdlc/testing.py:L18)

# Depends on
- [band_concepts](/modules/band-concepts.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [render](/modules/render.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
