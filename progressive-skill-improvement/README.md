# Progressive Skill Improvement

**A lesson only counts once it changes the skill.**

At the end of a session, reviews how a skill was used and proposes specific, evidence-backed edits to its SKILL.md, covering what to fix, what to keep and what to remove, for you to approve before anything changes. Every other progressive skill runs it as its closing step.

## How it works

1. **Review:** it reads the skill's current SKILL.md, then walks back through the session asking what was expected, what happened and why.
2. **Signals:** your corrections, rewordings, cuts and pushback first, then friction in the work, plus what worked and must not break.
3. **Select lessons:** at most five, each with its evidence, root cause and type (fix, keep or remove), kept only if they would help future sessions.
4. **Propose edits:** the lesson list first, then each edit one sentence at a time, current wording next to proposed, for you to reply `ok`, edit or `cut`.
5. **Output:** only the approved edits applied, with a short summary of what changed, committed and pushed where the skill lives in a git repository.

## What you get

- An updated SKILL.md with only the edits you approved
- A one-line note on any lesson that belongs to a different skill

## Use

> What did we learn? Improve the skill from this session.

> Update progressive-workflow with what we learned today.

## Files

```
progressive-skill-improvement/
  SKILL.md            the workflow
  agents/openai.yaml  display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-skill-improvement`, or copy the `progressive-skill-improvement/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

Called as the closing step of [progressive-design-system](../progressive-design-system/README.md), [progressive-knowledge](../progressive-knowledge/README.md), [progressive-skill-creation](../progressive-skill-creation/README.md), [progressive-voice](../progressive-voice/README.md) and [progressive-workflow](../progressive-workflow/README.md), or on its own for any skill. It doesn't review itself unless you ask, so it never loops. For testing a skill with evals, use `skill-creator`.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
