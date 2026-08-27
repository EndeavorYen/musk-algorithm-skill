---
name: musk-algorithm
description: >
  Evaluate a requirement, design, process, or system with Musk's
  first principles algorithm. Use when the user says
  musk algorithm, musk-algorithm, five-step algorithm, first principles algorithm,
  make requirements less dumb, delete before optimize, question every requirement,
  or runs /musk-algorithm. Explicit invocation always runs, on whatever subject
  they named. Use when a surviving operator surface still names a process
  that was just deleted.
---

Speak in the user's language.

Run this five-step algorithm in order. Sequence is the algorithm. Default
output is a structured evaluation report, not a code rewrite
(report-not-rewrite). Do not start a just-ten-more hunt or just-ten-more-loop.
Do not implement unless asked.

## When

If the user names this skill, says musk algorithm, or runs /musk-algorithm,
run it on whatever they pointed at: a requirement, design, process, system,
code, or docs. Explicit invocation always wins. Do not refuse because the
subject is small, already shipped, or not a greenfield design.

Auto-load when they are about to optimize, speed up, or automate something
that may not need to exist, or when they ask to question requirements or
delete parts of a design.

Do not auto-load for ordinary implementation, a bugfix, or an evidence-backed
hunt. Complementary; never merge.

`just-ten-more` lists up to 10 evidence-backed challenges. It does not fix
and does not write a review log. `just-ten-more-loop` fixes or records
blockers, writes `.just-ten-more/review-log.jsonl`, and hunts again.

If they asked only to list challenges, stop this skill and use just-ten-more.
If they asked to hunt bugs, fix them, and log challenges, stop this skill
and use just-ten-more-loop.

## Stance

Force this order. Cannot skip ahead. Cannot reverse order. Each step must
emit its artifacts before the next step starts. If the user asks to jump
to simplify, accelerate, or automate, refuse and resume at the first
incomplete step.

Enforce the named-person bar and the 10% add-back bar. Changes are
apply-only-if-asked: apply changes only if the user asked AND steps 1–2
say the thing should exist.

Quotes live in `references/sources.md`. Do not invent lines. Do not
retell the biography. Do not present a fire-suppression-pad
unowned-requirement story as Musk or Isaacson.

Corollaries (hands-on managers, urgency, physics vs recommendations) are
adjacent, not the five steps. Physics is law; everything else is a
recommendation.

## 1. Question every requirement

Named-person rule: a person, not a department. "Legal," "safety," or
"the military" is not an owner. Question even if it came from a smart
person or from Musk. Then make the requirements less dumb.

Artifact — every requirement in a table:

| Requirement | Named owner | Keep / change / drop | Less-dumb form (if change) |

Unowned or department-owned items default to drop unless physics forbids
it. A missing name is not an owner.

## 2. Delete any part or process you can

Delete what step 1 dropped, and delete any remaining part or process you
can. If you would not add back at least 10%, you did not delete enough.
Warn that some deletions will return. Over-conservative never-put-back
is failure.

Artifact:

- Delete list (part or process, why)
- Expected add-backs (at least 10% of the delete list, or delete more)
- Warning that some deletions will be put back

Deleting a process from the live path is not the same as deleting the
module. Leftover code in the tree is not a remaining requirement. Do
not optimize leftover modules as if they still gate the operator.

Inspect the surviving operator-facing surface (the button, the card,
the report). If it still names, requires, or looks finished because of
a deleted process, the delete is incomplete. Chrome is not a
requirement. Do not keep running a process because the surface still
lists it.

A merge or green CI is not proof the deleted process is gone from the
live surface.

If the whole subject is deleted, steps 3–5 are N/A. Accelerate: no.
Automate: no.

## 3. Simplify and optimize

Only after 1–2, and only for survivors. Do not optimize a thing that
should not exist.

Artifact — for each survivor: what to simplify or optimize, or
`none — deleted in step 2`.

## 4. Accelerate cycle time

Only after 1–3. Do not speed a process that should have been deleted
(grave-digging).

Artifact — Accelerate: **yes** or **no**, naming the surviving process
and the cycle to shorten. If no, say why (nothing left, or steps 1–3
incomplete).

## 5. Automate

Last. Do not automate first. Gone-backwards is automate → speed up →
simplify → delete (Nevada / Fremont). Automate last.

Artifact — Automate: **yes** or **no**. Never yes if steps 1–4 are
incomplete or the thing was deleted.

## After the report

Default is report-not-rewrite. If the user later asks to implement, do
not re-run this skill as a rewrite. Hand surviving contracts to
just-ten-more. Do not mix the two in one pass.

## Rationalizations

Reject these and continue:

- "Legal / safety / the military required it" — name the person or drop it.
- "A smart person said so" — question it harder.
- "In case we need it" — delete; add back if needed.
- "We never put anything back, so we deleted correctly" — you did not delete enough.
- "Optimize / speed / automate now; delete later" — gone-backwards; forbidden.
- "It is already automated, so keep it" — sunk cost is not a requirement.
- "The module is still in the tree, so keep the process" — leftover code is not a live-path requirement.
- "The card still lists it, so we should still run it" — chrome is not a requirement; delete the chrome with the process.
- "Merge means the delete landed" — go-live is the operator surface, not the merge.
- "Musk report done, rewrite now" — report-not-rewrite. Implement only if asked, as a separate hunt-fix.

## Report

Emit this report. Fill every section. Do not skip a heading.

```
# Musk algorithm evaluation

## 1. Requirements
(table: named owners; keep / change / drop)

## 2. Deletions
(delete list + expected add-backs + warning)
(live-path vs leftover tree; surviving surface check)

## 3. Simplify and optimize
(survivors of 1–2 only)

## 4. Accelerate
(yes / no)

## 5. Automate
(yes / no)

## Order-check
Steps ran 1→5. No skip. No reverse. If anything was optimized, sped, or
automated that steps 1–2 would drop, mark FAIL and return to that step.
If the surviving surface still names a deleted process, mark FAIL and
return to step 2.

## Decision
Keep, change, or drop the subject. Apply changes only if the user asked
AND steps 1–2 say the thing should exist. Otherwise report only.
```
