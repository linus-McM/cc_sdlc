# Spec: Graphify and OKF knowledge base integration

From: intent.md (2026-09-09). Status: accepted. Risk: high.

## Requirements

Traced to intent.md Proposed outcome items (PO1..PO7). "Verdict" means the one JSON dict `cli.main` returns.

1. (PO1) `sdlc knowledge bootstrap` returns a verdict with `steps: [{name, state, detail}]` where
   `state` is `present`, `installed`, `built`, `skipped` or `failed`, and `ok` is true only when
   no step is `failed`. Steps, in order: `uv` on PATH; `graphify` on PATH (installs with
   `uv tool install graphifyy` when absent and `uv` is present); Claude skill file present
   (`graphify install --platform claude`); git hooks installed (`graphify hook install`, checked
   via `graphify hook status`); `.graphifyignore` present with the plugin's exclusions; graph
   present (`graphify update .` when `graphify-out/graph.json` is absent); bundle present
   (generated when `<bundle>/index.md` is absent); `CLAUDE.md` pointer present (when configured).
2. (PO1) When every step is already satisfied, bootstrap performs no subprocess call other than
   `graphify hook status`, which is skipped when a cached `<bundle>/.state.json` says hooks were
   verified for the current `.git/hooks/post-commit` mtime. Proven by a test that monkeypatches
   `subprocess.run` to raise and asserts a healthy project still returns `ok`.
3. (PO1) `[knowledge] enabled = false` makes every `knowledge` action return
   `{"ok": true, "skipped": "knowledge disabled"}` and makes the `SessionStart` and post-commit
   paths exit silently. When `uv` is absent the bootstrap step for it is `failed` with a reason
   naming `uv`, later steps are `skipped`, and no `pip` call is made.
4. (PO1) Every install step is reported before it runs: the verdict's step list includes the exact
   command executed in `detail`, and the `SessionStart` hook prints the verdict as
   `additionalContext` so the installs are visible in the session.
5. (PO2) `sdlc knowledge refresh` regenerates the bundle from `graphify-out/graph.json` plus the
   sdlc artifacts, appends one dated entry to `<bundle>/log.md`, records `HEAD` and an
   incremented `updates` counter in `<bundle>/.state.json`, and returns
   `{ok, concepts, created, updated, tombstoned, source_commit}`. Running it twice on the same
   commit changes no file except `.state.json`.
6. (PO2) `graphify hook install` is the only writer of Graphify's git hooks. The plugin appends
   its own marker-delimited block (`# sdlc-knowledge-start` .. `# sdlc-knowledge-end`) to the
   same `post-commit` file, after Graphify's, which runs `python3 <plugin>/scripts/sdlc.py knowledge refresh --quiet` detached, honouring `GRAPHIFY_SKIP_HOOK=1`, skipping when the commit
   touched only `<bundle>/` or `graphify-out/`, and skipping in linked worktrees. The block is
   idempotent (re-install replaces it) and removable (`sdlc knowledge unhook`).
7. (PO2) The plugin's `PostToolUse` Bash handler `post-bash`, on a command whose tokens contain
   `git commit`, calls `knowledge.status` and, when the graph or bundle is behind `HEAD`, emits
   `additionalContext` naming the stale index and the command to run. It never runs the refresh
   itself (the git hook does; this is the visibility path when the hook did not fire).
8. (PO3) `sdlc knowledge status` returns `{ok, graph: {commit, behind, artifacts_agree, last_rebuild}, bundle: {commit, behind, updates, concepts, stale, unverified, draft}, rebuild: "incremental" | "clean", reasons}` where `behind` is the number of commits from the
   recorded commit to `HEAD` (`git rev-list --count`), `artifacts_agree` is false when
   `graph.json`, `GRAPH_REPORT.md` and `graph.html` mtimes differ by more than
   `[knowledge] artifact_skew_seconds` (default 300), and `last_rebuild` is the last line of
   `~/.cache/graphify-rebuild.log` (or `GRAPHIFY_REBUILD_LOG`) when readable. `ok` is false with
   a reason when either index is behind by more than `[knowledge] max_behind` commits (default 1)
   or the bundle's `updates` counter reached `[knowledge] clean_every` (default 5): then
   `rebuild` is `clean` and the next `bootstrap` or `refresh` runs `graphify update . --force`
   and a full bundle rewrite, resetting the counter.
