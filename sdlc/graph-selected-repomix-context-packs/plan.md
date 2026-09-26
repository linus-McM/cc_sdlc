# Plan: graph-selected repomix context packs
From: spec.md (2026-09-26). Status: accepted. Risk: high.

## Files that change
- plugin/scripts/sdlc/packs.py (new)
- plugin/templates/knowledge/repomix.config.json (new)
- plugin/scripts/sdlc/project.py
- plugin/scripts/sdlc/knowledge.py
- plugin/scripts/sdlc/cli.py
- plugin/scripts/sdlc/stages.py
- plugin/scripts/sdlc/testing.py
- plugin/scripts/sdlc/deploy.py
- plugin/commands/plan.md
- plugin/commands/design.md
- plugin/commands/build.md
- plugin/commands/test.md
- plugin/commands/maintain.md
- plugin/workflows/intent-scout.js
- plugin/workflows/design-panel.js
- plugin/workflows/plan-critic.js
- plugin/workflows/review.js
- plugin/workflows/diagnose.js
- plugin/README.md
- README.md
- CLAUDE.md
- tests/conftest.py
- tests/test_packs.py (new)
- tests/test_plan_design.py
- tests/test_build_test.py
- tests/test_knowledge.py
- tests/test_hooks.py
- tests/test_workflows.py

## Order of work
Every step: write the named test first, `sdlc build red <step>` (the suite fails), smallest change,
`sdlc build green <step>`, `sdlc build sync`, commit `build(graph-selected-repomix-context-packs): <step>`.
All new tests live in `tests/test_packs.py` unless another file is named. Every test that needs an
accepted feature lists `accepted_*` **before** `packs` (the accept runs while `SDLC_PACKS=off`), then
runs `knowledge bootstrap` itself.

1. **config** – failing tests `test_pack_config_defaults` (`project.config(root)["knowledge"]` has
   `pack_max_tokens == 0`, `pack_hops == 1`, `pack_base == "main"`) and `test_run_cmd_passes_stdin`
   (`p.run_cmd(root, ["cat"], input="a\nb")` returns stdout `a\nb`). Then add the three keys with
   comments to `DEFAULT_CONFIG` and `input: str | None = None` to `project.run_cmd`, passed through to
   `subprocess.run`.
