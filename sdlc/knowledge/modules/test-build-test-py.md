---
type: Module
title: test_build_test.py
description: "Graphify community 8: plugin/README.md, plugin/scripts/sdlc/workflows.py, tests/test_build_test.py, tests/test_evals.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 2e559b282f80c004 }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
  - { id: test_build_test, resource: tests/test_build_test.py, last_modified: "2026-09-09T07:52:07+10:00", digest: a23e976c32f40b84 }
  - { id: test_evals, resource: tests/test_evals.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 107908af8f9fb539 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/workflows.py`
- `tests/test_build_test.py`
- `tests/test_evals.py`

# Symbols
- Stage workflows (dynamic Workflow scripts) (plugin/README.md:L55)
- workflows.py (plugin/scripts/sdlc/workflows.py:L1)
- Stage workflows: the catalog of plugin Workflow scripts and the env that turns… (plugin/scripts/sdlc/workflows.py:L1)
- enabled() (plugin/scripts/sdlc/workflows.py:L32)
- meta() (plugin/scripts/sdlc/workflows.py:L36)
- The script's `export const meta` literal (written as JSON so Python can read… (plugin/scripts/sdlc/workflows.py:L37)
- catalog() (plugin/scripts/sdlc/workflows.py:L43)
- env() (plugin/scripts/sdlc/workflows.py:L47)
- Merge `[workflows.env]` into the local settings; report which keys were written… (plugin/scripts/sdlc/workflows.py:L48)
- export() (plugin/scripts/sdlc/workflows.py:L71)
- Append `export K=V` lines to the SessionStart env file, once each, so this… (plugin/scripts/sdlc/workflows.py:L72)
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
- test_evals.py (tests/test_evals.py:L1)
- write_eval() (tests/test_evals.py:L14)
- test_evals_run_all_and_gate_on_threshold() (tests/test_evals.py:L19)
- test_evals_pass_when_all_checks_green() (tests/test_evals.py:L33)
- test_evals_without_suite_is_a_clear_failure() (tests/test_evals.py:L41)
- fake_claude() (tests/test_evals.py:L6)

# Depends on
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [Order of work](/modules/order-of-work.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Status next pointer](/features/status-next-pointer.md)
