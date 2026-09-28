---
type: Module
title: test_hooks.py
description: "Graphify community 7: sdlc/dogfood-fixes-round-two/review.md, sdlc/release-hook-hardening/plan.md, sdlc/release-hook-hardening/review.md, sdlc/release-hook-hardening/spec.md, tests/test_hooks.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: review, resource: sdlc/dogfood-fixes-round-two/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: a4e885eac6b6172a }
  - { id: plan, resource: sdlc/release-hook-hardening/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 27db3b2d8bc6d184 }
  - { id: review, resource: sdlc/release-hook-hardening/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ed3f8ea859e0a2fd }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: ceec7eaa899c3151 }
  - { id: test_hooks, resource: tests/test_hooks.py, last_modified: "2026-09-26T15:09:04+10:00", digest: 1aa3e4ed4641b099 }
---

# Files
- `sdlc/dogfood-fixes-round-two/review.md`
- `sdlc/release-hook-hardening/plan.md`
- `sdlc/release-hook-hardening/review.md`
- `sdlc/release-hook-hardening/spec.md`
- `tests/test_hooks.py`

# Symbols
- dogfood-fixes-round-two/review.md (sdlc/dogfood-fixes-round-two/review.md:L1)
- Review: Dogfood fixes round two (sdlc/dogfood-fixes-round-two/review.md:L1)
- Security (sdlc/dogfood-fixes-round-two/review.md:L10)
- Compliance (sdlc/dogfood-fixes-round-two/review.md:L15)
- release-hook-hardening/plan.md (sdlc/release-hook-hardening/plan.md:L1)
- Plan: Release hook hardening (sdlc/release-hook-hardening/plan.md:L1)
- Order of work (sdlc/release-hook-hardening/plan.md:L14)
- Files that change (sdlc/release-hook-hardening/plan.md:L4)
- Risks (sdlc/release-hook-hardening/plan.md:L49)
- Proof (sdlc/release-hook-hardening/plan.md:L62)
- release-hook-hardening/review.md (sdlc/release-hook-hardening/review.md:L1)
- Review: Release hook hardening (sdlc/release-hook-hardening/review.md:L1)
- Bugs (sdlc/release-hook-hardening/review.md:L4)
- Security (sdlc/release-hook-hardening/review.md:L9)
- release-hook-hardening/spec.md (sdlc/release-hook-hardening/spec.md:L1)
- Spec: Release hook hardening (sdlc/release-hook-hardening/spec.md:L1)
- Concerns (sdlc/release-hook-hardening/spec.md:L27)
- Open questions (sdlc/release-hook-hardening/spec.md:L31)
- Proof (sdlc/release-hook-hardening/spec.md:L34)
- test_hooks.py (tests/test_hooks.py:L1)
- no_release_approval() (tests/test_hooks.py:L10)
- test_pre_bash_denies_configured_release_command() (tests/test_hooks.py:L101)
- test_pre_bash_gated_names_come_from_config_only() (tests/test_hooks.py:L114)
- test_pre_bash_survives_bad_release_command_config() (tests/test_hooks.py:L120)
- test_post_edit_warns_when_file_not_in_plan() (tests/test_hooks.py:L129)
- test_main_reads_stdin_and_prints_json() (tests/test_hooks.py:L136)
- edit() (tests/test_hooks.py:L14)
- test_session_start_context_lists_steps() (tests/test_hooks.py:L144)
- boom() (tests/test_hooks.py:L160)
- test_session_start_repairs_a_stale_hook_block_without_auto_install() (tests/test_hooks.py:L168)
- bash() (tests/test_hooks.py:L18)
- boom() (tests/test_hooks.py:L181)
- test_session_start_silent_when_disabled() (tests/test_hooks.py:L190)
- test_post_bash_flags_stale_after_commit() (tests/test_hooks.py:L194)
- test_post_edit_names_module_concepts() (tests/test_hooks.py:L212)
- denied() (tests/test_hooks.py:L22)
- test_pre_edit_allows_ordinary_file() (tests/test_hooks.py:L26)
- test_hooks_ignore_paths_outside_root() (tests/test_hooks.py:L30)
- test_hooks_judge_symlinks_by_their_in_repo_name() (tests/test_hooks.py:L40)
- test_pre_edit_blocks_protected_path() (tests/test_hooks.py:L48)
- test_pre_edit_blocks_tests_only_while_fix_lock() (tests/test_hooks.py:L55)
- test_pre_bash_production_gate() (tests/test_hooks.py:L64)
- test_pre_bash_ignores_prose_and_heredocs() (tests/test_hooks.py:L71)
- test_pre_bash_scans_every_command_line_outside_heredocs() (tests/test_hooks.py:L80)
- test_pre_bash_fallback_matches_tokens_not_text() (tests/test_hooks.py:L92)

# Depends on
- [Order of work](/modules/order-of-work.md)
- [pathlib](/modules/pathlib.md)
- [pre_bash](/modules/pre-bash.md)
- [watch](/modules/watch.md)

# Inferred
- [hooks.py](/modules/hooks-py.md)
- [pre_bash](/modules/pre-bash.md)
- [read_json](/modules/read-json.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
