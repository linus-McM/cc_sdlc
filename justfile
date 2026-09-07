# sdlc plugin — dev recipes

# Start Gemini in YOLO approval mode
gemini:
    @agy --model top --dangerously-skip-permissions

# Start Claude (Opus) in auto permission mode with this plugin loaded
opus:
    @claude --permission-mode auto --model opus --plugin-dir .

# Start Claude (Fable) in auto permission mode with this plugin loaded
fable:
    @claude --permission-mode auto --model fable --plugin-dir .

# Run the test suite
test:
    @uv run pytest

# Lint and format check
lint:
    @uv run ruff check scripts tests && uv run ruff format --check scripts tests

# Install the git pre-commit hooks
hooks:
    @uv run pre-commit install

# Run every pre-commit hook against the whole tree
precommit:
    @uv run pre-commit run --all-files

# Full gate: tests, lint, plugin manifest
check: test lint
    @claude plugin validate --strict .
