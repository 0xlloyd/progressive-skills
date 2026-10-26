# Progressive Skill Creation

**Research the craft. Approve every sentence. Ship a skill you wrote.**

An AI skill for co-creating a new skill step by step: clarifying questions, research into how experts do the task, a plan you approve, then every sentence drafted one at a time for your edit before the skill is assembled, tested and delivered.

## Files

- [SKILL.md](SKILL.md) — the full workflow and the rules applied to every skill it creates.
- [agents/openai.yaml](agents/openai.yaml) — optional display metadata and a suggested prompt.
- [README.md](README.md) — usage and licence.

## Use

Install with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 0xlloyd/progressive-skill-creation --skill progressive-skill-creation
```

For manual installation, use this repository root as the skill folder in your host's documented custom-skills location. You can also attach or paste [SKILL.md](SKILL.md) into a conversation and explicitly ask your AI tool to follow it.

> Use Progressive Skill Creation to build a new skill with me for turning meeting notes into decisions.

The workflow moves through intake, expert research, a plan gate, sentence-by-sentence drafting, a full read-back, testing, delivery and a self-learning close. It works best alongside [best-in-class](https://github.com/0xlloyd/best-in-class), a go-deeper skill, skill-creator and session-self-learning, and falls back to doing that thinking directly when they aren't installed.

Created by [Lloyd Bizaoui](https://github.com/0xlloyd).

<details>
<summary>MIT License</summary>

```text
MIT License

Copyright (c) 2026 Lloyd Bizaoui

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>