9. (PO4) The bundle root is `[knowledge] bundle` (default `sdlc/knowledge`) under the project
   root. `index.md` at the root carries `okf_version: "0.2"` frontmatter and one section per
   concept directory; every subdirectory has its own `index.md`; `log.md` uses `## YYYY-MM-DD`
   headings, newest first, entries `* **Creation**|**Update**|**Deprecation**: ...`.
10. (PO4) Concept documents are generated deterministically, one file per source:
    - `features/<slug>.md` `type: Feature`: title from intent, description from the first line of
      Problem, sections `# Problem`, `# Outcome`, `# Requirements` (spec), `# Files` (plan, each
      as a link to the `modules/` concept owning that file when one exists), `# Review` (review.md
      counts), `# Status` (artifact acceptance and deploy state).
    - `modules/<community-slug>.md` `type: Module`: one per Graphify community whose nodes span at
      least `[knowledge] min_community_nodes` (default 3) code nodes; description names the files;
      sections `# Files`, `# Symbols` (labels with `source_file:source_location`), `# Depends on`
      (links to other modules reached by EXTRACTED edges; INFERRED edges listed separately under
      `# Inferred`), `# Features` (back-links).
    - `hubs/<label-slug>.md` `type: Hub`: top `[knowledge] god_nodes` (default 10) from
      `graphify god-nodes --json`; links to its module.
    - `lessons/<date>-<n>.md` `type: Lesson`: one per line of `sdlc/lessons.md`; `supersedes`
      set when a later lesson line contains the earlier one's first sentence verbatim.
    - `bands/<metric>.md` `type: Control Band`: one per `[metrics.*]` in `sdlc/bands.toml`,
      with the latest reading from `metrics.jsonl`.
      Every concept's frontmatter: `type`, `title`, `description`, `resource` (repo-relative path),
      `tags`, `generated: {by: "sdlc/<plugin version>", at}`, `status`, `sources: [{id, resource, last_modified}]`, `source_commit` (organisational extension), `stale_after` (generation time
      plus `[knowledge] stale_after_days`, default 14).
11. (PO4) Invalidation: on refresh, a concept whose `sources[].resource` paths have a commit newer
    than its `source_commit` is regenerated and its `status` reset to `draft` even if it was
    `stable`, and `log.md` records the update. A concept whose every source path is confirmed
    absent from the tree (`Path.exists()` false, checked at the repo root) is rewritten as a
    tombstone: `status: deprecated`, body `# Deprecated` with a link to the replacement when a
    concept with the same title exists elsewhere. A concept whose sources cannot be resolved
    (no `sources`, or a path outside the repo) is kept unchanged and listed in the verdict under
    `unresolved`; nothing is deleted.
12. (PO5) Generation never writes a `verified` entry whose `by` starts with `human:`. `sdlc <stage> accept` (plan, design, build) calls `knowledge.publish(feature, actor)` which appends
    `{by: "human:<git user.name slug>", at}` to `verified` on `features/<slug>.md` and sets
    `status: stable`; a refresh that regenerates the concept from unchanged sources preserves
    `verified`; regeneration after a source change keeps the history but resets `status: draft`
    (requirement 11), so `verified` alone never implies current. `sdlc test run` adds
    `{by: "process:sdlc-test", at}` when the report passes.
13. (PO5) `sdlc knowledge check` returns three lists in one verdict: `conformance` (SPEC.md §11:
    unparseable frontmatter, missing or empty `type`, reserved-file structure), `policy`
    (organisational: missing `title`, `generated`, `source_commit`; `verified` with a `human:`
    actor on a `draft` concept; a `stale_after` in the past on a `stable` concept), `trust`
    (per-concept tier: unverified, machine-confirmed, human-reviewed; counts). `ok` is false only
    on `conformance` findings. Broken links, unknown types and unknown keys are never findings.
