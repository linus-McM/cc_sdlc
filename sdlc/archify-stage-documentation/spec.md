# Spec: Archify stage documentation
From: intent.md (2026-09-09). Status: accepted. Risk: low.

## Requirements
Traced to intent.md Proposed outcome items (PO1..PO4). "Verdict" means the one JSON dict
`cli.main` returns. "Skill dir" means `$CLAUDE_CONFIG_DIR/skills/archify` (default
`~/.claude/skills/archify`), the same base `knowledge.skill_path` uses.

1. (PO1) `[docs]` is a new table in `project.DEFAULT_CONFIG`: `enabled = true`, `dir = "docs"`
   (per-feature subdirectory), `quality = "showcase"`, `open = true` (open the HTML locally at
   accept time), `min_node = 18`, `min_version = "2.17"` (lowest Archify skill version the
   authoring guidance in `commands/*.md` was written against), `types` mapping stage to
   diagram type: `plan = "architecture"`, `design = "dataflow"`, `build = "workflow"`,
   `test = "sequence"`, `deploy = "lifecycle"`, `maintain = "lifecycle"`. `[docs] enabled =
   false` or `SDLC_DOCS=off` turns every `docs` mechanic into `{"ok": true, "skipped": "docs
   disabled"}` and removes every gate below (mirrors `knowledge.when_enabled`).
2. (PO1) `knowledge.STEPS` gains one step named `archify`, placed after `skill` and before
   `hooks`. Present when `<skill dir>/bin/archify.mjs` exists. Its present-check may raise
   `StepSkipped`: when docs are disabled (detail `docs disabled`) or when `node` is absent or
   `node --version` reports a major below `[docs] min_node` (detail names the found version and
   the install command). `bootstrap` treats a `StepSkipped` from a present-check as state
   `skipped` in both `check` and install mode, and later steps still run. In `check` mode a
   missing skill is state `missing` with the install command in `detail`; in install mode the
   step runs `npx -y skills add tt-a1i/archify --skill archify --agent claude-code --global
   --copy --yes` through `knowledge.ran` and is `installed` only when `bin/archify.mjs` exists
   afterwards, else `failed` with the stderr tail. `detail` of a present or installed step is
   `Archify skill <version>` where version is read from `<skill dir>/skill-release.json`
   (`unknown` when unreadable). The SessionStart hook needs no change: it prints the step list.
3. (PO1) `sdlc knowledge status` adds `archify: {installed: bool, version: str | null,
   min_version: str}` to its verdict and appends a note (not a reason; `ok` is unaffected)
   `archify <version> is older than [docs] min_version <min>` when the installed version tuple
   is lower. No network call is made anywhere in the plugin to learn the latest version.
4. (PO2) New module `scripts/sdlc/docs.py` (stdlib only) owns: `cfg`, `enabled`, `skill_dir`,
   `node_version`, `sources(stage, feature)`, `digest(root, sources)`, `render`, `check`,
   `require`, `open`. Sources per stage, relative to the feature directory unless noted:
   `plan: intent.md`; `design: spec.md`; `build: plan.md`; `test: review.md, test-report.json`;
   `deploy: pr-body.md`; `maintain: sdlc/bands.toml` (repo-relative; maintain has no feature).
   `digest` is the sha256 hex of the concatenated source bytes, each prefixed by its path.
5. (PO2) Claude authors the diagram source at `<feature>/<dir>/<stage>.json` (maintain:
   `sdlc/<dir>/maintain.json`) following the Archify skill fast path; `sdlc docs render <stage>
   [--slug]` then runs `node <skill dir>/bin/archify.mjs deliver <type> <stage>.json
   <stage>.html --quality <quality> --json` with `ARCHIFY_UPDATE_CHECK_DISABLED=1` in the
   environment and cwd at the docs directory, parses the receipt JSON from stdout, and writes
   `<stage>.receipt.json` = `{stage, type, sources: [{resource, digest}], source_digest,
   specification_sha256, artifact_sha256, validation, archify_version, delivered_at}`.
   Verdict: `{ok: true, html, receipt, validation}`. Missing `<stage>.json` fails with
   `stage document source missing; author <path> from <sources> (Archify <type>), then rerun`.
   A non-zero `deliver` exit fails with `archify deliver exited <n>: <last 400 chars of stderr
   or stdout>` and `<stage>.html` is left as Archify left it (previous trusted artifact or
   absent); the verdict never calls a failed delivery a success. Absent `node` or skill fails
   with the bootstrap install command in `reason`.
