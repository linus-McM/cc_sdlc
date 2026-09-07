#!/usr/bin/env python3
"""Launcher: python3 scripts/sdlc.py <stage> <action> ..."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc.cli import entry

sys.exit(entry())
