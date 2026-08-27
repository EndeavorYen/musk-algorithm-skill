# musk-algorithm architecture

Independent Grok skill. Same `SKILL.md` copies to Claude, Cursor, and Hermes. Complementary to [just-ten-more](https://github.com/EndeavorYen/just-ten-more): never merge them. `just-ten-more` lists challenges and writes no review log. `just-ten-more-loop` is the hunt-fix loop.

| | musk-algorithm | just-ten-more | just-ten-more-loop |
|---|---|---|---|
| Job | First-principles evaluation of a requirement, design, process, or system | Evidence-backed hunt, list only | Evidence-backed hunt-fix review loop |
| Sequence | Musk's five steps **in order** | One round of up to 10 challenges | Rounds until a round finds none |
| Default output | Structured evaluation report | List in the conversation; no review log | Fixes (or blockers) plus a review log |
| Helper | None | None | `scripts/review-log.py` + `.just-ten-more/` |
| Apply edits | Only if asked, and only after steps 1–2 say the thing should exist | None | Fix in the same round |

## File tree

```
LICENSE                     MIT, EndeavorYen 2026 (do not rewrite)
ARCHITECTURE.md             This file: layout, ownership, data flow
SKILL.md                    Agent prompt (YAML frontmatter + English body)
README.md                   Human story + install
references/sources.md       Quote home (primary / closely attributed; no biography dump in SKILL.md)
scripts/install.ps1         Windows installer
scripts/install.sh          Unix installer (git 100755, LF-only)
tests/check_skill.py        Structural + install acceptance
tests/test_skill_contract.py  Thin pytest wrapper around check_skill.py
.gitignore                  __pycache__/, .pytest_cache/, .grok/, .just-ten-more/
.gitattributes              scripts/install.sh text eol=lf
```

Installed skill root (`musk-algorithm/`): `SKILL.md`, `README.md`, `references/`. Not installed: `LICENSE`, `ARCHITECTURE.md`, `scripts/`, `tests/`.

## What each file owns

- **SKILL.md** — When to run (explicit invocation always; auto-load only when the description matches), the five-step contract, report shape, apply-vs-report rule, quote discipline. Entire repo is English. Runtime may still speak the user's language. Point at `references/sources.md` instead of retelling Isaacson.
- **references/sources.md** — Fair-use short quotes and attributions. Canonical written algorithm: Isaacson 2023 ~pp. 284–286. Spoken origin: Everyday Astronaut Starbase Tour, Aug 2021. Mantra / gone-backwards: Lex Fridman #438, Aug 2024. Flag unverified material (no fire-suppression-pad unowned-requirement story as Musk/Isaacson).
- **README.md** — What it is, complementary-to-just-ten-more, when it triggers, quick start, install table, `GROK_HOME` / `HERMES_HOME`.
- **scripts/install.ps1**, **scripts/install.sh** — Copy `SKILL.md`, optional `README.md`, and `references/` if present. One positional arg: `grok | claude | cursor | hermes | all` (default `all`). No `review-log.py`. Shape matches just-ten-more (neither ships that helper). just-ten-more-loop ships `scripts/review-log.py`.
- **tests/check_skill.py** — Named PASS/FAIL checks: frontmatter, five-step bars, English-only repo files, installers, LF on `install.sh`, git mode `100755`, README paths, complementary just-ten-more vs just-ten-more-loop claims, `.gitignore` lists `.just-ten-more/`, tempdir install (never the real home).
- **tests/test_skill_contract.py** — `pytest` exec of `check_skill.py`; assert returncode 0.

## Data flow

```
trigger (musk algorithm, /musk-algorithm, description phrases)
    -> load SKILL.md (agent)
    -> cite from references/sources.md; do not invent quotes
    -> step 1 Question every requirement   (named person, not department)
    -> step 2 Delete any part or process   (10% add-back bar)
    -> step 3 Simplify and optimize        (only after 1–2)
    -> step 4 Accelerate cycle time        (only after 1–3)
    -> step 5 Automate                     (last)
    -> structured evaluation report
    -> apply changes only if the user asked AND steps 1–2 keep the thing
```

Sequence is the algorithm. Skipping ahead multiplies waste (optimize a thing that should not exist; accelerate / automate something later deleted). One algorithm across Isaacson / Starbase / Lex — not three.

## Install destinations

Repo root is the parent of `scripts/`. Home: sh `$HOME`; ps1 `$env:USERPROFILE` else `$HOME`.

| Target | Destination |
| --- | --- |
| grok | `$GROK_HOME/skills/musk-algorithm` if set, else `$HOME/.grok/skills/musk-algorithm` |
| hermes | `$HERMES_HOME/skills/musk-algorithm` if set, else `$HOME/.hermes/skills/musk-algorithm` |
| claude | `$HOME/.claude/skills/musk-algorithm` (no env override) |
| cursor | `$HOME/.cursor/skills/musk-algorithm` (no env override) |

`all` = grok, claude, cursor, hermes in that order. Unknown platform: ps1 `ValidateSet` / throw; sh usage and exit 2.

Tests prove install in a tempdir with `USERPROFILE=HOME=tmp` and `GROK_HOME` / `HERMES_HOME` popped. Do not install into the real user home from tests or from this design pass.
