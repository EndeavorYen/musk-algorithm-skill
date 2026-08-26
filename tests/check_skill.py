#!/usr/bin/env python3
"""Structural acceptance checks for musk-algorithm. Run from the skill root."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "SKILL.md"
README_PATH = ROOT / "README.md"
SOURCES_PATH = ROOT / "references" / "sources.md"

CJK = re.compile(r"[\u4e00-\u9fff]")
STEP_MARKERS = (
    "Question every requirement",
    "Delete any part or process",
    "Simplify and optimize",
    "Accelerate cycle time",
    "Automate last",
)


def read_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    rest = text[3:]
    if rest.startswith("\r\n"):
        rest = rest[2:]
    elif rest.startswith("\n"):
        rest = rest[1:]
    match = re.search(r"\n---\s*(?:\n|$)", rest)
    if not match:
        return "", text
    return rest[: match.start()], rest[match.end() :]


def first_occurrences_in_order(text: str, needles: tuple[str, ...]) -> bool:
    lower = text.lower()
    positions: list[int] = []
    for needle in needles:
        found = lower.find(needle.lower())
        if found < 0:
            return False
        positions.append(found)
    return all(positions[i] < positions[i + 1] for i in range(len(positions) - 1))


def _posix_shell() -> str | None:
    if os.name != "nt":
        return "bash"
    git_bash = Path(r"C:\Program Files\Git\bin\bash.exe")
    if git_bash.is_file():
        return str(git_bash)
    return None


def _run(cmd: list[str], env: dict) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )


def _run_install(platform: str, env: dict) -> subprocess.CompletedProcess[str]:
    if os.name == "nt":
        return _run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(ROOT / "scripts" / "install.ps1"),
                platform,
            ],
            env,
        )
    return _run(["bash", str(ROOT / "scripts" / "install.sh"), platform], env)


def _copied_equal(dest: Path, src: Path) -> bool:
    return dest.is_file() and src.is_file() and dest.read_bytes() == src.read_bytes()


def main() -> int:
    skill = read_text(SKILL_PATH) or ""
    readme = read_text(README_PATH) or ""
    fm, body = split_frontmatter(skill)
    body_l = body.lower()
    checks: list[tuple[str, bool]] = []

    def check(name: str, ok: bool) -> None:
        checks.append((name, bool(ok)))

    check("SKILL.md frontmatter name musk-algorithm", bool(re.search(r"(?m)^name:\s*musk-algorithm\s*$", fm)))
    check("description contains musk algorithm", "musk algorithm" in fm)
    check("description contains musk-algorithm", "musk-algorithm" in fm)
    check("description contains five-step algorithm", "five-step algorithm" in fm)
    check("description contains first principles algorithm", "first principles algorithm" in fm)
    check("description contains question every requirement", "question every requirement" in fm)
    check("description contains /musk-algorithm", "/musk-algorithm" in fm)
    check("description says explicit invocation always", "explicit invocation always" in fm.lower())

    named_person = (
        "named person" in body_l
        or "named-person" in body_l
        or "person, not department" in body_l
        or "not a department" in body_l
    )
    add_back = "10%" in body and (
        "add-back" in body_l
        or "add back" in body_l
        or "adding back" in body_l
        or "put back" in body_l
    )
    apply_if_asked = "only if" in body_l and "asked" in body_l
    report_not_rewrite = "structured evaluation report" in body_l and (
        "not a code rewrite" in body_l or "not a rewrite" in body_l
    )

    check("body has Question every requirement", "Question every requirement" in body)
    check("body has named-person rule", named_person)
    check("body has Delete any part or process", "Delete any part or process" in body)
    check("body has 10% add-back bar", add_back)
    check("body has Simplify and optimize", "Simplify and optimize" in body)
    check("body has Accelerate cycle time", "Accelerate cycle time" in body)
    check("body has Automate last", "Automate last" in body or "automate last" in body_l)
    check("five steps appear in order", first_occurrences_in_order(body, STEP_MARKERS))
    check("body states sequence/order", "in order" in body_l or "sequence is the algorithm" in body_l)
    check("default output is a report not a rewrite", report_not_rewrite)
    check("apply only if asked", apply_if_asked)

    english_files = [
        SKILL_PATH,
        README_PATH,
        SOURCES_PATH,
        ROOT / "ARCHITECTURE.md",
        ROOT / "scripts" / "install.ps1",
        ROOT / "scripts" / "install.sh",
        ROOT / "tests" / "check_skill.py",
        ROOT / "tests" / "test_skill_contract.py",
    ]
    for path in english_files:
        text = read_text(path) or ""
        check(f"{path.relative_to(ROOT).as_posix()} is English", not CJK.search(text))
    check("SKILL.md body is English", not CJK.search(body))
    check("README mentions just-ten-more", "just-ten-more" in readme)
    check("scripts/install.ps1 exists", (ROOT / "scripts" / "install.ps1").is_file())
    check("scripts/install.sh exists", (ROOT / "scripts" / "install.sh").is_file())
    check("install.sh has no CR", b"\r" not in (ROOT / "scripts" / "install.sh").read_bytes())
    gitattributes = read_text(ROOT / ".gitattributes") or ""
    check("gitattributes forces install.sh LF", "scripts/install.sh" in gitattributes and "eol=lf" in gitattributes)
    mode = subprocess.run(
        ["git", "ls-files", "-s", "scripts/install.sh"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    check("install.sh is executable in git", mode.stdout.startswith("100755"))
    check("README install path", "~/.grok/skills/musk-algorithm/" in readme)
    check("README documents GROK_HOME", "GROK_HOME" in readme)
    check("README hermes install path", "~/.hermes/skills/musk-algorithm/" in readme)
    check("README documents HERMES_HOME", "HERMES_HOME" in readme)

    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "dest"
        dest.mkdir()
        env = {
            **{k: v for k, v in os.environ.items()},
            "USERPROFILE": str(dest),
            "HOME": str(dest),
        }
        env.pop("GROK_HOME", None)
        env.pop("HERMES_HOME", None)
        proc = _run_install("grok", env)
        installed = dest / ".grok" / "skills" / "musk-algorithm"
        src_skill = SKILL_PATH.read_text(encoding="utf-8") if SKILL_PATH.is_file() else ""
        src_readme = README_PATH.read_text(encoding="utf-8") if README_PATH.is_file() else ""
        check(
            "install grok copies SKILL.md",
            proc.returncode == 0 and (installed / "SKILL.md").is_file(),
        )
        check("install grok copies README.md", (installed / "README.md").is_file())
        check(
            "copied SKILL.md matches source",
            _copied_equal(installed / "SKILL.md", SKILL_PATH) and bool(src_skill),
        )
        check(
            "copied README.md matches source",
            _copied_equal(installed / "README.md", README_PATH) and bool(src_readme),
        )
        if SOURCES_PATH.is_file():
            copied_sources = installed / "references" / "sources.md"
            check("install grok copies references/sources.md", copied_sources.is_file())
            check(
                "copied references/sources.md matches source",
                _copied_equal(copied_sources, SOURCES_PATH),
            )

        proc_all = _run_install("all", env)
        check("install all succeeds", proc_all.returncode == 0)
        check(
            "install all copies claude SKILL.md",
            (dest / ".claude" / "skills" / "musk-algorithm" / "SKILL.md").is_file(),
        )
        check(
            "install all copies cursor SKILL.md",
            (dest / ".cursor" / "skills" / "musk-algorithm" / "SKILL.md").is_file(),
        )
        check(
            "install all copies hermes SKILL.md",
            (dest / ".hermes" / "skills" / "musk-algorithm" / "SKILL.md").is_file(),
        )

        hhome = dest / "custom-hermes"
        env_hermes = {**env, "HERMES_HOME": str(hhome)}
        proc_hermes = _run_install("hermes", env_hermes)
        hermes_installed = hhome / "skills" / "musk-algorithm"
        check(
            "HERMES_HOME dest copies SKILL.md",
            proc_hermes.returncode == 0 and (hermes_installed / "SKILL.md").is_file(),
        )

        ghome = dest / "custom-grok"
        env_home = {**env, "GROK_HOME": str(ghome)}
        proc_home = _run_install("grok", env_home)
        grok_installed = ghome / "skills" / "musk-algorithm"
        check(
            "GROK_HOME dest copies SKILL.md",
            proc_home.returncode == 0 and (grok_installed / "SKILL.md").is_file(),
        )
        check(
            "GROK_HOME dest copies README.md",
            (grok_installed / "README.md").is_file(),
        )
        if SOURCES_PATH.is_file():
            check(
                "GROK_HOME dest copies references/sources.md",
                (grok_installed / "references" / "sources.md").is_file(),
            )

        if os.name == "nt":
            bad_ps = _run_install("nope", env)
            check("install.ps1 rejects unknown platform", bad_ps.returncode != 0)

        shell = _posix_shell()
        if shell is None and os.name == "nt":
            check("install.sh checks skipped without posix shell", True)
        else:
            check("posix shell available to test install.sh", shell is not None)
        if shell:
            bad_sh = _run([shell, str(ROOT / "scripts" / "install.sh"), "nope"], env)
            check("install.sh rejects unknown platform", bad_sh.returncode != 0)
            sh_home = dest / "sh-home"
            sh_home.mkdir()
            env_sh = {**env, "HOME": str(sh_home)}
            env_sh.pop("GROK_HOME", None)
            proc_sh = _run([shell, str(ROOT / "scripts" / "install.sh"), "grok"], env_sh)
            sh_skill = sh_home / ".grok" / "skills" / "musk-algorithm" / "SKILL.md"
            check(
                "install.sh grok copies SKILL.md",
                proc_sh.returncode == 0 and sh_skill.is_file(),
            )
            if SOURCES_PATH.is_file():
                sh_sources = sh_home / ".grok" / "skills" / "musk-algorithm" / "references" / "sources.md"
                check("install.sh grok copies references/sources.md", sh_sources.is_file())

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    if failed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
