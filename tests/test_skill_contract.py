#!/usr/bin/env python3
"""Run the skill contract checks under pytest."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_skill_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tests" / "check_skill.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