6. (PO3) `docs.check(root, feature, stage)` returns `{ok: true, html, fresh: true}` when
   `<stage>.html` and `<stage>.receipt.json` exist and the receipt's `source_digest` equals the
   digest of the current sources. It fails `stage document missing; author <stage>.json, then
   `sdlc docs render <stage>`` when either file is absent, and `stage document is stale:
   <changed resources> changed since <stage>.html was delivered; rerun `sdlc docs render
   <stage>`` when the digest differs. `sdlc docs check <stage>` exposes it.
7. (PO3) Gates, all through `docs.require` (= `check`, or the skipped verdict when disabled):
   `stages.accept` for plan, design and build calls it before writing `Status: accepted`;
   `testing.review` calls it for `test` after validating review.md; `deploy.record` calls it
   for `deploy` before appending the deployment. Each blocked verdict carries the `check`
   reason verbatim. `sdlc docs render maintain` has no gate (maintain is a watch loop, not an
   acceptance); `maintain.watch` adds `docs: "<reason>"` to its verdict when the maintain
   document is missing or stale, and nothing else changes.
8. (PO3) `sdlc docs open <stage> [--slug]` runs `node <skill dir>/bin/open-artifact.mjs
   <stage>.html` when `[docs] open` is true and the environment variable `CI` is unset, and
   returns `{ok: true, html, opened: bool, reason?}`; it never fails on an opener error (the
   acceptor still gets the path). `commands/*.md` call it right before the AskUserQuestion that
   asks for acceptance and quote the HTML path in the question.
9. (PO3) `deploy.pr_body` adds a `### Documents` section listing every `<feature>/<dir>/*.html`
   present, one bullet `- <stage>: sdlc/<slug>/<dir>/<stage>.html (<validation>)` from the
   matching receipt, or `- none` when the directory is empty.
10. (PO2) Authoring guidance lives in `commands/*.md`, not in Python: each stage command gains a
    `docs` step that names the diagram type, the artifact sections to read, the node budget (at
    most 12 primary nodes), the required summary card `Generated by sdlc from <source> @
    <first 12 of source_digest>; drafts are Claude's reading of the artifact, the acceptor
    decides`, `meta.quality_profile: "showcase"`, and the command sequence `sdlc docs render
    <stage>` then `sdlc docs open <stage>`. The per-stage reading: plan = affected users and
    systems from Affected users and systems plus Problem (architecture); design = data flow
    between the components named in Design (dataflow); build = Order of work steps with their
    red/green tests (workflow); test = the run, verifier and reviewer exchange with finding
    counts (sequence); deploy = environments, gates, rehearsal and rollback (lifecycle);
    maintain = band tiers and the actions they trigger (lifecycle). A `deliver` failure is
    repaired in the JSON source only, at most two rounds, then reported.
11. (PO4) `[knowledge] ignore` default gains `sdlc/*/docs/` and `sdlc/docs/`, so `write_ignore`
    keeps generated HTML out of the Graphify graph; `knowledge.refresh` treats the docs
    directory like `references/` (no concept, no source). `features/<slug>.md` concepts gain a
    `# Documents` section listing the delivered stage documents (path plus validation) when the
    directory exists; empty otherwise. Generation still never writes a `human:` event.
12. (PO4) `README.md` documents the `[docs]` table, the `archify` bootstrap step, the gate, the
    off switches (`[docs] enabled = false`, `SDLC_DOCS=off`, `CI` suppresses opening) and the
    supply-chain note; `CLAUDE.md` Architecture lists `docs.py`; `hooks/hooks.json` is unchanged.

## Design
Components and data flow:

