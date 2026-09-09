---
type: Module
title: toml_config
description: "Graphify community 5: tests/conftest.py, tests/test_hooks.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
  - { id: test_hooks, resource: tests/test_hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 9dc3aa8cb5a97b01 }
---

# Files
- `tests/conftest.py`
- `tests/test_hooks.py`

# Symbols
- toml_config() (tests/conftest.py:L84)
- test_hooks.py (tests/test_hooks.py:L1)
- no_release_approval() (tests/test_hooks.py:L10)
- test_pre_bash_denies_configured_release_command() (tests/test_hooks.py:L101)
- test_pre_bash_gated_names_come_from_config_only() (tests/test_hooks.py:L114)
- test_pre_bash_survives_bad_release_command_config() (tests/test_hooks.py:L120)
- test_post_edit_warns_when_file_not_in_plan() (tests/test_hooks.py:L129)
- test_main_reads_stdin_and_prints_json() (tests/test_hooks.py:L136)
- edit() (tests/test_hooks.py:L14)
- test_session_start_context_lists_steps() (tests/test_hooks.py:L144)
- test_session_start_silent_when_disabled() (tests/test_hooks.py:L168)
- test_post_bash_flags_stale_after_commit() (tests/test_hooks.py:L172)
- bash() (tests/test_hooks.py:L18)
- test_post_edit_names_module_concepts() (tests/test_hooks.py:L190)
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
- [build.py](/modules/build-py.md)
- [run](/modules/run.md)

# Inferred
- [run](/modules/run.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