14. (PO6) `commands/*.md` change: every stage command starts with `sdlc knowledge bootstrap` and
    reads `<bundle>/index.md` before any other file; build.md, test.md and maintain.md name
    `graphify query "<question>"` and `graphify affected "<symbol>"` as the first tool for
    call-graph questions and say INFERRED edges are hints. `hooks.post_edit` adds to its context
    the `modules/` concepts whose `# Files` list the edited path. `sdlc test run` runs
    `knowledge check` after the configured commands and fails on `conformance` findings.
    `deploy.pr_body` adds a `### Knowledge` section with `git diff --stat main...HEAD -- <bundle>`.
    `sdlc maintain ingest` gains no new syntax; `knowledge refresh` appends readings
    `knowledge_nodes`, `knowledge_communities`, `knowledge_stale`, `knowledge_unverified`,
    `knowledge_behind` to `metrics.jsonl`, and `templates/bands.toml` gains bands for
    `knowledge_stale` and `knowledge_behind` with `bad = "high"`.
15. (PO6) Agents: `agents/reviewer.md` and `agents/verifier.md` say to read `<bundle>/index.md`
    first and may run `graphify query`; their `tools` lists are unchanged (`Bash` already covers
    it).
16. (PO7) `evals/knowledge-questions.json` holds five fixed questions about this repo with
    deterministic checks; `docs/knowledge-measurement.md` records the token counts of answering
    them from raw reads versus bundle plus `graphify query`, on one commit, then after a rename
    and a deletion. Numbers are recorded as measured; no target is asserted by a test.
17. (Constraints) All new code is stdlib; `graphify` and `uv` are invoked through
    `project.run_cmd`-style subprocess helpers with `check=False`; no hook path runs
    `graphify label` or any LLM; every current test passes unchanged; `[knowledge] enabled = false` leaves every existing verdict byte-identical.

## Design

### Components

- `scripts/sdlc/knowledge.py` (new, the only new module). Public functions, each returning a
  verdict or raising `Blocked`: `bootstrap(root)`, `status(root)`, `refresh(root, quiet=False)`,
  `check(root)`, `publish(root, feature, actor)`, `unhook(root)`. Private helpers grouped as:
  tools (`which`, `run_tool`, `graphify_python`), graph (`load_graph`, `communities`,
  `god_nodes`), sources (`feature_concepts`, `module_concepts`, `hub_concepts`,
  `lesson_concepts`, `band_concepts`), bundle (`write_concept`, `write_index`, `append_log`,
  `tombstone`, `state`), frontmatter (`dump_frontmatter`, `parse_frontmatter`: a 60-line
  YAML subset writer/reader for scalars, flat lists, `{by, at}` maps and lists of maps; the
  reader tolerates anything it cannot parse by returning the raw block, which `check` reports as
  a conformance finding only when no `type:` line is present).
- `scripts/sdlc/cli.py`: `("knowledge", action)` entries for `bootstrap`, `status`, `refresh`,
  `check`, `unhook`, gate `None`; `--quiet` flag on the common parser.
- `scripts/sdlc/project.py`: `DEFAULT_CONFIG` gains
  ```
  [knowledge]
  enabled = true
  auto_install = false      # SessionStart installs missing tools only when true; stage commands always do
  bundle = "sdlc/knowledge"
  claude_md_pointer = true
  clean_every = 5
  max_behind = 1
  stale_after_days = 14
  artifact_skew_seconds = 300
  min_community_nodes = 3
  god_nodes = 10
  ignore = ["sdlc/*/references/", "graphify-out/", ".venv/"]
  ```

  and `run_cmd(root, argv, env=None)` (list form, no shell) beside `run_git`.
- `scripts/sdlc/hooks.py`: `session_start(payload, root)` calls `knowledge.bootstrap` and returns
  `additionalContext` with the step list; `post_bash` (new PostToolUse handler) per requirement 7;
  `post_edit` appends module concepts per requirement 14. `HANDLERS` gains `session-start` and
  `post-bash`.
- `hooks/hooks.json`: `SessionStart` entry (`matcher` omitted, `timeout: 120` because the first
  run may install) and a `PostToolUse` `Bash` entry (`timeout: 10`).
