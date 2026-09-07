#!/usr/bin/env python3
"""Hook launcher: python3 scripts/hook.py <pre-edit|pre-bash|post-edit>  (hook JSON on stdin)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc.hooks import main

sys.exit(main(sys.argv[1:]))
