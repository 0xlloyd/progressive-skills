# Progressive Voice

**Talk for thirty minutes. Get an AI that sounds like you.**

Builds a personal voice skill, so your AI writes and talks like you rather than like a chatbot. It works even if you rarely write: most of the material comes from a short, conversational interview, plus any messages or voice notes you already have.

## How it works

1. **Gather:** you talk through three or four short pieces (a story, an opinion, an explanation), one at a time.
2. **Probe:** quick tests catch what free talk misses: pairs of phrasings, a few everyday moments, the AI phrases that make you cringe, and how your writing differs from your speech.
3. **Analyse:** your signature phrases, swaps, connectors, hedges and rhythm, each with a verbatim quote and a dose (everyday, occasional or rare), so the result doesn't become a caricature.
4. **Test:** a blind test mixes generated pieces with your real excerpts, and whatever gives a fake away becomes a new rule.
5. **Build:** your own voice skill, which triggers whenever you ask for something written on your behalf and offers to learn from every edit you make.

## What you get

- A voice skill folder: `SKILL.md`, a lexicon and real examples
- A never-say list built from your taste rather than a generic ban list

## Use

> Build my voice.

> Make my AI sound like me, not like ChatGPT.

## Files

```
progressive-voice/
  SKILL.md                         the workflow
  references/ai-tells.md           common AI words, phrases and habits
  references/interview-prompts.md  prompts for when you get stuck
  scripts/voice_stats.py           sentence length, contractions, function words and punctuation habits
  templates/examples.md            the examples template
  templates/lexicon.md             the lexicon template
  templates/voice-skill.md         the voice skill's SKILL.md
  agents/openai.yaml               display metadata and a suggested prompt
```

## Install

Part of [progressive-skills](../README.md). To install all six and keep them in sync across machines:

```bash
git clone https://github.com/0xlloyd/progressive-skills.git ~/progressive-skills
~/progressive-skills/install.sh
```

To install only this skill, run `npx skills add 0xlloyd/progressive-skills --skill progressive-voice`, or copy the `progressive-voice/` folder into your skills directory (`~/.claude/skills/` for Claude Code). For Claude, you can also zip the folder and upload it as a custom skill.

## Works with

Works on its own; if your tool only takes a single `SKILL.md`, it still runs and improvises the missing files. Your words may become examples in the finished skill, with names, numbers and private details removed first. It closes every run with [progressive-skill-improvement](../progressive-skill-improvement/README.md), which proposes evidence-backed edits to this skill for you to approve. If that skill isn't installed, it suggests the improvements directly.

## License

MIT. See [LICENSE](../LICENSE). Created by [Lloyd Bizaoui](https://github.com/0xlloyd).