- `scripts/sdlc/stages.py` `accept`: after setting the status, `knowledge.publish(root, feature, p.author(root))` when enabled; `create_feature` calls `knowledge.bootstrap` so `plan new` is a
  bootstrap point too.
- `scripts/sdlc/testing.py` `run`: appends the `knowledge check` result as a fourth entry in
  `results` named `knowledge` (exit 1 on conformance findings) and calls `publish` with the
  `process:sdlc-test` actor on pass. `deploy.py` `pr_body`: Knowledge section. `maintain.py`:
  unchanged code; `knowledge.refresh` writes readings through `maintain.ingest`.
- `templates/knowledge/`: `concept.md` (frontmatter skeleton), `index.md`, `log.md`,
  `claude-pointer.md` (the marker-delimited two-line block), `post-commit.sh` (the plugin's hook
  block). `templates/bands.toml` gains the two knowledge bands. `templates/evals/knowledge-questions.json`.
- `.graphifyignore` (project file, written by bootstrap from `[knowledge] ignore`, never
  overwritten when present): keeps `references/` packs and `graphify-out/` out of the graph;
  measured today the repomix pack is the top god node (degree 102) without it.
- `.gitignore` gains `graphify-out/`; `.gitattributes` untouched by us (Graphify's merge driver
  line is theirs and only matters when `graph.json` is tracked, which it is not).

### Data flow

1. Session start or any stage command -> `knowledge.bootstrap`: read config; when disabled
   return skipped; check `uv`, `graphify` (PATH), skill file, hook markers, `.graphifyignore`,
   `graphify-out/graph.json`, `<bundle>/index.md`, `CLAUDE.md` pointer; install or build what is
   missing, in that order, stop at the first `failed`; return steps.
2. Commit -> Graphify block in `post-commit` rebuilds `graphify-out/` detached and logs -> plugin
   block runs `knowledge refresh --quiet` detached after a `graphify check-update .`-style wait
   loop of at most 60 s on `graph.json` mtime (so the bundle is built from the new graph, not the
   old one); when the graph did not update in time, refresh still runs and `status` shows the
   graph behind.
3. `refresh`: `load_graph` (`graph.json`: `nodes[].community`, `community_name`, `source_file`,
   `source_location`, `_origin`; `links[].relation`, `confidence`; `built_at_commit`) plus
   `.graphify_labels.json` for community names; `god-nodes --json`; read `sdlc/*/{intent,spec, plan,review}.md`, `test-report.json`, `deploy.json`, `lessons.md`, `bands.toml`,
   `metrics.jsonl`; build the concept set in memory; for each existing concept decide keep /
   update / tombstone per requirement 11 using `git log -1 --format=%H -- <path>` per source
   path (one `git log` per distinct path, cached); write changed files only; write indexes;
   append `log.md`; write `.state.json` `{commit, updates, ts, hooks_mtime}`; ingest metrics.
4. `status`: read `.state.json`, `graph.json` header (only the first 4 KB is scanned for
   `built_at_commit` to stay cheap), mtimes, rebuild log tail, `git rev-list --count`.
5. Accept -> `publish` -> `verified` appended, `status: stable`, `log.md` entry.

### Interfaces

- Bundle layout:
  ```
  sdlc/knowledge/
    index.md            okf_version: "0.2"; sections Features, Modules, Hubs, Lessons, Bands
    log.md
    .state.json         {commit, updates, ts, hooks_mtime}   (tracked; small)
    features/index.md, features/<slug>.md
    modules/index.md,  modules/<community-slug>.md
    hubs/index.md,     hubs/<label-slug>.md
    lessons/index.md,  lessons/<date>-<n>.md
    bands/index.md,    bands/<metric>.md
  ```
- Frontmatter emitted (example, `features/rehearsal-and-band-nits.md`):
  ```
  ---
  type: Feature
  title: Rehearsal and band nits
  description: Five nits left open by the review of dogfood-fixes-round-two.
  resource: sdlc/rehearsal-and-band-nits
  tags: [feature, accepted, released]
  status: stable
  generated: { by: sdlc/0.2.0, at: 2026-09-09T07:30:00Z }
  verified:
    - { by: process:sdlc-test, at: 2026-09-08T05:50:00Z }
    - { by: human:linus-mcmanamey, at: 2026-09-08T05:55:00Z }
  stale_after: 2026-09-23T07:30:00Z
  source_commit: 8409f99e...
  sources:
    - { id: intent, resource: sdlc/rehearsal-and-band-nits/intent.md, last_modified: 2026-09-08T05:40:00Z }
  ---
  ```
