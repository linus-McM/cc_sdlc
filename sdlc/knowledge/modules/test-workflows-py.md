---
type: Module
title: test_workflows.py
description: "Graphify community 4: scripts/bump_version.py, tests/test_bump.py, tests/test_workflows.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: bump_version, resource: scripts/bump_version.py, last_modified: "2026-09-09T15:02:31+10:00", digest: cefef3eae8e6c4bd }
  - { id: test_bump, resource: tests/test_bump.py, last_modified: "2026-09-09T15:02:31+10:00", digest: b17b9763b42ddb1d }
  - { id: test_workflows, resource: tests/test_workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: a006d4dbeef09c2e }
---

# Files
- `scripts/bump_version.py`
- `tests/test_bump.py`
- `tests/test_workflows.py`

# Symbols
- bump_version.py (scripts/bump_version.py:L1)
- Bump the plugin version in every file that carries it (plugin.json is the… (scripts/bump_version.py:L2)
- parse() (scripts/bump_version.py:L22)
- bump() (scripts/bump_version.py:L29)
- current() (scripts/bump_version.py:L38)
- write() (scripts/bump_version.py:L42)
- Set `version` in plugin.json, marketplace.json and pyproject.toml, keeping each… (scripts/bump_version.py:L43)
- part_from_labels() (scripts/bump_version.py:L53)
- main() (scripts/bump_version.py:L57)
- test_bump.py (tests/test_bump.py:L1)
- tree() (tests/test_bump.py:L12)
- test_bump_parts() (tests/test_bump.py:L21)
- test_write_syncs_every_version_file() (tests/test_bump.py:L29)
- test_main_bumps_only_when_head_equals_base() (tests/test_bump.py:L39)
- test_part_from_labels() (tests/test_bump.py:L49)
- test_workflows.py (tests/test_workflows.py:L1)
- test_env_off_switches() (tests/test_workflows.py:L104)
- test_session_start_sets_workflow_env_once() (tests/test_workflows.py:L114)
- test_env_leaves_projects_without_sdlc_config_alone() (tests/test_workflows.py:L122)
- test_env_refuses_keys_outside_the_workflow_namespace() (tests/test_workflows.py:L129)
- test_every_plugin_source_file_is_tracked() (tests/test_workflows.py:L136)
- test_session_start_reports_unreadable_settings_without_failing() (tests/test_workflows.py:L142)
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
- [hooks.py](/modules/hooks-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
