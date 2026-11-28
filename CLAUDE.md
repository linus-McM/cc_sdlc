# sdlc plugin

Claude Code plugin under `plugin/` (the installable package); the repo root holds tests, CI and dev tooling. Dogfood output (`sdlc/`, `docs/`, the knowledge bundle) is tracked only on the `dogfood` branch; `dev` and `main` stay package-only. Six stage commands (`/sdlc:plan design build test deploy maintain`): the loop is plan, design, build, test and ends at `test review`; deploy and maintain are optional. No risk levels and no named sign-off roles: Claude accepts intent.md and spec.md, the user approves once at `build accept`. Python does the gating; markdown only tells Claude which mechanic to call and what to do with the verdict.

## Commands

* Test: `uv run pytest` (all green; never skip or delete a failing test; runs under `pytest-xdist -n auto`, so a test never shares state outside its `tmp_path`)

* Lint: `uv run ruff check plugin/scripts scripts tests && uv run ruff format --check plugin/scripts scripts tests` (zero findings)

* Validate: `claude plugin validate --strict plugin && claude plugin validate --strict .` (plugin manifest, then the marketplace manifest)

* Try locally: `claude --plugin-dir plugin` then `/sdlc:plan new "title"`; dogfood on the `dogfood` branch
  Run all three checks before reporting a task complete and paste the tail. If a test fails, fix the code, not the test.

## Architecture

* `plugin/scripts/sdlc/` stdlib-only package. `cli.py` dispatches `<stage> <action> [arg]` and returns one JSON dict (`ok`, `reason`, `next`, ...). `stages.py` owns the new/check/accept lifecycle shared by intent.md, spec.md, plan.md (`stages.trace` ties every numbered spec.md requirement to a numbered plan.md step; `stages.APPROVAL` names the one stage whose accept is the user's). `build.py` TDD log + plan sync + fix lock + the approved plan (`build accept` pins files and steps in `approved.json`; `deviations` reports how plan.md differs from it, `missing_steps` and `untouched` are what `test run` refuses; `build red|green --only <test id>` runs `[commands] test_one` for the step; a green also runs the sync and, with `[build] commit_steps`, the step commit; `build simplify` records the `/simplify` pass that `test run` requires, and tests run with `SDLC_SIMPLIFY=off` unless they drop it). `testing.py` feedback loop + review.md (`test review` refuses open `Important:` lines and a Compliance section missing a requirement's verdict; `fixed:` or `wontfix: <reason>` resolves a line; `builtin_missing` refuses a review.md whose `## Built-in review` has no line for a `[test] builtin_review` skill (`/code-review`, `/security-review`), and tests run with `SDLC_BUILTIN_REVIEW=off` unless they drop it; its verdict carries `complete: true`). `deploy.py` tiers, rollback rehearsal, PR body. `maintain.py` Western Electric bands that write the next intent.md. `handover.py` writes `sdlc/<slug>/HANDOVER.md` at each `handover.BOUNDARIES` boundary before the checkpoint commit (verdict key `handover`). `checkpoint.py` the stage-boundary commit of generated artifacts; `cli.ENTRY` names the stage entry actions whose verdict carries the `workflow` gate and a `knowledge` note when tools are missing; `cli.BOUNDARIES` names the boundaries (`knowledge refresh` is one, committed silently so the post-commit hooks do not loop) and `cli.main` commits the verdict's `path` after a success (tests run with `SDLC_CHECKPOINT=off` unless they take the `checkpoint_on` fixture, listed before any `accepted_*` fixture). `hooks.py` PreToolUse/PostToolUse/SessionStart guardrails. `evals.py` continuous evals. `knowledge.py` Graphify bootstrap plus the OKF v0.2 bundle under `sdlc/knowledge/` (bootstrap/status/refresh/check/publish/unhook; Graphify and uv are subprocesses, tests stub them with the `knowledge` fixture). `workflows.py` the stage Workflow catalog (`plugin/workflows/*.js`, invoked as `sdlc:<name>`), the `gate` that runs a stage's workflow when `[workflows.run]` switches that stage on, and the session-start merge of `[workflows.env]` into `.claude/settings.local.json`; tests run with `SDLC_WORKFLOWS=off` unless they drop it. `docs.py` Archify stage documents (draft/render/check/open plus the `archify` bootstrap step; `drafts.py` writes the build, deploy and maintain sources mechanically; the shared authoring `recipe` rides on check/render failure verdicts, not in the commands; Node and Archify are subprocesses, tests stub them with the `docs_tools` fixture). `packs.py` graph-selected Repomix context packs under `graphify-out/packs/` (`knowledge pack <stage>`, and `require`, which builds the pack `plan accept` and `test review` report; Repomix, npm and Bandit are subprocesses, tests stub them with the `packs` fixture and otherwise run with `SDLC_PACKS=off`).

