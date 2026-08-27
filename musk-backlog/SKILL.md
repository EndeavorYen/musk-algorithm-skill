---
name: musk-backlog
description: >
  Turn a musk-algorithm evaluation report into forge-agnostic work items,
  then stop. Use when the user says musk-backlog, musk backlog,
  open work items from the musk report, musk report to issues, or runs
  /musk-backlog. Explicit invocation always. Do not use to implement,
  open a PR/MR, run just-ten-more, or re-run musk-algorithm.
---

Speak in the user's language.

Turn a musk-algorithm evaluation report into forge-agnostic work items,
then stop. This skill is not an implementation pipeline. It is not a
pull request or merge request. It is not a workflow identity. Do not
merge the pass with musk-algorithm, just-ten-more, or just-ten-more-loop.
This file lives in the musk-algorithm-skill repo. It is not a second
GitHub repository.

Do not start musk-algorithm.
Do not start a just-ten-more hunt or just-ten-more-loop.
Do not implement. Do not open a pull request or merge request.
Do not write a file to preserve memory.

## When

If the user names this skill, says musk-backlog, musk backlog, open work
items from the musk report, musk report to issues, or runs /musk-backlog,
run it. Explicit invocation always.

Do not auto-load only because a musk report appeared. Complementary;
never merge.

`musk-algorithm` evaluates a requirement, design, process, or system.
Default output is a structured evaluation report in the conversation, no
evaluation file.

`just-ten-more` lists up to 10 evidence-backed challenges. It does not fix
and does not write a review log. `just-ten-more-loop` fixes or records
blockers, writes `.just-ten-more/review-log.jsonl`, and hunts again.

If they asked to evaluate a requirement, design, process, or system,
stop this skill and use musk-algorithm. Do not re-run musk-algorithm
from here. Do not invent a report.

If they asked only to list challenges, stop this skill and use just-ten-more.

If they asked to hunt bugs, fix them, and log challenges, stop this skill
and use just-ten-more-loop.

## Input

The input is a musk-algorithm evaluation report. Take it from the
conversation, a paste, or a path they named.

Missing report -> stop. Do not re-run musk-algorithm. Do not invent a
report. Do not invent a default path. Do not write a file to preserve
memory.

Do not invent a default report path. If they named no path, read from
the conversation or paste only.

## Map

This file is the one home of the mapping.

- keep -> work item from that requirement
- change -> work item from the less-dumb form
- drop -> no work item (drop is no work item)
- delete-list row -> work item ONLY when deleting is itself the work
  (delete-work). A gone process with nothing left to remove is not an item.
- accelerate:no / automate:no -> no item for speeding or automating
- whole subject dropped and no delete-work -> empty list, stop

Do not invent items that are not in the report. Do not turn a drop into
work unless it is delete-work.

## Forge

Read the git remote and the default branch. Tracker is optional.

Classify the remote as GitHub, GitLab, or other-or-none. Do not enumerate
every forge.

GitHub is github.com. GitLab is gitlab.com or a host that is GitLab.

Do not assume GitHub because a GitHub MCP exists. Never invent a GitHub
repo. Never open GitHub issues for a non-GitHub remote.

Default branch is whatever the repo uses. Do not assume main.

After listing the table: create tracker items only if that forge has a
usable tracker and credentials.

No tracker / no credentials / other-or-none -> the conversation table is
success, not failure.

This skill still does not open a pull request or merge request.

## Report table

Emit this table in the conversation. Columns:

| id | source | title | body | tracker | tracker-ref |

source is keep, change, or delete-work.
tracker is github, gitlab, or none.

Fill tracker-ref only when a tracker item was created. If tracker is
none, leave tracker-ref empty.

Then stop. Later implement, review, or open a PR/MR only if they ask,
and that is NOT this skill.

## Rationalizations

Reject these and continue (or stop, when the job is already done):

- "The report is missing, so re-run musk-algorithm" — stop. Do not invent a report.
- "A musk report appeared, so auto-load" — explicit invocation always; do not auto-load only because a report appeared.
- "GitHub MCP exists, so this is GitHub" — do not assume GitHub because a GitHub MCP exists. Never invent a GitHub repo.
- "No tracker, so this failed" — no tracker: the conversation table is success.
- "Open a PR/MR to land the items" — this skill does not open a pull request or merge request.
- "Implement the items now" — then stop. Later implement is not this skill.
- "List challenges while we are here" — stop this skill and use just-ten-more.
- "Hunt, fix, and log" — stop this skill and use just-ten-more-loop.
- "Evaluate first; we have no report" — stop this skill and use musk-algorithm.
- "Drop means a ticket to drop it" — drop is no work item unless it is delete-work.
- "accelerate:no / automate:no still need tickets" — no item for speeding or automating.
- "Write a file so we remember" — do not write a file to preserve memory.
- "The remote is other, invent a GitHub repo" — never invent a GitHub repo.
- "This skill needs its own GitHub repo" — it lives in musk-algorithm-skill as musk-backlog/SKILL.md.
