# sdlc — AI-native SDLC plugin for Claude Code

Six commands, one per stage of the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook). Each stage ends by committing an artifact; the next stage refuses to start until a human has accepted it. Gates are Python, not prose: every command calls `scripts/sdlc.py` and acts on a JSON verdict.

Architecture: <a href="https://linus-mcm.github.io/cc_sdlc/docs/architecture/sdlc-plugin.html" target="_blank" rel="noopener">interactive diagram</a> (scope, core components, primary path; source in `docs/architecture/sdlc-plugin.architecture.json`).

| Stage | Command | Writes | Gate to enter |
|---|---|---|---|
| Plan | `/sdlc:plan new "title"` → `check` → `accept` | `sdlc/<slug>/intent.md` | — |
| Design | `/sdlc:design new` → `accept` | `spec.md` (with flagged Concerns) | intent.md accepted |
| Build | `/sdlc:build new` → `accept` → `red/green` per step, `sync`, `fix on/off` | `plan.md`, `tdd.jsonl` | spec.md accepted |
| Test | `/sdlc:test run` → `review` → `evals` | `test-report.json`, `review.md` | plan.md accepted + ≥1 red→green cycle |
| Deploy | `/sdlc:deploy pr` → `check <env>` → `rehearse` → `record <env>` | `pr-body.md`, `deploy.json` | passing report + review; production also needs rehearsed rollback + `RELEASE_APPROVAL` |
| Maintain | `/sdlc:maintain watch` → `propose <metric>` → `lesson` | next `intent.md`, `lessons.md` | Western Electric rules on `sdlc/metrics.jsonl` |

## Guardrails (hooks/hooks.json)
- **pre-edit**: denies edits under `build.protected_paths`; denies test-file edits while `build fix on` (bug fixes prove themselves with a test the agent cannot rewrite).
- **pre-bash**: unless `RELEASE_APPROVAL` names a release manager, denies a command whose shell tokens hold a `deploy` program plus a `gate`-tier environment name from `.sdlc.toml` (a release script that accepts `prod` needs `prod = "gate"` listed too), and, when `deploy.command` is configured, that command rendered for a gated environment. Heredoc bodies and quoted prose (commit messages) never match; every other command line does. Hooks are advisory; `deploy.check` is the gate.
- **post-edit**: tells Claude when an edited file is missing from plan.md "Files that change".

## Install
```sh
claude --plugin-dir /path/to/cc_sdlc          # try it
claude plugin marketplace add /path/to/cc_sdlc # or install from the local marketplace
claude plugin install sdlc@sdlc
```
Project config is `.sdlc.toml` (created on first `plan new`): test/lint/build commands, protected paths, environment tiers, rollback command, metrics path. Copy `templates/REVIEW.md` to the repo root and `templates/bands.toml` to `sdlc/`.

## Develop
```sh
uv sync && uv run pytest            # TDD: red test first, then code
uv run ruff check scripts tests
claude plugin validate --strict .
```
