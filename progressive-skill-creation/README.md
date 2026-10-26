# Progressive Skill Creation

**Research the craft. Approve every sentence. Ship a skill you wrote.**

Co-creates a new skill with you step by step: the assistant researches, proposes and drafts, but nothing enters the skill until you have approved it in your own words.

## How it works

1. **Intake:** clarifying questions until the goal, what the skill does, when it triggers, what it outputs and its constraints are clear, played back as a brief.
2. **Expert research:** how the best practitioners do the task the skill is for, shared as a short summary with sources.
3. **Plan gate:** name, description, a section-by-section outline and any bundled files, revised until you approve.
4. **Sentence-by-sentence drafting:** each sentence shown on its own for you to reply `ok`, edit or `cut`.
5. **Full read-back:** the assembled skill, checked as a whole for repetition, clashes and gaps.
6. **Testing:** realistic prompts run with `skill-creator`, with any changes approved sentence by sentence.
7. **Output:** the finished skill as a save card where offered, plus the SKILL.md and a zipped folder.

## What you get

- A finished, tested skill folder in your own words
- A closing step in every skill it creates that runs `progressive-skill-improvement`, so each skill keeps improving

## Use

> Build a new skill with me for turning meeting notes into decisions.

> Create a skill with me, step by step, for writing release notes.

## Files

```
progressive-skill-creation/
  SKILL.md            the workflow and the rules applied to every skill it creates
  agents/openai.yaml  display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-skill-creation`, or copy the `progressive-skill-creation/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

Uses [progressive-knowledge](../progressive-knowledge/README.md) to set the standard for the task, plus `go-deeper` and `skill-creator` when they're installed, and does the same thinking directly when they aren't. It closes every run with [progressive-skill-improvement](../progressive-skill-improvement/README.md), which proposes evidence-backed edits to this skill for you to approve. If that skill isn't installed, it suggests the improvements directly.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