- `CLAUDE.md` pointer block (appended once, between `<!-- sdlc-knowledge-start -->` and
  `<!-- sdlc-knowledge-end -->`): "Knowledge base: read `sdlc/knowledge/index.md` first; for
  call-graph questions run `graphify query \"<question>\"` (graphify-out/ is the AST graph;
  INFERRED edges are hints)."
- Hook block in `.git/hooks/post-commit` (appended after Graphify's, same guards):
  ```
  # sdlc-knowledge-start
  [ "${GRAPHIFY_SKIP_HOOK:-0}" = "1" ] && exit 0
  <worktree guard, rebase/merge guard as Graphify's>
  CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null)
  echo "$CHANGED" | grep -qv -e '^sdlc/knowledge/' -e '^graphify-out/' || exit 0
  ( sleep 0; for i in $(seq 1 30); do [ graphify-out/graph.json -nt .git/HEAD ] && break; sleep 2; done;
    python3 "<plugin root>/scripts/sdlc.py" knowledge refresh --quiet ) >>"${HOME}/.cache/sdlc-knowledge.log" 2>&1 &
  # sdlc-knowledge-end
  ```

  `<plugin root>` is `PLUGIN_ROOT` at install time; `bootstrap` re-installs the block when the
  recorded path no longer exists.
- Verdict shapes are fixed in requirements 1, 5, 8, 13.

### Changes to existing behaviour

- `stages.accept` gains one call; `testing.run` gains one result row and may now fail on bundle
  conformance (only when enabled). `hooks.post_edit` context grows by one line per module hit.
  `deploy.pr_body` gains a section. `project.DEFAULT_CONFIG` gains a table (deep-merge keeps old
  `.sdlc.toml` files valid). `hooks.json` gains two entries. `plugin.json` version to `0.2.0`
  (the `generated.by` actor uses it).
- No change to `cli.main` verdict handling, `Blocked`, gating order, band maths, rehearsal.

## Concerns

1. Machine-level installs from a hook (`uv tool install graphifyy`, `~/.claude/skills/graphify`,
   `.git/hooks/*`). Policy conflict: CLAUDE.md "never route around a hook" and the session rule
   "confirm hard-to-reverse actions" versus the intent's "install on first use". Resolution
   proposed: installs happen only from `bootstrap`; the `SessionStart` path runs `bootstrap` in
   `--check` mode (reports what is missing, installs nothing) unless `[knowledge] auto_install = true` is set in the project's `.sdlc.toml`, which this repo sets. Stage commands run the full
   bootstrap because the user invoked them. Owner: Linus. Resolved 2026-09-09: check-only
   unless `auto_install = true`; `auto_install` added to the `[knowledge]` table (default false;
   this repo sets true).
2. Third-party code executes on every commit with the developer's credentials (Graphify's hook
   and ours). Graphify's block already runs on machines with `graphify hook install`; ours adds
   a Python process reading the repo. Mitigation: no network, no LLM, `GRAPHIFY_SKIP_HOOK=1`
   opt-out honoured by both blocks, log file per hook, and `sdlc knowledge unhook` removes ours
   without touching Graphify's. Owner: Linus.
3. Graphify defects documented in article 7 (ghost nodes after symbol deletion, destructive merge
   in `--update`, manifest path mismatch) mean the module concepts can be wrong even when fresh.
   Mitigation is the `clean_every` forced `--force` rebuild and the `stale`/`behind` bands;
   correctness of `graph.json` itself is out of our control and the spec says so in
   `docs/knowledge-measurement.md`. Owner: Linus, accepted risk.
4. The bundle is committed and derived from `graph.json` which is not: a fresh clone has a bundle
   older than its graph until the post-checkout hook and a refresh run. `status` reports this as
   `behind`; nothing pretends otherwise. Owner: Linus.