* `plugin/scripts/sdlc.py`, `plugin/scripts/hook.py` are launchers (they fix `sys.path`); `plugin/hooks/hooks.json` and `plugin/commands/*.md` call them via `${CLAUDE_PLUGIN_ROOT}`. `scripts/bump_version.py` is CI only (the `version` job bumps inside each PR to main); `.github/workflows/release.yml` tags and releases `v<version>` from `plugin/.claude-plugin/plugin.json` on each push to main, skipping a version that already has a release.

* `plugin/workflows/*.js` Workflow scripts: `export const meta` is written as JSON (Python reads it), phase titles must match, no `Date.now`/`Math.random`; read-only agents, the command writes the artifact.

* `plugin/templates/` artifact skeletons; `tests/` pytest, `conftest.py` has the fixtures that walk a feature through the stages.

## Conventions

* TDD: every mechanic gets a failing test before code. Tests drive the CLI in-process through the `run` fixture; no subprocess of `sdlc.py` in tests.

* Config comes from `project.config()` (defaults deep-merged with `.sdlc.toml`); never read the file elsewhere.

* Expected failures raise `project.fail(reason, **extra)` (a `Blocked`); success returns a dict with `ok: true`.

* Python 3.11+ (`tomllib`), no third-party runtime deps. Commit messages: `<stage>(<slug>): ...` for dogfooded work, Conventional Commits otherwise.

## Things Claude gets wrong

* Do not bring back risk levels, named approvers or `RELEASE_APPROVAL`: fidelity comes from `approved.json`, per-step cycles and per-requirement Compliance lines, and tests build plans with `conftest.build_out` so `test run` sees the planned files changed.

* `cli.main(argv, root)` never prints and is the only place `Blocked` is caught; `entry()` prints. Mechanics raise via `project.fail`, never return `{"ok": False}` by hand.

* `hooks.json` needs the top-level `hooks` key and plugin agents must not declare `hooks`/`permissionMode`.

* Generation never writes a `human:` actor into a concept's `verified`; only `stages.accept` (via `knowledge.publish`) does. Tests run with `SDLC_KNOWLEDGE=off` unless they take the `knowledge` fixture, which puts fake `uv`/`graphify` on PATH; never let a test reach the real tools.

* Stage documents are on demand: no accept, review or record waits for one (`docs.check` only reports). Tests run with `SDLC_DOCS=off` unless they take `docs_tools`. Never render documents inside a hook.

* Context packs are advice: `plan accept` and `test review` call `packs.require` through `project.attempt` and report the result under `pack`; only a changed file excluded as a secret refuses `test review`. A test that takes both `accepted_*` and `packs` lists `accepted_*` first. Pack test repos exclude the sandbox (`bin/`, `home/`, `claude/`) in `.git/info/exclude`, or `git add -A` commits it and the graph looks stale.

* After `/simplify` renames or removes a public name, grep spec.md, plan.md, README.md, CLAUDE.md and commands/ for the old name in the same commit; two reviews in a row flagged a stale `docs.require`.

* `hooks.py` imports the other mechanics inside the handlers (`test_hook_module_imports_stay_lazy`), and the Bash hooks in `hooks.json` filter in the shell before starting Python: that filter must stay a superset of the Python rule.

* Hook commands run through `uv run --no-project` (cwd is the user's project, whose pyproject must not be synced); the generated git post-commit block does the same.
