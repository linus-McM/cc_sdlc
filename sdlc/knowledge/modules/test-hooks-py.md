---
type: Module
title: test_hooks.py
description: "Graphify community 7: tests/test_hooks.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: test_hooks, resource: tests/test_hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 9dc3aa8cb5a97b01 }
---

# Files
- `tests/test_hooks.py`

# Symbols
- test_hooks.py (tests/test_hooks.py:L1)
- no_release_approval() (tests/test_hooks.py:L10)
- test_post_edit_warns_when_file_not_in_plan() (tests/test_hooks.py:L129)
- test_main_reads_stdin_and_prints_json() (tests/test_hooks.py:L136)
- edit() (tests/test_hooks.py:L14)
- test_session_start_context_lists_steps() (tests/test_hooks.py:L144)
- boom() (tests/test_hooks.py:L160)
- test_session_start_silent_when_disabled() (tests/test_hooks.py:L168)
- test_post_bash_flags_stale_after_commit() (tests/test_hooks.py:L172)
- test_post_edit_names_module_concepts() (tests/test_hooks.py:L190)
- test_pre_edit_allows_ordinary_file() (tests/test_hooks.py:L26)
- test_hooks_ignore_paths_outside_root() (tests/test_hooks.py:L30)
- test_hooks_judge_symlinks_by_their_in_repo_name() (tests/test_hooks.py:L40)
- test_pre_edit_blocks_protected_path() (tests/test_hooks.py:L48)
- test_pre_edit_blocks_tests_only_while_fix_lock() (tests/test_hooks.py:L55)

# Depends on
- [bash](/modules/bash.md)
- [Order of work](/modules/order-of-work-5.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
