---
name: progressive-workflow
description: 'Use when the user says "flow", "use flow", "/flow" or "/progressive-workflow", or wants the right process for a big task rather than a fixed pipeline, even if they don''t say "flow". Designs a bespoke workflow from how expert practitioners do that kind of work, then runs it end to end with approval gates. Saves the flow to a library and improves it after every run, so the next similar task starts from a proven process instead of a blank page.'
metadata:
  category: progressive
  tags: [workflow, process]
  source: https://github.com/0xlloyd/flow
---

# Flow

## Purpose

A fixed pipeline runs every task through the same steps, but each kind of work wants its own process: a marketing piece needs references and a copy pass, a video needs a shot list and a review of takes, a business case needs criteria and costings.
This skill designs that process first, from how the best practitioners do the work, then runs it and keeps it, so the process improves each time the same kind of task comes back.
Every run produces two things: the work itself, and a saved flow that records the process, what it checked and what was learned.

## Step 1: Frame the task

Pin down in three to five bullets what is being made or decided, who it's for, what done looks like, and the constraints already known, such as format, audience, deadline or brand.
Check the user's stored preferences and memory for anything that changes the process, and turn each one into a step or a check in the flow rather than an afterthought, because a correction the user has already given once should never need giving again.
Ask at most one or two questions, and only ones whose answer changes the shape of the flow, such as who it's for or what format it ends in, since questions about content can wait for the research.
Play the frame back to the user and get their confirmation before going further, because a wrong frame sends the whole flow in the wrong direction.

## Step 2: Check the flow library

Before designing anything, look in the flow library (see Step 9) for a saved flow that fits this kind of task, matching on the task type and the "use when" line at the top of each file.
If one fits, treat it as the baseline: run it as saved unless this task clearly needs a change, and name each planned change and its reason when presenting the flow, because without a stable baseline there's no way to tell whether a change actually helped.
If a saved flow fits, skip the process research in Step 3 except for anything the flow's changelog or this task's differences flag as missing, and go straight to presenting the flow in Step 5.
If a saved flow is related but doesn't fit, don't adapt it; design a new flow, borrowing any step or check from it that the research in Step 3 confirms this task needs.

## Step 3: Research how the work is best done

This is the heart of the skill, because a flow is only as good as the expertise built into it, so research the process thoroughly rather than quickly: the aim is to find how the best practitioners actually run this kind of work, not to do the task yet.
Before searching, reframe the task the way a top professional in the field would see it, naming what they would treat as the real problem and the real bar, because an ambitious or vague request researched at face value finds only the average process; use the `go-deeper` skill for this if it's installed, and otherwise do the reframing directly.
Then set the elite standard for the process: identify the bar-setters by demonstrated results such as awards, wins or measured outcomes rather than fame, and research past generic results to practitioner books and interviews, professional bodies' guidance, training curricula and expert write-ups, preferring primary sources; use the `progressive-knowledge` skill for this if it's installed, and otherwise apply the same approach directly.
Look specifically for what shapes the process: the stages experts move through and in what order, the checks they insist on, what separates best from good, and the shortcuts they reject and why, since these become the flow's steps and its Verify list.
Aim for at least three independent strong sources, and when they disagree, record the disagreement rather than averaging it away, because where experts split is usually where the user should choose.
Look through the available skills for any that cover a stage of the work, such as image or video prompting, prose editing, deck building, critique or stakeholder rehearsal, and read the instructions of each one you plan to use.
Note which tools and connectors the flow needs, such as web or image search, output types like slides or documents, subagents for parallel research or independent review, and connections to any app the task touches, and suggest connecting any that would help but aren't available.
Search past conversations and memory for earlier runs of similar work and the corrections the user made then, because a correction given last time is a step or check this time.
Share the findings with the user as a short summary with sources, covering the bar-setters, the stages and checks experts insist on, and any disagreements, so they can steer the process before it's composed.

## Step 4: Compose the flow

Start from the six-step spine below, which most flows keep, and cut any step only with a stated reason:

| Step | What it does |
|---|---|
| Understand | Pin the goal, audience and definition of done |
| Research | Gather the context, domain knowledge and material the task itself needs |
| Plan | Set the approach and share it with the user for approval |
| Execute | Do the work, using the skill or tool mapped to each step |
| Verify | Check the output against the definition of done and the flow's checks |
| Learn | Review the run and save what was learned |