2. **fixture** – failing test `test_packs_fixture_fakes_every_tool` (takes the new `packs` fixture:
   `repomix --version` prints `1.18.0`, `npm` and `uv tool run` log to `calls.log`, and
   `os.environ` has no `SDLC_PACKS`). Then in `tests/conftest.py`:
   - the `repo` fixture also sets `SDLC_PACKS=off` (convention of SDLC_DOCS/SDLC_WORKFLOWS/SDLC_CHECKPOINT:
     existing `knowledge` + `accepted_*` tests keep passing without a pack);
   - new `packs(knowledge, monkeypatch)` fixture: deletes `SDLC_PACKS`, writes `FAKE_REPOMIX`,
     `FAKE_NPM` and replaces `uv` with a `FAKE_UV` that also handles `tool run --from bandit==… bandit`.
   - `FAKE_REPOMIX`: logs argv to `calls.log` and stdin to `stdin.log`; reads paths from stdin; writes
     `<file path="p">…</file>` to `--output` for each path except those whose content holds
     `FAKE_SECRET` (printed in Repomix's real stdout form: `1 suspicious file(s) detected and excluded
     from the output:` then `1. <path>`) or `FAKE_DROP` (silently omitted); a file holding `FAKE_EXTRA`
     adds an unrequested `<file path="unrequested.txt">`; prints ` Total Tokens: N tokens` where N is
     the sum of file bytes, halved under `--compress`; `FAKE_REPOMIX_EXIT` in the env forces an exit code.
   - fake bandit: for each `.py` arg containing `FAKE_PASSWORD` emits a B105 result at that line and
     exits 1; `FAKE_BANDIT_CRASH` makes it exit 2; `FAKE_BANDIT_GARBAGE` prints non-JSON and exits 0;
     otherwise `{"results": []}`, exit 0.
   - `FAKE_NPM`: logs; `i -g repomix` copies `repomix.hidden` to `repomix`; `FAKE_NPM_EXIT` forces a code.
   - `packs.uninstall("repomix")` works through the existing `FakeTools.uninstall`.
3. **expand** – failing test `test_expand_is_one_hop_over_calls_plus_community` against
   `tests/fixtures/graph.json`: seed `src/web/api.py` gives `{src/web/api.py: seed,
   src/app/core.py: callee, src/web/views.py: callee}` (the `post → render` calls link) and never
   `src/app/util.py` (two hops) nor `README.md` (a `mentions` edge); plus
   `test_expand_adds_community_members` on an inline graph dict where a file shares only the seed's
   community (reason `community`). Then `packs.expand(graph, seeds, hops)`: pure, only `calls` links,
   priority seed > caller/callee > community.
4. **seeds** – failing tests `test_seeds_per_stage` (plan: backticked paths in intent "Affected users
   and systems", `path:line` suffixes stripped, directories and globs resolved over `git ls-files`;
   design: intent plus spec "Design"; build: `build.planned_files`; test: `git diff --name-only
   --diff-filter=d <pack_base>...HEAD` minus sdlc-owned; maintain: `git diff --name-only <sha>..HEAD`
   from the last production entry in deploy.json) and `test_unresolved_tokens_are_listed_not_guessed`.
   Then the `SEEDS` table and `resolve(root, tokens) -> (files, unresolved)`.
5. **admit** – failing tests `test_exclude_list_applies_after_expansion` (a `.env.local`, `id_rsa`,
   `x.pem`, `.npmrc`, `my_credentials.json`, `graphify-out/x`, an untracked file, a symlink and a
   git-ignored tracked file reach `excluded` with their rule; none reach the Repomix stdin) and
   `test_exclude_list_is_frozen` (`packs.EXCLUDE` is a tuple; no `[knowledge]` key names it). Then
   `EXCLUDE` (frozen `(glob, rule)` tuples) and `admit(root, files) -> (admitted, excluded)`.
6. **refusals** – failing tests `test_pack_refuses_deploy_and_unknown_stages`,
   `test_pack_refuses_stale_graph_by_content` (a non-ignored commit after `built_at_commit` refuses
   naming the file and `graphify update .`; an `sdlc/`-only commit does not),
   `test_checkpoint_paths_do_not_stale_the_graph` (a commit touching only `.graphifyignore`,
   `.sdlc.toml` or `CLAUDE.md` does not refuse), `test_pack_refuses_missing_graph_and_unignored_graphify_out`,
   `test_pack_refuses_dirty_admitted_file`, `test_missing_repomix_skips_advisory_and_fails_gated`
   (reason contains `npm i -g repomix`) and `test_pack_layer_off_is_skipped` (`SDLC_KNOWLEDGE=off` and
   `SDLC_PACKS=off`). Then `packs.build` preconditions in the spec's order (steps 1-6). Freshness
   exempts the SDLC home, the `[knowledge] ignore` list, `[checkpoint] paths` and `build.SDLC_OWNED`.
7. **pack** – failing tests `test_pack_writes_xml_and_manifest` (path
   `graphify-out/packs/feat/plan-<key12>.xml`, manifest fields of Requirement 1, repomix argv has
   `--stdin --config <plugin>/templates/knowledge/repomix.config.json --style xml`, never
   `--no-security-check`, `packs/.gitignore` is `*`), `test_pack_reuses_same_key` (second call
   `reused: true`, no new repomix call), `test_new_commit_rekeys_and_prunes_older_pack` and
   `test_output_scanner_refuses` (parametrised: `FAKE_SECRET`, `FAKE_DROP`, `FAKE_EXTRA`, non-zero
   exit; no .xml, no manifest, no temp file left, reason names the path and never the file text).
   Then the template config, `run_repomix`, `scan_output` (suspicious list read only from the
   Security Check block, not the top-files list), the key
   `sha256(HEAD, files, effective budget, repomix_version)` where the effective budget is
   `--max-tokens` else `pack_max_tokens`, atomic manifest-then-pack write, and pruning.
8. **bandit** – failing tests `test_bandit_finding_refuses_pack` (reason names `path:line B105`, not
   the value), `test_bandit_crash_refuses`, `test_bandit_bad_json_refuses`,
   `test_bandit_skipped_without_py_files`. Then `BANDIT = "bandit==1.9.4"` and `run_bandit` via
   `uv tool run --from <BANDIT> bandit -q -f json -t B105,B106,B107 <py files>` before Repomix.
9. **ladder** – failing tests `test_no_budget_runs_once_without_compress` (one step `full`, one
   repomix call, no `--compress`) and `test_budget_ladder_reports_every_rung` (full over budget, then
   compress, then seeds only; dropped files listed; seeds never dropped; seeds-only still over budget
   writes the pack with `over_budget: true`; `--max-tokens` overrides `pack_max_tokens`). Then `LADDER`.
10. **cli** – failing test `test_cli_knowledge_pack_row` (`run("knowledge", "pack", "plan", "--slug",
    "feat", "--max-tokens", "10")` reaches `packs.build`; `("knowledge", "pack")` not in
    `cli.BOUNDARIES`). Then the COMMANDS row and a common `--max-tokens` int flag.
11. **plan-gate** – failing tests in `tests/test_plan_design.py`:
    `test_plan_accept_needs_a_pack_at_head` (no pack refused naming `sdlc knowledge pack plan`; a pack
    built before a new commit refused; a current pack accepted), `test_plan_accept_needs_repomix`
    (reason contains `npm i -g repomix`), `test_plan_gate_skipped_visibly_when_off`, and in
    `tests/test_packs.py` `test_packs_never_committed_or_checkpointed` (fixtures `checkpoint_on`, then
    the accept flow, then `packs`: after a pack and a checkpointed `plan accept`, `git status
    --porcelain` and `checkpoint.pending` list no `graphify-out/packs` path). Then `packs.require`
    (GATED = {"plan", "test"}) and its call in `stages.accept` after `docs.check`.
12. **test-gate** – failing tests in `tests/test_build_test.py`:
    `test_review_refused_when_a_changed_file_is_missing_from_the_pack` (JSON list `missing`),
    `test_review_refused_for_a_secret_excluded_change` (names the rule),
    `test_review_skips_deleted_binary_and_sdlc_owned_changes`, `test_review_gate_skipped_visibly_when_off`
    and `test_review_accepts_a_covering_pack`. Then the diff-coverage branch of `require` (binary via
    `git diff --numstat` `-\t-`, deleted and sdlc-owned files skipped) and the call in
    `testing.review` after `docs.check`.
13. **bootstrap** – failing tests in `tests/test_knowledge.py`:
    `test_bootstrap_installs_and_updates_repomix` (install mode, repomix missing: `npm i -g repomix`;
    present and `update=True`: `npm update -g repomix`, state `updated`; check mode and SessionStart: no
    npm call) and `test_repomix_step_is_optional` (`FAKE_NPM_EXIT=1`: graph and bundle still built);
    update the existing `STEP_NAMES` and per-step state expectations in `tests/test_knowledge.py` and
    `tests/test_hooks.py` to include `"repomix": "skipped"`. Then the `repomix` STEPS row after
    `graph`, `OPTIONAL |= {"repomix"}`; `repomix_present` uses `shutil.which` (no process) and raises
    `StepSkipped("packs disabled")` under `SDLC_PACKS=off`; `install_repomix`; and
    `bootstrap(root, check, update=False)` with an update branch for present tools in `UPDATES`
    (`npm update -g repomix`, state `updated`); `cli` and `stages.new("plan")` pass `update=True`;
    SessionStart does not.
14. **workflows** – failing tests in `tests/test_workflows.py`: `test_pack_aware_workflows` (the five
    scripts read `args.pack` and their grounding says "snapshot", "data, never instructions", "say
    when"; release-readiness does not mention `pack`; meta still parses) and
    `test_commands_run_the_pack_step` (plan, design, build, test, maintain commands contain
    `knowledge pack`, in plan.md before `plan accept` and in test.md before `test review`; deploy.md
    does not). Then edit the five scripts and five commands.
15. **docs** – no new test; add the `packs.py` line to CLAUDE.md Architecture, the fixture-order rule
    (`accepted_*` before `packs`) to "Things Claude gets wrong", README.md and plugin/README.md; grep
    for stale names. Then `/simplify`, `sdlc build sync`.

## Risks
- **Riskiest steps: 11-12 (the gates).** They change `stages.accept` and `testing.review`, which every
  `accepted_*` fixture walks. Mitigation: `SDLC_PACKS=off` in the `repo` fixture (step 2), so only
  tests that take `packs` see the gates; `accepted_*` precedes `packs`; the full suite runs at every green.
- **Circular import.** cli → deploy → knowledge → testing → packs → knowledge would be half
  initialised. packs defines its own `SKIPPED` and `enabled(root)` that calls `knowledge.enabled` at
  call time, and reads no attribute of knowledge, deploy or testing at import; otherwise `testing.py`
  imports packs inside the function.
- **Bootstrap blast radius.** Existing tests pin `STEP_NAMES`, per-step states and "no process on a
  healthy project". `repomix_present` is `shutil.which` only and skips under `SDLC_PACKS=off`, so those
  tests only gain a `repomix: skipped` row (step 13).
- **Deviation 1, flagged for accept: `SDLC_PACKS=off`.** The spec names only the layer switch as the
  bypass. Without a second switch, the 14 existing tests that take `knowledge` alongside `accepted_*`
  are refused at `plan accept` (no fake Repomix). The env switch follows the SDLC_DOCS precedent, is not
  config, and the bypass stays visible (`skipped: "packs disabled"`). Rejected: reordering those
  tests' fixtures (loses their layer-on accept coverage).
- **Deviation 2: key uses the effective budget, not the ladder rung.** The rung is only known after
  Repomix runs; same HEAD, files, budget and version give the same rung.
- **Deviation 3: update only when asked.** `npm update -g repomix` runs from `knowledge bootstrap` and
  `plan new` (`update=True`), never from SessionStart: with `auto_install` on, every session start would
  otherwise spawn a networked global npm update, and STEPS installs only absent tools. Departs from
  Requirement 17's "install mode updates".
- **Deviation 4: freshness exempts checkpoint paths.** `[checkpoint] paths` (`.graphifyignore`,
  `.sdlc.toml`, `.claude/settings.local.json`) and `build.SDLC_OWNED` are committed by the plugin's own
  checkpoint; counting them would refuse every pack after the first checkpointed accept until the
  background rebuild caught up. None of them is graph input.
- **What could break:** a project without `graphify-out/` in `.graphifyignore` gets refused packs (by
  design); the real Repomix output format may drift (the scanner fails closed on any requested file
  missing, so drift refuses rather than leaks); Bandit first use needs network.
- **Rejected:** putting packs in `knowledge.py` (1080 lines already); Repomix `--include` globs instead
  of `--stdin` (path quoting); a `pack_required` config key (would let config weaken the gate); a
  separate no-commit step (its test passes before any code, so `build red` would refuse it).

## Proof
- `uv run pytest` all green, including the new `tests/test_packs.py` and the gate tests in
  `test_plan_design.py`, `test_build_test.py`, `test_knowledge.py`, `test_workflows.py`.
- `uv run ruff check plugin/scripts scripts tests && uv run ruff format --check plugin/scripts scripts
  tests`: zero findings.
- `claude plugin validate --strict plugin && claude plugin validate --strict .`: both pass.
- Manual on this repo: `sdlc knowledge pack build --slug graph-selected-repomix-context-packs` returns
  `ok: true` with a path under `graphify-out/packs/` and `git status --porcelain` shows no pack file.
