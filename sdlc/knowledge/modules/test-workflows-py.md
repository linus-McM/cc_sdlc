---
type: Module
title: test_workflows.py
description: "Graphify community 4: scripts/bump_version.py, tests/test_bump.py, tests/test_workflows.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: bump_version, resource: scripts/bump_version.py, last_modified: "2026-09-25T17:29:11+10:00", digest: 040d927133b4dcab }
  - { id: test_bump, resource: tests/test_bump.py, last_modified: "2026-09-25T17:29:11+10:00", digest: 2984f92c38ea221e }
  - { id: test_workflows, resource: tests/test_workflows.py, last_modified: "2026-09-26T16:35:55+10:00", digest: da0adbf6c76c9a08 }
---

# Files
- `scripts/bump_version.py`
- `tests/test_bump.py`
- `tests/test_workflows.py`

# Symbols
- bump_version.py (scripts/bump_version.py:L1)
- Bump the plugin version in every file that carries it (plugin.json is the… (scripts/bump_version.py:L2)
- parse() (scripts/bump_version.py:L23)
- bump() (scripts/bump_version.py:L30)
- current() (scripts/bump_version.py:L39)
- write() (scripts/bump_version.py:L43)
- Set `version` in plugin.json, marketplace.json, pyproject.toml and uv.lock,… (scripts/bump_version.py:L44)
- part_from_labels() (scripts/bump_version.py:L57)
- main() (scripts/bump_version.py:L61)
- test_bump.py (tests/test_bump.py:L1)
- tree() (tests/test_bump.py:L12)
- test_bump_parts() (tests/test_bump.py:L22)
- test_write_syncs_every_version_file() (tests/test_bump.py:L30)
- test_main_bumps_only_when_head_equals_base() (tests/test_bump.py:L42)
- test_repository_lock_matches_the_plugin_version() (tests/test_bump.py:L52)
- test_part_from_labels() (tests/test_bump.py:L57)
- test_workflows.py (tests/test_workflows.py:L1)
- test_env_off_switches() (tests/test_workflows.py:L104)
- test_session_start_sets_workflow_env_once() (tests/test_workflows.py:L114)
- test_env_leaves_projects_without_sdlc_config_alone() (tests/test_workflows.py:L122)
- test_env_refuses_keys_outside_the_workflow_namespace() (tests/test_workflows.py:L129)
- test_every_plugin_source_file_is_tracked() (tests/test_workflows.py:L136)
- test_session_start_reports_unreadable_settings_without_failing() (tests/test_workflows.py:L142)
- test_pack_aware_workflows() (tests/test_workflows.py:L152)
- test_commands_run_the_pack_step() (tests/test_workflows.py:L160)
- workflows_on() (tests/test_workflows.py:L17)
- settings() (tests/test_workflows.py:L22)
- test_every_stage_ships_one_workflow_script() (tests/test_workflows.py:L26)
- test_workflow_meta_is_a_literal_whose_phases_match_the_body() (tests/test_workflows.py:L34)
- test_workflow_script_parses_as_an_es_module() (tests/test_workflows.py:L46)
- test_each_stage_command_calls_its_workflow() (tests/test_workflows.py:L55)
- test_list_reports_the_catalog() (tests/test_workflows.py:L61)
- test_env_writes_workflow_variables_into_local_settings() (tests/test_workflows.py:L67)
- test_env_keeps_existing_settings_and_user_values() (tests/test_workflows.py:L75)
- test_env_refuses_to_overwrite_unreadable_settings() (tests/test_workflows.py:L87)
- test_env_exports_to_the_session_env_file() (tests/test_workflows.py:L95)

# Depends on
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
