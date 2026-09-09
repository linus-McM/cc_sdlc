---
type: Module
title: run
description: "Graphify community 82: scripts/sdlc/project.py, tests/conftest.py, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T11:57:45+10:00", digest: 48ea2a2a85d58a00 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `scripts/sdlc/project.py`
- `tests/conftest.py`
- `tests/test_plan_design.py`

# Symbols
- write_json() (scripts/sdlc/project.py:L200)
- run() (tests/conftest.py:L28)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L29)
- test_plan_design.py (tests/test_plan_design.py:L1)
- test_status_next_points_at_first_unaccepted_stage() (tests/test_plan_design.py:L100)
- test_status_next_before_any_acceptance() (tests/test_plan_design.py:L106)
- test_status_next_after_spec() (tests/test_plan_design.py:L111)
- test_status_next_walks_test_deploy_maintain() (tests/test_plan_design.py:L115)
- test_status_next_agrees_with_deploy_gate_on_failed_report() (tests/test_plan_design.py:L128)
- test_status_reports_corrupt_json_as_verdict_not_traceback() (tests/test_plan_design.py:L134)
- test_accept_publishes_feature_concept() (tests/test_plan_design.py:L141)
- test_plan_new_refuses_duplicate() (tests/test_plan_design.py:L25)
- test_plan_check_fails_on_placeholders_then_passes() (tests/test_plan_design.py:L30)
- test_plan_accept_requires_valid_intent_and_sets_status() (tests/test_plan_design.py:L46)
- test_design_gate_blocks_until_intent_accepted() (tests/test_plan_design.py:L64)
- test_design_new_blocked_without_accepted_intent() (tests/test_plan_design.py:L72)
- test_design_accept_flow() (tests/test_plan_design.py:L78)
- test_plan_new_creates_intent_from_template() (tests/test_plan_design.py:L8)
- test_status_reports_stage_progress() (tests/test_plan_design.py:L92)

# Depends on
- [conftest.py](/modules/conftest-py.md)
- [__init__.py](/modules/init-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
