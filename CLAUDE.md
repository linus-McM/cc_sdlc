# sdlc plugin

Claude Code plugin: six stage commands (`/sdlc:plan design build test deploy maintain`). Python does the gating; markdown only tells Claude which mechanic to call and what to do with the verdict.

## Commands
- Test: `uv run pytest` (all green; never skip or delete a failing test)
- Lint: `uv run ruff check scripts tests && uv run ruff format --check scripts tests` (zero findings)
- Validate: `claude plugin validate --strict .`
- Try locally: `claude --plugin-dir .` then `/sdlc:plan new "title"`
Run all three checks before reporting a task complete and paste the tail. If a test fails, fix the code, not the test.

## Architecture
- `scripts/sdlc/` stdlib-only package. `cli.py` dispatches `<stage> <action> [arg]` and returns one JSON dict (`ok`, `reason`, `next`, ...). `stages.py` owns the new/check/accept lifecycle shared by intent.md, spec.md, plan.md. `build.py` TDD log + plan sync + fix lock. `testing.py` feedback loop + review.md. `deploy.py` tiers, rollback rehearsal, PR body. `maintain.py` Western Electric bands that write the next intent.md. `hooks.py` PreToolUse/PostToolUse/SessionStart guardrails. `evals.py` continuous evals. `knowledge.py` Graphify bootstrap plus the OKF v0.2 bundle under `sdlc/knowledge/` (bootstrap/status/refresh/check/publish/unhook; Graphify and uv are subprocesses, tests stub them with the `knowledge` fixture).
- `scripts/sdlc.py`, `scripts/hook.py` are launchers (they fix `sys.path`); `hooks/hooks.json` and `commands/*.md` call them via `${CLAUDE_PLUGIN_ROOT}`.
- `templates/` artifact skeletons; `tests/` pytest, `conftest.py` has the fixtures that walk a feature through the stages.

## Conventions
- TDD: every mechanic gets a failing test before code. Tests drive the CLI in-process through the `run` fixture; no subprocess of `sdlc.py` in tests.
- Config comes from `project.config()` (defaults deep-merged with `.sdlc.toml`); never read the file elsewhere.
- Expected failures raise `project.fail(reason, **extra)` (a `Blocked`); success returns a dict with `ok: true`.
- Python 3.11+ (`tomllib`), no third-party runtime deps. Commit messages: `<stage>(<slug>): ...` for dogfooded work, Conventional Commits otherwise.

## Things Claude gets wrong
- `cli.main(argv, root)` never prints and is the only place `Blocked` is caught; `entry()` prints. Mechanics raise via `project.fail`, never return `{"ok": False}` by hand.
- `hooks.json` needs the top-level `hooks` key and plugin agents must not declare `hooks`/`permissionMode`.
- Generation never writes a `human:` actor into a concept's `verified`; only `stages.accept` (via `knowledge.publish`) does. Tests run with `SDLC_KNOWLEDGE=off` unless they take the `knowledge` fixture, which puts fake `uv`/`graphify` on PATH; never let a test reach the real tools.
- Hook commands run through `uv run --no-project` (cwd is the user's project, whose pyproject must not be synced); the generated git post-commit block does the same.
