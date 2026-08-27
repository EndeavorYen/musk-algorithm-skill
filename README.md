# musk-algorithm

> **TL;DR** — Run Elon Musk's five-step algorithm as an evaluation, in order, on a requirement, design, process, or system. The point is the sequence: do not optimize, speed up, or automate a thing that should not exist.

This is an independent agent skill. It is **not affiliated with** Elon Musk, SpaceX, Tesla, xAI, or Walter Isaacson.

Works as a Grok skill. The same `SKILL.md` copies onto Claude, Cursor, and Hermes.

## Quick start

Clone, install, then say `musk algorithm` or `/musk-algorithm`.

```powershell
.\scripts\install.ps1 grok
```

```bash
./scripts/install.sh grok
```

Use `claude`, `cursor`, `hermes`, or `all` instead of `grok`. You get a structured report, not an immediate rewrite.

## The algorithm

Sequence **is** the algorithm. Full attributed excerpts: [`references/sources.md`](references/sources.md).

1. **Question every requirement.** A **named person**, not a department. `legal` / `safety` / `the military` is not an owner. Question it even if a smart person wrote it — including Musk. Then make the requirements less dumb.
2. **Delete any part or process you can.** If you would not add back at least **10%**, you did not delete enough. Some deletions will return. Never-put-back is failure.
3. **Simplify and optimize — only after 1–2.** "Possibly the most common error of a smart engineer is to optimize a thing that should not exist."
4. **Accelerate cycle time — only after 1–3.** Do not dig the grave faster. Musk spent Tesla-factory time speeding processes he later deleted.
5. **Automate last.** Nevada and Fremont started by automating every step. Gone-backwards is automate → speed up → simplify → delete.

Default output is a report: owners and keep/change/drop, a delete list with expected add-backs, simplify only survivors, then yes/no on accelerate and automate. The agent applies edits **only if you asked** and **only if steps 1–2 say the thing should exist**.

| If you skip ahead | What fails |
| --- | --- |
| Simplify / optimize first | Perfect answer to the wrong question |
| Accelerate before 1–3 | You speed a process that should have been deleted |
| Automate first | Robots and conveyors for work you later delete |
| Never add back 10% | Leftover waste looks like prudence |

## Origin

Musk recites this as a **mantra** because he got tired of doing it backwards.

The first systematic public telling is Tim Dodd's Everyday Astronaut *Starbase Tour and Interview with Elon Musk* (August 2021): make the requirements less dumb, then try very hard to delete the part or process. Walter Isaacson, *Elon Musk* (2023, ~pp. 284–286), writes it as **The Algorithm** — five commandments, including the named-person rule and the 10% add-back bar. On Lex Fridman Podcast #438 (August 2024) he calls it a **first principles algorithm**: "I've gone backwards so many times where I've automated something, sped it up, simplified it, and then deleted it."

One algorithm across those three tellings — not three algorithms. Quotes and "do not use" notes live in [`references/sources.md`](references/sources.md).

## Complementary to just-ten-more

Use this skill for *should this exist, who owns it, and in what order do we touch it?*

Use **[just-ten-more](https://github.com/EndeavorYen/just-ten-more)** `/just-ten-more` for *what is still wrong, with evidence — list up to 10 challenges, no edits, no review log.* A list-only round lives in the conversation. It is not the loop's log.

Use `/just-ten-more-loop` for *fix or block, write `.just-ten-more/review-log.jsonl` in the repository under review, then hunt again until a round finds none.* The loop's next round reads that log, not a prior list-only chat.

| | musk-algorithm | just-ten-more | just-ten-more-loop |
| --- | --- | --- | --- |
| Job | First-principles evaluation | Evidence-backed hunt, list only | Evidence-backed hunt-fix loop |
| Sequence | Five steps **in order** | One round of up to 10 challenges | Rounds until a round finds none |
| Default | Structured report | List in the conversation; no review log | Fixes or blockers, plus a log |
| Edits | Only if asked, after 1–2 keep it | None | Fix in the same round |

Do not merge them.

## Install

One argument: `grok` | `claude` | `cursor` | `hermes` | `all`. Default `all`. Unknown platform is rejected.

| Platform | Skill root |
| --- | --- |
| grok | `~/.grok/skills/musk-algorithm/` |
| claude | `~/.claude/skills/musk-algorithm/` |
| cursor | `~/.cursor/skills/musk-algorithm/` |
| hermes | `~/.hermes/skills/musk-algorithm/` |

```text
# Windows
.\scripts\install.ps1 grok
.\scripts\install.ps1 claude
.\scripts\install.ps1 cursor
.\scripts\install.ps1 hermes
.\scripts\install.ps1 all

# Unix
./scripts/install.sh grok
./scripts/install.sh claude
./scripts/install.sh cursor
./scripts/install.sh hermes
./scripts/install.sh all
```

If `GROK_HOME` is set, the grok target is `$GROK_HOME/skills/musk-algorithm/`.
If `HERMES_HOME` is set, the hermes target is `$HERMES_HOME/skills/musk-algorithm/`.

Claude and Cursor always use the home paths in the table.

The destination contains `SKILL.md`, `README.md`, and `references/sources.md`. Restart the agent if it was already running.

Confirm:

```powershell
Test-Path "$env:USERPROFILE\.grok\skills\musk-algorithm\SKILL.md"
```

```bash
test -f ~/.grok/skills/musk-algorithm/SKILL.md && echo installed
```

Uninstall: delete the skill directory. Nothing else is registered.

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.grok\skills\musk-algorithm"
```

```bash
rm -rf ~/.grok/skills/musk-algorithm
```

Repeat for claude, cursor, and hermes if you installed `all`. If you used `GROK_HOME` or `HERMES_HOME`, delete those paths instead.

## Usage

You can run this whenever you want. Name the subject and invoke it.

**Explicit (always):** `/musk-algorithm`, or `musk algorithm` / `run the musk algorithm on …`. Explicit invocation always runs, even if the subject is small or already shipped.

**Automatic (only when it fits):** questioning requirements, deleting before optimizing, or whether something should exist before it is sped up or automated. It does **not** load on every message.

Phrases: `musk algorithm`, `musk-algorithm`, `five-step algorithm`, `first principles algorithm`, `question every requirement`, `make requirements less dumb`, `delete before optimize`, `/musk-algorithm`.

Typical asks:

- Evaluate this design / process / requirement with the Musk algorithm.
- Question every requirement on this spec; named owners only.
- Run `/musk-algorithm` on the proposed pipeline before we automate it.

## Sources

Fair-use short excerpts only. Do not invent lines. See [`references/sources.md`](references/sources.md).

- Walter Isaacson, *Elon Musk* (Simon & Schuster, 2023), ~pp. 284–286 — “The Algorithm.”
- Everyday Astronaut, *Starbase Tour and Interview with Elon Musk*, Tim Dodd, August 2021, YouTube `t705r8ICkRw` (~13:25).
- Lex Fridman Podcast #438, August 2024 (~00:44:08) — first principles algorithm; gone-backwards order.

Do not treat a fire-suppression-pad “unowned requirement” story as Musk or Isaacson.

## Layout

```
SKILL.md                     Agent prompt
README.md                    This file
ARCHITECTURE.md              Maintainer layout and data flow
references/sources.md        Quote home
scripts/install.ps1          Windows installer
scripts/install.sh           Unix installer (git 100755, LF)
tests/                       Structural + install acceptance
```

Installed skill root: `SKILL.md`, `README.md`, `references/`. There is no `review-log.py`.
