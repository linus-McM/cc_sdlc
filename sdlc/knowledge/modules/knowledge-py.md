---
type: Module
title: knowledge.py
description: "Graphify community 0: scripts/sdlc/artifacts.py, scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:31:29Z" }
stale_after: "2026-09-22T22:31:29Z"
source_commit: 639850475d5980649e4dd44aed6fdad796bd7f4c
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T07:44:17+10:00", digest: 3e063b545e7dd897 }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T08:04:31+10:00", digest: 73d9a5df88ab9c1f }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T08:13:01+10:00", digest: c9db0e8a714ce397 }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- slugify() (scripts/sdlc/artifacts.py:L30)
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- policy_findings() (scripts/sdlc/knowledge.py:L1016)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1017)
- as_actor() (scripts/sdlc/knowledge.py:L1030)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1031)
- publish() (scripts/sdlc/knowledge.py:L1035)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1036)
- split_document() (scripts/sdlc/knowledge.py:L148)
- enabled() (scripts/sdlc/knowledge.py:L158)
- cfg() (scripts/sdlc/knowledge.py:L165)
- bundle_dir() (scripts/sdlc/knowledge.py:L169)
- graph_path() (scripts/sdlc/knowledge.py:L173)
- skill_path() (scripts/sdlc/knowledge.py:L177)
- state_path() (scripts/sdlc/knowledge.py:L182)
- read_state() (scripts/sdlc/knowledge.py:L186)
- write_state() (scripts/sdlc/knowledge.py:L190)
- hooks_dir() (scripts/sdlc/knowledge.py:L197)
- Git's hooks directory without spawning git: .git or the worktree's common dir,… (scripts/sdlc/knowledge.py:L198)
- post_commit_path() (scripts/sdlc/knowledge.py:L211)
- tool() (scripts/sdlc/knowledge.py:L215)
- bundle_skeleton() (scripts/sdlc/knowledge.py:L219)
- index.md and log.md from the templates; `refresh` rewrites them from real… (scripts/sdlc/knowledge.py:L220)
- hook_block() (scripts/sdlc/knowledge.py:L233)
- our_block_present() (scripts/sdlc/knowledge.py:L238)
- install_hook() (scripts/sdlc/knowledge.py:L243)
- Idempotent: replaces an existing sdlc block, otherwise appends after everything… (scripts/sdlc/knowledge.py:L244)
- unhook() (scripts/sdlc/knowledge.py:L254)
- uv_install_command() (scripts/sdlc/knowledge.py:L273)
- find_uv() (scripts/sdlc/knowledge.py:L278)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (scripts/sdlc/knowledge.py:L279)
- StepFailed (scripts/sdlc/knowledge.py:L293)
- bootstrap() (scripts/sdlc/knowledge.py:L297)
- scalar() (scripts/sdlc/knowledge.py:L39)
- graph_commit() (scripts/sdlc/knowledge.py:L426)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L434)
- artifacts_agree() (scripts/sdlc/knowledge.py:L443)
- bundle_counts() (scripts/sdlc/knowledge.py:L449)
- status() (scripts/sdlc/knowledge.py:L460)
- now_iso() (scripts/sdlc/knowledge.py:L494)
- plugin_version() (scripts/sdlc/knowledge.py:L498)
- head_commit() (scripts/sdlc/knowledge.py:L503)
- load_graph() (scripts/sdlc/knowledge.py:L507)
- is_code() (scripts/sdlc/knowledge.py:L515)
- Graphify tags code, document and rationale nodes; only code communities become… (scripts/sdlc/knowledge.py:L516)
- flow() (scripts/sdlc/knowledge.py:L52)
- community_labels() (scripts/sdlc/knowledge.py:L522)
- communities() (scripts/sdlc/knowledge.py:L532)
- Graphify communities big enough for a Module concept, with a stable slug each. (scripts/sdlc/knowledge.py:L533)
- god_nodes() (scripts/sdlc/knowledge.py:L553)
- concept() (scripts/sdlc/knowledge.py:L561)
- link() (scripts/sdlc/knowledge.py:L570)
- section() (scripts/sdlc/knowledge.py:L574)
- first_line() (scripts/sdlc/knowledge.py:L578)
- feature_files() (scripts/sdlc/knowledge.py:L585)
- features() (scripts/sdlc/knowledge.py:L590)
- module_concepts() (scripts/sdlc/knowledge.py:L595)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L60)
- review_counts() (scripts/sdlc/knowledge.py:L630)
- feature_status() (scripts/sdlc/knowledge.py:L640)
- feature_concepts() (scripts/sdlc/knowledge.py:L652)
- hub_concepts() (scripts/sdlc/knowledge.py:L681)
- first_sentence() (scripts/sdlc/knowledge.py:L709)
- lesson_concepts() (scripts/sdlc/knowledge.py:L713)
- band_concepts() (scripts/sdlc/knowledge.py:L742)
- signature() (scripts/sdlc/knowledge.py:L767)
- Content identity: the builder's own keys plus the body; provenance and trust… (scripts/sdlc/knowledge.py:L768)
- git_last_modified() (scripts/sdlc/knowledge.py:L772)
- render_concept() (scripts/sdlc/knowledge.py:L779)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L780)
- write_index() (scripts/sdlc/knowledge.py:L797)
- write_root_index() (scripts/sdlc/knowledge.py:L808)
- append_log() (scripts/sdlc/knowledge.py:L820)
- digest() (scripts/sdlc/knowledge.py:L836)
- sources_changed() (scripts/sdlc/knowledge.py:L841)
- True when any source's content differs from the digest recorded at generation… (scripts/sdlc/knowledge.py:L842)
- reconcile() (scripts/sdlc/knowledge.py:L847)
- Concept files nothing generated any more: tombstone when every source is… (scripts/sdlc/knowledge.py:L848)
- behind() (scripts/sdlc/knowledge.py:L880)
- refresh() (scripts/sdlc/knowledge.py:L887)
- concept_files() (scripts/sdlc/knowledge.py:L960)
- concepts_for() (scripts/sdlc/knowledge.py:L968)
- Bundle-relative module concept paths whose `# Files` section lists `rel`; empty… (scripts/sdlc/knowledge.py:L969)
- check() (scripts/sdlc/knowledge.py:L984)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L985)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [build.py](/modules/build-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
