---
type: Module
title: test_build_test.py
description: "Graphify community 86: tests/test_build_test.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:55:17Z" }
stale_after: "2026-09-23T01:55:17Z"
source_commit: 0972bddc57871b4600edb500118b597e83638fbc
sources:
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
---

# Files
- `tests/test_build_test.py`

# Symbols
- test_build_test.py (tests/test_build_test.py:L1)
- test_test_review_validates_findings_file() (tests/test_build_test.py:L100)
- test_run_adds_knowledge_result_and_process_verified() (tests/test_build_test.py:L109)
- test_build_new_then_accept() (tests/test_build_test.py:L11)
- test_build_red_records_failing_run_and_rejects_passing() (tests/test_build_test.py:L15)
- test_build_green_requires_prior_red_and_passing_tests() (tests/test_build_test.py:L26)
- test_build_sync_flags_unplanned_files() (tests/test_build_test.py:L37)
- test_build_sync_ignores_sdlc_artifacts_and_config() (tests/test_build_test.py:L48)
- test_build_sync_keeps_unstaged_first_line_path_intact() (tests/test_build_test.py:L52)
- ` M path` is the first porcelain line; stripping its leading space mangled the… (tests/test_build_test.py:L53)
- test_build_fix_toggles_lock() (tests/test_build_test.py:L60)
- test_test_run_gated_on_accepted_plan() (tests/test_build_test.py:L67)
- test_build_new_gated_on_accepted_spec() (tests/test_build_test.py:L7)
- test_test_run_requires_tdd_cycle() (tests/test_build_test.py:L71)
- test_test_run_writes_report() (tests/test_build_test.py:L77)
- test_test_run_failure_reported_not_hidden() (tests/test_build_test.py:L90)

# Depends on
- [conftest.py](/modules/conftest-py.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Inferred
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