5. Sensitive content: concept bodies quote intent/spec text and symbol names only, never file
   contents beyond `source_location`; `references/` packs are excluded from the graph and from
   concepts. No PII beyond the git author name already in every artifact. Owner: Linus.
6. Tech lead for `Risk: high`: Linus McManamey (recorded 2026-09-09). Concerns 2-5 resolved as
   written by the product owner on the same date.

## Open questions

1. Bundle location: `sdlc/knowledge/`, configurable via `[knowledge] bundle`. Answered.
2. `graphify-out/`: ignored (`.gitignore`), rebuilt by Graphify's post-checkout hook; only the OKF
   bundle is committed. `.state.json` inside the bundle carries the graph commit it was built
   from. Answered.
3. Post-commit trigger: git hook block appended after Graphify's (works for commits made outside
   Claude); the `PostToolUse` Bash handler is visibility only. Answered.
4. Conformance checker: stdlib, three official rules plus a labelled policy list; `okf lint` is
   not installed or required. Answered.
5. Skill scope: user-level `graphify install --platform claude` (one skill for every project);
   `--project` mode not used because it also rewrites `.claude/settings.json` hooks, which this
   plugin owns through `hooks.json`. Answered.
6. Reviewer and verifier: prompts updated to read the index and allow `graphify query`; tool
   lists unchanged. Answered.
7. Clean-rebuild cadence: `clean_every = 5` updates, plus `max_behind = 1` commits; both
   configurable. Answered.
8. `CLAUDE.md` pointer: added once by bootstrap, marker-delimited, `claude_md_pointer = false`
   opts out; the block is two lines so it does not bloat context. Answered.
9. New: should `SessionStart` install anything (Concern 1)? Answered by the product owner:
   check-only unless `auto_install = true`.

## Proof

- `tests/test_knowledge.py` (new; `graphify` and `uv` are stubbed with a `fake_tools` fixture
  that puts shell scripts on PATH writing a canned `graph.json`, `god-nodes` output and `hook status` text, so the suite never needs Graphify installed):
  `test_bootstrap_installs_in_order_and_reports_steps` (req 1, 4);
  `test_bootstrap_healthy_project_makes_no_calls` (req 2);
  `test_bootstrap_disabled_and_missing_uv` (req 3);
  `test_refresh_is_idempotent_and_logs` (req 5, 9, 10: frontmatter round-trips, index sections,
  log heading format);
  `test_refresh_invalidates_changed_sources_and_tombstones_deleted` (req 11);
  `test_publish_only_on_accept_and_never_by_generation` (req 12);
  `test_check_separates_conformance_policy_trust` (req 13, including a bundle with broken links
  and unknown keys passing conformance);
  `test_status_reports_behind_skew_and_clean_cadence` (req 8);
  `test_hook_block_idempotent_and_removable` (req 6, on a temp repo's `.git/hooks/post-commit`
  that already holds a Graphify-style block);
  `test_frontmatter_subset_round_trip` (Design: YAML subset).
- `tests/test_hooks.py`: `test_session_start_context_lists_steps`, `test_post_bash_flags_stale _after_commit`, `test_post_edit_names_module_concepts` (req 7, 14).
- `tests/test_build_test.py`: `test_run_adds_knowledge_result_and_process_verified` (req 12, 14);
  `test_deploy.py`: `test_pr_body_has_knowledge_section` (req 14).
- `tests/test_plan_design.py`: `test_accept_publishes_feature_concept` (req 12).
- Existing suite unchanged and green with `[knowledge] enabled = false` in the `repo` fixture
  default, plus one test asserting a verdict is byte-identical with the table off (req 17).
- Live proof on this repo, recorded in `docs/knowledge-measurement.md`: `sdlc knowledge bootstrap`
  from a fresh clone; a commit followed by `sdlc knowledge status` showing `behind: 0` for both
  indexes; `graphify hook status` output; the five-question token measurement (req 16).
- `uv run pytest`, `uv run ruff check scripts tests && uv run ruff format --check scripts tests`,
  `claude plugin validate --strict .` green.
