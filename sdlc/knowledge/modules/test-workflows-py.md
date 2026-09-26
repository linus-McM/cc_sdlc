---
type: Module
title: test_workflows.py
description: "Graphify community 4: tests/test_workflows.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: test_workflows, resource: tests/test_workflows.py, last_modified: "2026-09-26T15:57:51+10:00", digest: da0adbf6c76c9a08 }
---

# Files
- `tests/test_workflows.py`

# Symbols
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
