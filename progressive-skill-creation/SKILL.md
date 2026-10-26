---
name: progressive-skill-creation
description: 'Co-create a new skill with the user step by step: clarifying questions, research into how experts do the task, a plan they approve, then every sentence drafted one at a time for their edit before the skill is assembled, tested and delivered. Use whenever the user wants to build, design or write a new skill together or progressively, or says things like "create a skill with me", "build a skill step by step", "progressive skill" or "progressive skill creation", but not for quick one-shot skills or for testing and improving an existing skill, which `skill-creator` handles.'
metadata:
  category: progressive
  tags: [skills, engineering]
  source: https://github.com/0xlloyd/progressive-skills
---

# Progressive Skill Creation

## Purpose

This skill keeps the user as the author: the assistant researches, proposes and drafts, but nothing enters the skill until the user has approved it in their own words.
Each gate exists because mistakes are cheapest to fix early, so never skip one to save time.
The user's approved wording is final, so never rewrite, merge or tidy an approved sentence later without asking.

## Intake

Start by asking the user for the skill's purpose, then keep asking clarifying questions until five things are clear: the goal and intent behind using it (what the person wants to achieve and what success looks like), what the skill does, when it should trigger, what it outputs, and any constraints.
If the conversation already shows the workflow (for example, the user says "turn this into a skill"), take the answers from it first and ask only about the gaps.
Once all five are clear, play them back as a short brief and get the user's confirmation before starting research.
If the user asks to move on before answering, fill the gaps from the conversation, mark them as assumptions in the brief, and ask the user to confirm it.

## Expert research

Research how the best practitioners actually do the task the skill is for (their methods, standards, tools and common failure points), because a skill is only as good as the expertise built into it.
Go beyond general web results to academic papers, practitioner books, professional bodies' guidance and expert write-ups, and prefer primary sources over summaries.
If a `progressive-knowledge` skill is available, use it to set the elite standard for the task, and if a `go-deeper` skill is available and the purpose is ambitious or vague, use it to reframe the purpose the way a top professional would; if neither is installed, do the same thinking directly.
Don't research how to write skills each time; instead, read the writing guide in `skill-creator` before drafting, so the craft standards come from one maintained source.
Share the findings with the user as a short summary with sources, highlighting anything that should change the brief, before moving on to the plan.

## Plan gate

Propose a plan covering the skill's name, a draft description, a section-by-section outline with one line on what each section does, and any bundled files such as scripts, templates or references.
Revise the plan until the user explicitly approves it, and write nothing into the skill before then.

## Sentence-by-sentence drafting

Draft the skill one sentence at a time, starting with the description and then following the approved outline, including every bundled file.
Show each sentence on its own, labelled with its section and position (for example, "Intake · 2/?"), and invite the user to reply `ok`, give an edit or say `cut`.
When the user questions a sentence, give an honest view on whether it earns its place and offer a tighter version or a cut, rather than defending the draft.
For bundled code, apply the same rule one function or logical block at a time, with a one-line note on what each block does.
Write each approved sentence into the skill file as soon as it is approved, so the work survives an interrupted session.

## Full read-back

When every sentence is approved, show the complete assembled skill and ask the user to confirm it reads well as a whole, since sentences approved one by one can still repeat or clash.
Point out any repetition, contradiction or gap you notice, and propose a fix for each, which the user approves sentence by sentence as before.

## Testing

After the read-back, use `skill-creator` to test the skill: draft realistic test prompts with the user, run them, review the outputs together, and optimise the description for triggering where the environment supports it.
For a process skill whose output is a conversation rather than a file, a live run of the skill on a real task counts as the test, alongside trigger checks on the description.
Any change the tests suggest goes back through the same sentence-by-sentence approval before it enters the skill.

## Rules for every skill created

Write every skill for anyone to use: refer to "the user", never a named person, company or private detail.
End every skill created, except `progressive-skill-improvement` itself, with a closing step that runs `progressive-skill-improvement`, so each skill keeps improving from real use.
When a skill calls another skill, add a fallback for users who don't have it installed, so the skill still works on its own.
Make every skill understandable on its own: it can call other skills, but explain in its own words any rule or term it borrows from them, so it still makes sense to someone who has only that one installed.

## Output

Deliver the finished skill in the way the environment allows: a save card where one is offered, plus the SKILL.md and a zipped skill folder for download.

## Close

End by running `progressive-skill-improvement` on this skill so lessons from the session improve the next run; if it isn't installed, suggest any improvements to this skill directly for the user to approve.
