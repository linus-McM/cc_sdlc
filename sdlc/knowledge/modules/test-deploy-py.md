---
type: Module
title: test_deploy.py
description: "Graphify community 77: tests/conftest.py, tests/test_deploy.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:48:10Z" }
stale_after: "2026-09-23T01:48:10Z"
source_commit: f5370acaa20694aba335e2e3cab1cee4dc0582a5
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 17b40c0ad91b947d }
  - { id: test_deploy, resource: tests/test_deploy.py, last_modified: "2026-09-09T11:03:29+10:00", digest: dd03cc571d88f162 }
---

# Files
- `tests/conftest.py`
- `tests/test_deploy.py`

# Symbols
- load() (tests/conftest.py:L42)
- test_deploy.py (tests/test_deploy.py:L1)
- test_deploy_rehearse_fails_when_no_rollback_configured() (tests/test_deploy.py:L103)
- test_deploy_record_appends_history() (tests/test_deploy.py:L108)
- test_deploy_pr_writes_body_from_artifacts() (tests/test_deploy.py:L118)
- test_deploy_unknown_env_rejected() (tests/test_deploy.py:L126)
- tested() (tests/test_deploy.py:L13)
- test_pr_body_has_knowledge_section() (tests/test_deploy.py:L130)
- Feature with a green TDD cycle, passing test-report and review.md. (tests/test_deploy.py:L14)
- test_templates_and_config_carry_knowledge_bands_and_evals() (tests/test_deploy.py:L150)
- test_deploy_check_blocks_without_test_report() (tests/test_deploy.py:L24)
- test_deploy_check_dev_is_free() (tests/test_deploy.py:L29)
- test_deploy_check_staging_asks() (tests/test_deploy.py:L34)
- test_deploy_check_production_gate() (tests/test_deploy.py:L38)
- test_deploy_rehearse_records_rollback() (tests/test_deploy.py:L50)
- test_deploy_rehearse_runs_in_throwaway_worktree() (tests/test_deploy.py:L56)
- test_deploy_rehearse_needs_git() (tests/test_deploy.py:L66)
- test_deploy_rehearse_reports_leftover_worktree() (tests/test_deploy.py:L72)
- test_deploy_rehearse_runs_at_project_path() (tests/test_deploy.py:L87)
- A project that is a subdirectory of the repo rehearses at that same… (tests/test_deploy.py:L88)

# Depends on
- [build.py](/modules/build-py.md)
- [conftest.py](/modules/conftest-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- [run](/modules/run.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
