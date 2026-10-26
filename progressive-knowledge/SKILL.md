---
name: progressive-knowledge
description: 'Define the elite standard for a task from proven practitioners, build a confidence-tagged rubric, do or rebuild the work to that bar, and save a domain knowledge file so the standard compounds over time. Use whenever the user asks for the best, best-in-class, world-class, gold-standard or Michelin-level version of something, or asks "is this the best?" about finished work, even if they don''t use the words "best in class".'
metadata:
  category: progressive
  tags: [knowledge, research]
  source: https://github.com/0xlloyd/progressive-skills
---

# Progressive Knowledge

## Purpose

Most answers default to the typical version of a task, which is what the top search results say: usually popular, search-optimised and average.
This skill replaces that with the standard the best practitioners in the domain actually work to, so a recipe becomes the one a Michelin pastry chef would use and a how-to becomes the practices experts follow rather than just the steps.
Every run produces two things: the work done (or judged and rebuilt) to that standard, and a knowledge file capturing the standard so the next run in that domain starts from it.

## Define what best means

"Best" depends on context, so pin it down before researching, starting with the domain and sub-domain (for example, Food > Pastry > Laminated dough).
Then name who sets the bar, choosing them by demonstrated results such as awards, competition wins or measured outcomes rather than fame, because reputation alone can mislead.
Then state what best optimises for in this context, such as quality, rigour, craft, speed or safety, since a deck for a CEO optimises for a clear decision while a reference guide optimises for completeness.
Play these three back to the user as a short brief and get their confirmation before researching, because a wrong definition of best wastes all the research built on it.

## Check the library

Before searching, look in the knowledge library (see Save the knowledge file) for an existing file on this topic.
If one exists, read it and research only what's missing or out of date, so each run builds on the last instead of repeating it.

## Research the elite standard

Research past the generic results to academic papers, practitioner books and interviews, professional bodies' guidance, training curricula and expert write-ups, preferring primary sources over summaries.
Adding elite qualifiers to searches, such as Michelin, award-winning, competition-grade, masterclass or "how top X do Y", helps get past the average answers.
Look specifically for what separates best from good (the techniques, ratios, tolerances and habits experts insist on that generic guides skip) and for the common defaults experts reject, along with why they reject them.
Aim for at least three independent strong sources, prefer depth over volume, and discount listicles, content farms and forums unless a recognised expert is speaking.
When sources disagree, record the disagreement rather than averaging it away, because where experts split is often where the user's own judgement matters most.
If web search isn't available, build the standard from what you already know of the recognised experts and their methods, and tell the user the sources are unverified so the confidence tags reflect it.

## Share the findings

Share what the research found as a short summary with sources, covering the bar-setters, what separates best from good, and the defaults to avoid.
Flag anything that should change the brief, and get the user's go-ahead before building the rubric, so they can steer the standard before it shapes the work.

## Build the rubric

Distil the research into 5–7 criteria that define best in class for this task, because more than that dilutes focus and fewer usually misses something that matters.
For each criterion, give a plain name, the generic version (what the average answer does), the best-in-class version, why it matters to the outcome, its source, and a confidence tag.
Describe quality, not counts: "butter at 12–14°C during lamination so the layers don't fuse" is a criterion, while "high quality" or "includes three examples" is not.
Tag confidence as High when several strong sources agree, Medium when the support is thinner or indirect, and Low when it rests on one expert's view or the sources conflict, so the user knows which parts of the standard are settled.

## Adapt to the user's context

Don't copy the experts' practices wholesale: for each criterion, carry over the reason it works and apply that reason to the user's situation, constraints and resources.
For example, a pastry kitchen's blast chiller becomes a home freezer with shorter rest intervals, because the point is keeping the butter cold, not owning the equipment.

## Do or review the work

If the user hasn't supplied existing work, do the task to the rubric, briefly saying why each step a generic answer would skip is there, and remember that best in class means better, not longer.
If the user has supplied existing work, score it against each criterion as Meets, Partly or Misses with one line of evidence, then give an honest overall verdict, because a flattering review defeats the point of the skill.
Then, unless it already meets every criterion, deliver the full rebuilt version in the same response and the same format as the original, without asking first, because the point of asking "is this the best?" is to end up with the best.
If a best-in-class choice still costs real extra effort after adapting, keep it in the delivered work and add a one-line note on the shortcut, rather than giving two versions.
If the user only wants to know what best in class looks like, with no task to do or review, skip this section and go straight to saving the knowledge file.
Close the work with a short generic vs best-in-class comparison of three to five lines, so the difference the standard made is visible.

## Save the knowledge file

The knowledge library is a root folder with one subfolder per domain, each holding one markdown file per topic, such as `Pastry/laminated-dough.md`.
Use the library location the user has given; if none is known, ask once, and use a `Best in Class/` folder until they answer.
Save the file where the library lives, preferring a folder the user owns (local or a connected cloud drive) because it works across tools; if that can't be reached, use the assistant's built-in storage, and if neither is available, give the user the file to download and name the folder it belongs in.
If a file for this topic already exists, merge into it rather than creating a duplicate: update criteria, add new sources, keep what's still valid, and add a dated changelog line.
Name the file after the topic, not the task, in lowercase with hyphens (`laminated-dough.md`, not `croissant-request.md`), so it can be found again for any future task in that topic.
Build the file from `references/knowledge-file-template.md`, and write it so someone reading it months later, with no memory of the original task, could apply the standard on its own.

## Output

Present the response in this order: a one-line statement of the domain and what best means here, the work (or the scored review followed by the rebuilt version), the generic vs best-in-class comparison, where the knowledge file was saved, and the sources.

## Close

End by running `progressive-skill-improvement` on this skill so lessons from the session improve the next run; if it isn't installed, suggest any improvements to this skill directly for the user to approve.
