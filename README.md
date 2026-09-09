# cc_sdlc

Claude Code plugin: six AI-native SDLC stage commands (`/sdlc:plan design build test deploy maintain`) with Python-gated artifacts, hooks as guardrails and TDD from build to maintain. The installable package is [`plugin/`](plugin/) ([plugin README](plugin/README.md)).

## Install
```sh
claude plugin marketplace add linus-McM/cc_sdlc   # this repo is the marketplace; installs pull plugin/ only
claude plugin install sdlc@sdlc
```
Try a checkout without installing: `claude --plugin-dir ./plugin`.

## Repository layout
| Path | What | Ships in the package |
|---|---|---|
| `plugin/` | `.claude-plugin/plugin.json`, `commands/`, `agents/`, `hooks/`, `scripts/`, `templates/`, README, LICENSE | yes |
| `.claude-plugin/marketplace.json` | marketplace manifest pointing at `plugin/` (`git-subdir`, ref `main`) | no |
| `tests/`, `pyproject.toml`, `uv.lock`, `.pre-commit-config.yaml`, `justfile`, `scripts/bump_version.py`, `.github/` | development and CI | no |
| `dogfood` branch | the plugin run on itself: `sdlc/<feature>/` artifacts, stage documents, knowledge bundle, `docs/` | no |

`dev` and `main` carry the package and its tooling only. The plugin dogfoods itself on the `dogfood` branch, which merges `main` in and never merges out; GitHub Pages serves that branch (architecture diagram: <https://linus-mcm.github.io/cc_sdlc/docs/architecture/sdlc-plugin.html>).

## CI and versions
`.github/workflows/ci.yml` runs on every PR to `main` and every push to `dev`: `uv run pytest`, ruff check and format, the pre-commit hooks and `claude plugin validate --strict` on `plugin/` and on the marketplace manifest. On a PR from this repo the `version` job then bumps `plugin/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `pyproject.toml` together and commits the bump into the PR branch when the PR has not bumped past `main` yet: patch by default, `release:minor` or `release:major` labels choose the part (`scripts/bump_version.py`). `main` is protected (PR required, no direct pushes); work lands on `dev` and merges through a PR.

## Develop
```sh
uv sync && uv run pytest            # TDD: red test first, then code
uv run ruff check scripts tests
claude plugin validate --strict .
```
