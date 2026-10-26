# Progressive Knowledge

**Not the typical answer. The standard the best practitioners actually work to.**

Replaces the popular, search-optimised answer with the elite standard for a task, does the work (or rebuilds yours) to that bar, and saves the standard as a knowledge file so the next run in that domain starts from it.

## How it works

1. **Define best:** the domain, the people who set the bar (chosen by results, not fame) and what best optimises for, played back for your confirmation.
2. **Check the library:** if a knowledge file for the topic exists, it builds on it instead of starting over.
3. **Research the elite standard:** papers, practitioner books, professional bodies and expert write-ups, looking for what separates best from good.
4. **Share the findings:** a short summary with sources, so you can steer the standard before it shapes the work.
5. **Build the rubric:** five to seven criteria that describe quality, each tagged High, Medium or Low confidence.
6. **Adapt to your context:** it carries over why each practice works, not the practice itself.
7. **Do or review the work:** it builds to the rubric, or scores your draft and delivers the rebuilt version, ending with a generic vs best-in-class comparison.
8. **Save the knowledge file:** in a folder you own where possible, otherwise your assistant's storage, otherwise as a download.

## What you get

- The work, done or rebuilt to the standard
- A short generic vs best-in-class comparison
- A knowledge file per topic, such as `Pastry/laminated-dough.md`, that later runs build on

## Use

> Give me a best-in-class croissant recipe.

> Is this the best? [paste or attach your draft]

> What does best in class look like for a product requirements document?

## Files

```
progressive-knowledge/
  SKILL.md                               the workflow
  references/knowledge-file-template.md  the template for each saved knowledge file
  agents/openai.yaml                     display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-knowledge`, or copy the `progressive-knowledge/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

Works on its own. Fresh research needs web access; without it, the skill builds the standard from what the model knows and marks it unverified. Tell your assistant where your knowledge library lives, and keep private notes out of public repositories. It closes every run with [progressive-skill-improvement](../progressive-skill-improvement/README.md), which proposes evidence-backed edits to this skill for you to approve. If that skill isn't installed, it suggests the improvements directly.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
