---
type: Module
title: conftest.py
description: "Graphify community 2: scripts/sdlc/project.py, tests/conftest.py, tests/test_plan_design.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:33Z" }
stale_after: "2026-09-23T03:02:33Z"
source_commit: 7a6549e2e0a57fe6fe0b1257011d2e78bce58136
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
  - { id: test_plan_design, resource: tests/test_plan_design.py, last_modified: "2026-09-09T07:52:07+10:00", digest: 0ef824c0b5e9bd38 }
---

# Files
- `scripts/sdlc/project.py`
- `tests/conftest.py`
- `tests/test_plan_design.py`

# Symbols
- write_json() (scripts/sdlc/project.py:L246)
- conftest.py (tests/conftest.py:L1)
- FakeTools (tests/conftest.py:L114)
- Handle on the sandbox: `bin/` holds the fake tools and their call log,… (tests/conftest.py:L115)
- .__init__() (tests/conftest.py:L117)
- .calls() (tests/conftest.py:L120)
- .skill() (tests/conftest.py:L125)
- .skill_dir() (tests/conftest.py:L129)
- repo() (tests/conftest.py:L13)
- .uninstall() (tests/conftest.py:L132)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L14)
- sandbox() (tests/conftest.py:L141)
- A bare PATH (a temp `bin/` plus git and the system dirs), temp HOME and… (tests/conftest.py:L142)
- knowledge() (tests/conftest.py:L154)
- Knowledge layer on, with fake `uv` and `graphify` in the sandbox. (tests/conftest.py:L155)
- install_fake_archify() (tests/conftest.py:L194)
- write_fake_node() (tests/conftest.py:L203)
- docs_tools() (tests/conftest.py:L214)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L215)
- fill() (tests/conftest.py:L37)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L38)
- accepted_intent() (tests/conftest.py:L60)
- accepted_spec() (tests/conftest.py:L68)
- accepted_plan() (tests/conftest.py:L76)
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
- [fail](/modules/fail.md)
- [project.py](/modules/project-py.md)
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Inferred
- [run](/modules/run.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