- `docs.py` (new, ~150 lines). `cfg(root) = p.config(root)["docs"]`; `enabled(root)` checks
  the table and `SDLC_DOCS`; `when_enabled` decorator copied in shape from `knowledge`
  (returns `SKIPPED = {"ok": true, "skipped": "docs disabled"}`). `skill_dir()` mirrors
  `knowledge.skill_path` with `archify`. `node_version()` runs `node --version`, returns the
  major int or `None`. `version()` reads `skill-release.json["version"]`.
  `SOURCES = {"plan": ["intent.md"], "design": ["spec.md"], "build": ["plan.md"], "test":
  ["review.md", "test-report.json"], "deploy": ["pr-body.md"], "maintain": ["sdlc/bands.toml"]}`;
  `docs_dir(root, feature, stage)` is `feature / cfg["dir"]` or `p.home(root) / cfg["dir"]`
  for maintain. `render` builds the argv, runs `p.run_cmd(root, argv, env)` (existing helper,
  cwd = root; paths passed absolute), decodes the receipt with `json.loads(stdout)` falling
  back to the last JSON object in the output, and writes the receipt via `p.write_json`.
  `check` recomputes the digest and compares. `require = check` wrapped by `when_enabled`.
  `open` shells out to `open-artifact.mjs` with a 10-second timeout and swallows failure into
  `opened: false, reason`.
- `knowledge.py`: `STEPS` gets `("archify", docs.archify_present, docs.install_archify,
  "installed", "Archify skill")` after `skill`; `bootstrap` wraps the present-check in
  `try/except StepSkipped`; the present-check returns the version-bearing detail through a
  small `Present(detail)` return (a truthy `str` subclass) so the loop keeps `detail` for a
  present step; `status` adds `archify` and the version note. `docs.install_archify` raises
  `StepSkipped` when node is missing and calls `knowledge.ran` otherwise (imported lazily to
  avoid the cycle: `knowledge` imports `docs`; `docs` never imports `knowledge` at module
  level). Default `ignore` list gains the two docs globs; `feature_concepts` reads receipts.
- `project.py`: `DEFAULT_CONFIG` gains the `[docs]` and `[docs.types]` tables with comments.
- `stages.accept`: `docs.require(root, path.parent, stage)` right after `check`, before
  `set_meta`. `testing.review`: `docs.require(feature.parent.parent, feature, "test")` after
  validate (root is passed in by the CLI handler; the signature becomes `review(root,
  feature)`, `cli.py` and `deploy.pr_body` follow). `deploy.record`: `docs.require(root,
  feature, "deploy")` after `check`. `deploy.pr_body`: new `documents(feature)` helper.
  `maintain.watch`: attempt `docs.check` for maintain and attach `docs` on `Blocked`.
- `cli.py`: `("docs", "render"|"check"|"open")`, gate `None`, handler resolves the feature with
  `p.feature(root, ns.slug)` unless `arg == "maintain"`; `arg` is the stage and is validated
  against `docs.SOURCES` (`fail("unknown stage; one of ...")`).
- `commands/*.md`: one `## docs` block per stage (requirement 10) placed before the accept or
  review step; plan.md, design.md, build.md say the accept is refused until the document is
  fresh; test.md before step 4 of review; deploy.md before `record`; maintain.md under watch.
- `templates/`: none new (Archify's own schemas and examples in the skill dir are the
  templates; commands point at them).
- Interfaces: the Archify CLI receipt (`deliver --json`) is the only contract consumed;
  `specification.sha256`, `artifact.sha256` and the check counts are copied, nothing else is
  interpreted. The plugin never edits Archify's files and never runs `visual-check` or
  `preview`.
- Data: `sdlc/<slug>/docs/<stage>.json` (Claude-authored, committed), `<stage>.html` and
  `<stage>.receipt.json` (generated, committed with the stage artifact). Nothing is written
  outside the feature directory except `sdlc/docs/` for maintain.

## Concerns
- Supply chain (owner: repository owner, Linus McManamey). The bootstrap can execute
  `npx -y skills add tt-a1i/archify ...`, which downloads and runs third-party code from npm
  and GitHub, only when `[knowledge] auto_install = true` (the default is check-only, which
  prints the command). The skills CLI cannot pin a version, so the version installed is
  whatever upstream ships; `min_version` only flags drift downwards. Accepting this spec
  accepts unpinned installs on machines that opt in. Resolved 2026-09-09: accepted for this
  repo, `auto_install` stays opt-in for others.
- Network egress (owner: repository owner). Archify's update checker performs an HTTP GET to
  its release manifest about every 72 hours; the plugin sets
  `ARCHIFY_UPDATE_CHECK_DISABLED=1` on every subprocess so a stage command never reaches the
  network. The Archify skill's own instructions tell Claude to run the checker after the first
  candidate; `commands/*.md` says not to, and the sdlc instruction wins inside a stage. Two
  policies contradict here; this spec picks no network during stages.
