---
name: progressive-skill-improvement
description: 'At the end of a session, review how a skill was used and propose specific, evidence-backed edits to its SKILL.md, covering what to fix, what to keep and what to remove, for the user to approve before the skill is updated. Use when another skill calls it as its closing step, or when the user asks "what did we learn", "improve this skill from this session", "update the skill with what we learned" or similar, but not for testing a skill with evals, which `skill-creator` handles.'
metadata:
  category: progressive
  tags: [skills, self-learning]
  source: Lloyd's own skill, from Session self learning-v2.zip (was session-self-learning)
---

# Progressive Skill Improvement

## Why

A lesson only counts once it changes the skill: noting what went wrong without editing the instructions means it was observed, not learned, and the same mistake will come back.
Aim to fix the cause rather than the symptom, so one edit prevents a whole class of future mistakes instead of patching a single case.

## Review

Start by reading the current SKILL.md of the skill that was used, so every lesson is judged against what the skill actually says rather than what you remember it saying.
Then walk back through the session and, for each step of the skill, ask three questions: what did the skill expect to happen, did it happen, and why or why not, asking "why" a second time to reach the root cause.

## Signals to look for

The strongest evidence is what the user did: corrections, rewordings, cuts, questions like "is this necessary?", steps they skipped or pushed back on, and anything they had to explain more than once.
Also look for friction in the work itself: steps that stalled, broke or had to be redone, and places where the skill was silent and you had to improvise.
Record what worked well too, such as steps the user accepted without change or praised, because those are the parts a careless edit could break.

## Select lessons

Turn the signals into lessons, each stating the evidence (the moment in the session), the root cause, and the type: fix, keep or remove.
Keep only lessons that pass the generalise test: the change would help other users and future sessions, not just repeat one session's specifics, because a skill overfitted to one conversation gets worse for everyone else.
Propose at most the top five lessons per session, ranked by how much they would change future runs, and prefer removing or tightening a line over adding a new one so the skill stays lean.

## Propose edits

First show the user the list of lessons, one line each with its type and evidence, and let them drop any before drafting edits.
Then present each edit one sentence at a time, showing the current wording (if any) next to the proposed wording and where it sits in the skill, and wait for the user to reply `ok`, give an edit or say `cut`.
For a removal, quote the exact sentence to be removed and ask the user to confirm, since deleting a line can quietly drop behaviour the skill relied on.

## Update and deliver

Apply only the approved edits to the full SKILL.md, keeping every other line exactly as it was, and show the user a short summary of what changed.
If the skill lives in the user's skills bank (such as `~/Documents/Skills Bank`), edit the SKILL.md there, since the bank is the source and its installed copies are links to it.
Otherwise, deliver the updated skill in the way the environment allows: a save card that replaces the existing skill where one is offered, otherwise the updated SKILL.md and a zipped skill folder for download.

## Limits

Edit only the skill that was used in the session; if a lesson belongs to a different skill or to the user's general preferences, mention it in one line and leave it for the user to decide.
If several skills were used, ask which one to review.
If nothing in the session is worth changing, say so plainly instead of inventing lessons, because a needless edit makes the skill worse.
Unlike the skills that close by running it, don't apply this skill to itself unless the user asks, so it never loops.
