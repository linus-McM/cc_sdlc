---
type: Module
title: conftest.py
description: "Graphify community 0: CLAUDE.md, plugin/README.md, sdlc/graph-selected-repomix-context-packs/plan.md, sdlc/graph-selected-repomix-context-packs/spec.md, tests/conftest.py, tests/test_checkpoint.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: CLAUDE, resource: CLAUDE.md, last_modified: "2026-09-29T08:42:51+10:00", digest: 9e44fdf18f345fb0 }
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-29T08:42:51+10:00", digest: c7e6b88df8690ad4 }
  - { id: plan, resource: sdlc/graph-selected-repomix-context-packs/plan.md, last_modified: "2026-09-26T16:06:32+10:00", digest: bbace73703f81509 }
  - { id: spec, resource: sdlc/graph-selected-repomix-context-packs/spec.md, last_modified: "2026-09-26T09:27:53+10:00", digest: 39b0915a5020a08c }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 44de9d075d1ea218 }
  - { id: test_checkpoint, resource: tests/test_checkpoint.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d92ef688e9ecd33c }
---

# Files
- `CLAUDE.md`
- `plugin/README.md`
- `sdlc/graph-selected-repomix-context-packs/plan.md`
- `sdlc/graph-selected-repomix-context-packs/spec.md`
- `tests/conftest.py`
- `tests/test_checkpoint.py`

# Symbols
- CLAUDE.md (CLAUDE.md:L1)
- sdlc plugin (CLAUDE.md:L1)
- Architecture (CLAUDE.md:L12)
- Conventions (CLAUDE.md:L18)
- Things Claude gets wrong (CLAUDE.md:L24)
- Commands (CLAUDE.md:L5)
- Context packs (Repomix) (plugin/README.md:L50)
- graph-selected-repomix-context-packs/plan.md (sdlc/graph-selected-repomix-context-packs/plan.md:L1)
- Plan: graph-selected repomix context packs (sdlc/graph-selected-repomix-context-packs/plan.md:L1)
- Risks (sdlc/graph-selected-repomix-context-packs/plan.md:L149)
- Proof (sdlc/graph-selected-repomix-context-packs/plan.md:L182)
- Files that change (sdlc/graph-selected-repomix-context-packs/plan.md:L4)
- Proof (sdlc/graph-selected-repomix-context-packs/spec.md:L265)
- conftest.py (tests/conftest.py:L1)
- toml_config() (tests/conftest.py:L105)
- _write() (tests/conftest.py:L106)
- FakeTools (tests/conftest.py:L135)
- Handle on the sandbox: `bin/` holds the fake tools and their call log,… (tests/conftest.py:L136)
- .__init__() (tests/conftest.py:L138)
- repo() (tests/conftest.py:L14)
- .calls() (tests/conftest.py:L141)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L15)
- .skill_dir() (tests/conftest.py:L150)
- .uninstall() (tests/conftest.py:L153)
- sandbox() (tests/conftest.py:L162)
- A bare PATH (a temp `bin/` plus git and the system dirs), temp HOME and… (tests/conftest.py:L163)
- knowledge() (tests/conftest.py:L175)
- Knowledge layer on, with fake `uv` and `graphify` in the sandbox. (tests/conftest.py:L176)
- install_fake_archify() (tests/conftest.py:L216)
- write_fake_node() (tests/conftest.py:L225)
- docs_tools() (tests/conftest.py:L236)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L237)
- packs() (tests/conftest.py:L326)
- Context packs on (knowledge layer on too), with fake `repomix`, `npm` and `uv… (tests/conftest.py:L327)
- checkpoint_on() (tests/conftest.py:L33)
- Stage-boundary checkpoints on; list it before any `accepted_*` fixture so their… (tests/conftest.py:L34)
- run() (tests/conftest.py:L40)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L41)
- _run() (tests/conftest.py:L43)
- fill() (tests/conftest.py:L49)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L50)
- accepted_intent() (tests/conftest.py:L81)
- accepted_spec() (tests/conftest.py:L89)
- accepted_plan() (tests/conftest.py:L97)
- test_checkpoint.py (tests/test_checkpoint.py:L1)
- Stage-boundary checkpoints: every accepted artifact lands in its own commit. (tests/test_checkpoint.py:L1)
- test_a_failed_commit_never_fails_the_stage() (tests/test_checkpoint.py:L104)
- test_a_merge_in_progress_defers_the_checkpoint() (tests/test_checkpoint.py:L114)
- subjects() (tests/test_checkpoint.py:L12)
- test_knowledge_refresh_is_a_boundary_that_skips_the_post_commit_hooks() (tests/test_checkpoint.py:L123)
- files_in() (tests/test_checkpoint.py:L16)
- test_plan_accept_commits_the_intent() (tests/test_checkpoint.py:L20)
- test_each_accept_is_its_own_commit() (tests/test_checkpoint.py:L26)
- test_extra_generated_files_ride_along_and_are_counted() (tests/test_checkpoint.py:L34)
- test_source_changes_are_never_swept_in() (tests/test_checkpoint.py:L43)
- test_staged_unrelated_work_stays_staged() (tests/test_checkpoint.py:L52)
- test_review_deploy_and_maintain_are_boundaries() (tests/test_checkpoint.py:L62)
- test_propose_commits_the_next_intent() (tests/test_checkpoint.py:L76)
- test_nothing_to_commit_is_not_an_error() (tests/test_checkpoint.py:L84)
- test_layer_off_never_commits() (tests/test_checkpoint.py:L91)
- test_config_can_disable_the_layer() (tests/test_checkpoint.py:L96)

# Depends on
- [accept](/modules/accept.md)
- [Order of work](/modules/order-of-work.md)
- [Order of work](/modules/order-of-work-11.md)
- [Order of work](/modules/order-of-work-8.md)
- [pathlib](/modules/pathlib.md)
- [test_deploy.py](/modules/test-deploy-py.md)

# Inferred
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [check](/modules/check.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [select](/modules/select.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
