#!/usr/bin/env python3
"""Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>  (hook JSON on stdin; run via uv run --no-project)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc.hooks import main

sys.exit(main(sys.argv[1:]))