Then add or reshape steps from what the research found, using `references/modules.md` as a menu of common additions such as references, a shot list, options analysis or independent review, and add any step the research shows experts rely on even when it isn't on the menu.
Give every step a one-line reason it's there, and cut any step whose reason doesn't change the output, because a step that earns no place only slows the work.
For each step, also name the skill or tool it uses where one applies, and a short "done when" so Verify has something concrete to check against.
Order the steps so each one has what it needs before it starts, such as references before visual direction, audience before copy, and data before analysis.
Mark the gates, the pause points where the user approves or chooses before work continues: the plan always, plus any selection such as picking a concept, a draft or a take.
Draft the flow's Verify list as a short set of checks to confirm after the work is done, keeping only the critical items that are easy to miss, since a long list gets skimmed and the important checks get lost.
Scale the flow to the task, so a quick piece of work might have four steps and a launch campaign twelve.
Before presenting, check the composed flow as a whole: every step's inputs come from an earlier step, no two steps do the same job, and nothing in the definition of done is left without a step that produces it.

## Step 5: Present the flow

Present the flow compactly in this format:

```
FLOW: [task in one line]
Based on: [new / saved flow name, with changes]

 #  Step                 Why it's here        Skill / tool     Done when
 1  Understand           ...                  -                ...
 2  References           ...                  image search     ...
 3  Plan        [GATE]   ...                  -                ...
 ...

Verify checks: [the short list]
Added beyond the spine: [step, one line on why]
Cut from the spine: [step and why, or "nothing"]
```

Ask the user to approve, edit or reorder it, and wait for their answer, unless they've said "just run it", in which case skip this gate and the check-ins in Steps 1 and 3, and stop only at the plan.

## Step 6: Run the flow

Set up a task list with one item per flow step and tick each off as it finishes, so the user can see progress if they step away.
Work through the steps in order, announcing each in one short line, reading the instructions of any skill a step uses before using it, and carrying on until that step's "done when" is met.
At each gate, show the output and wait for the user before continuing.
At the Plan gate, cover the approach, the deliverables and their format, and the remaining steps, and if the task research has shown a step is unnecessary or a new one is needed, update the flow there and say why.
Where the plan involves a judgement call, such as strategy, prioritisation or a commercial or people decision, lay out the options with their trade-offs and let the user choose, while for tasks with an objectively right answer, just plan the execution.
Deliver outputs in the format the work calls for as soon as they're useful, so the user can redirect early rather than at the end.

## Step 7: Verify

Verify always runs and is never a formality, because work that grades itself without a real check ships its own mistakes.
Confirm the output against each step's "done when", the definition of done from Step 1, the flow's Verify checks, the rules of every skill used, and the user's stored preferences.
Open what was made rather than trusting it: render the deck, open the document, view the page, and run the numbers.
For high-stakes work, have a fresh agent that hasn't seen the work being produced review it against the definition of done, and if subagents aren't available, re-read the output as its intended audience would, checking only for what they need.
Fix what the checks find before presenting the work, and name the weakest remaining element honestly rather than leaving the user to discover it.

## Step 8: Review the run

Review the run with four questions: what was intended, what actually happened, why the two differed, and what to change or repeat next time.
Capture what worked as well as what went wrong, and look for causes in the process rather than blame, because a step that worked is as worth keeping as a gap is worth fixing.
Sort each lesson into where it belongs: facts about the user or their world go to memory, lessons about this kind of task go into the flow, and problems with a skill used along the way become a specific suggested fix for that skill.
Turn lessons about the task into edits to the flow's steps and Verify checks themselves, keeping only checks that caught a real problem or guard against a costly one, rather than appending notes that pile up unread.

## Step 9: Save the flow

The flow library is a single folder holding one markdown file per task type, such as `Flows/linkedin-carousel.md` or `Flows/business-case.md`.
Use the library location the user has given; if none is known, ask once, and use a `Flows/` folder until they answer.
Save the file where the library lives, preferring a folder the user owns, local or on a connected cloud drive, because it works across tools; if that can't be reached, use the assistant's built-in storage, and if neither is available, give the user the file to download and name the folder it belongs in.
If a file for this task type already exists, merge into it rather than creating a duplicate: edit the steps and checks, increase the run count, and add a dated changelog line saying what changed and why.
Name the file after the task type, not the specific task, in lowercase with hyphens (`business-case.md`, not `q3-funding-deck.md`), so it can be found for any future task of that kind.
Build the file from `references/flow-template.md`, and write it so someone reading it months later, with no memory of the original task, could run the flow on its own.
If the task is unlikely to recur, say so and ask whether to save the flow anyway, rather than filling the library with flows nobody will run again.

## Output order

End the run with a short summary in this order: what was made, the flow used and where it was saved, the two or three most important lessons, any suggested skill fixes, and the sources.

## Close

End by running `progressive-skill-improvement` on this skill so lessons about how the flow skill itself worked improve the next run; if it isn't installed, suggest any improvements to this skill directly for the user to approve.