- Visual review contradiction (owner: product owner). Archify's delivery contract expects a
  browser `visual-check` and a perceptual review before handoff. The plugin gates on the
  deterministic `deliver` receipt only (Chrome is not a plugin dependency) and makes the human
  acceptor the perceptual reviewer by opening the HTML. Accepting this spec accepts
  `browser_evidence: skipped` as the plugin's standing state.
- LLM-authored diagrams presented for acceptance (owner: product owner). The diagram is
  Claude's reading of the artifact, not a parse of it; it can omit or misplace a system. The
  required summary card labels it as such and names the source digest; the gate proves only
  that the document was built from the current artifact, not that it is correct.
- Repository size (owner: engineer). Each stage adds one HTML of roughly 100 to 300 KB; six
  per feature, committed. Acceptable for this repo; `[docs] enabled = false` is the opt-out.
- No PII, auth, payments or infra are touched. Risk stays low.
- Resolution 2026-09-09: the product owner (Linus McManamey) accepted all five concerns as
  written: unpinned opt-in install, no network during stages, `browser_evidence: skipped` as
  standing state, labelled LLM-authored diagrams, committed HTML.

## Open questions
Carried from intent.md, all closed there on 2026-09-09; refinements made here:
- Display: local HTML through `open-artifact.mjs` via `sdlc docs open`; suppressed when `CI` is
  set or `[docs] open = false`; PR body links the files. No Artifact publishing.
- Missing Node or Archify, or a failed `deliver`: `accept`, `test review` and `deploy record`
  are refused with the reason verbatim while docs are enabled; disabled skips gate and docs.
- Version pin: none available; bootstrap reports the installed version, `knowledge status`
  notes when it is below `[docs] min_version`. The intent said "drift from the version in
  `references/README.md`"; a config value is checkable, a README is not, so `min_version`
  replaces it.
- New: maintain documents have no gate (requirement 7) because maintain has no human
  acceptance step; `watch` reports staleness instead.

## Proof
- `tests/test_docs.py` (new), driven through the `run` fixture with a new `docs_tools`
  fixture in `tests/conftest.py` that unsets `SDLC_DOCS`, puts fake `node` and `npx` shell
  scripts on a bare PATH (fake `node` answers `--version` with `v20.11.0`, handles
  `<archify.mjs> deliver <type> <in> <out> --quality showcase --json` by writing `<out>` and
  printing a receipt JSON, exits 1 with `composition error` when the JSON source contains
  `"fail": true`, logs `open-artifact.mjs <path>`; fake `npx` creates the skill dir with
  `bin/archify.mjs` and `skill-release.json`), and sets `CLAUDE_CONFIG_DIR` and `HOME` to tmp.
  Tests: disabled verdicts (`SDLC_DOCS=off` and `[docs] enabled = false`); render writes html
  and receipt with the source digest; render fails verbatim on deliver exit 1 and on missing
  source JSON; check fresh, missing, stale after editing intent.md; accept blocked without a
  document and allowed with one for plan, design, build; `test review` and `deploy record`
  blocked and allowed; maintain render writes `sdlc/docs/`; `watch` carries `docs`; open logs
  the call and is skipped under `CI=1`; `pr_body` lists documents; unknown stage fails.
- `tests/test_knowledge.py`: bootstrap step order includes `archify` after `skill`; skipped
  with a node-less PATH in both modes; missing in check mode with the command; installed via
  fake `npx` in install mode; detail carries the version; `status` reports `archify` and the
  `min_version` note; the default `.graphifyignore` contains `sdlc/*/docs/`; the feature
  concept has a `# Documents` section listing a delivered document.
- `tests/test_hooks.py`: session-start text lists the `archify` step.
- Existing suites stay green with `SDLC_DOCS=off` set in the `repo` fixture (stages behave as
  today when docs are off).
- Checks: `uv run pytest`; `uv run ruff check scripts tests && uv run ruff format --check
  scripts tests`; `claude plugin validate --strict .`; live: `sdlc knowledge bootstrap` on this
  machine reports `archify: present (Archify skill 2.17.0-dev.1)`, then `sdlc docs render
  design` on this feature delivers `sdlc/archify-stage-documentation/docs/design.html` and
  `sdlc design accept` is refused before and allowed after.
