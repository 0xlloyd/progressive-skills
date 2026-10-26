# Best in Class

**Not the typical answer. The standard the best practitioners actually work to.**

An AI skill that replaces the popular, search-optimised answer with the elite standard for a task, then does the work (or rebuilds yours) to that bar, and saves the standard as a knowledge file so the next run in that domain starts from it.

## How it works

1. **Define best, and check with you.** It names the domain, the people who set the bar (chosen by demonstrated results, not fame) and what best optimises for here, then plays this back for your confirmation.
2. **Check the library.** If a knowledge file for the topic already exists, it builds on it rather than starting over.
3. **Research the elite standard.** Academic papers, practitioner books, professional bodies and expert write-ups, looking for what separates best from good and the defaults experts reject.
4. **Share the findings, and check with you again.** A short summary with sources, so you can steer the standard before it shapes the work.
5. **Build the rubric.** 5–7 criteria that describe quality rather than counts, each tagged High, Medium or Low confidence.
6. **Adapt to your context.** It carries over why each practice works, not the practice itself.
7. **Do or review the work.** It builds to the rubric, or scores your draft, gives an honest verdict and delivers the full rebuilt version, ending with a short generic vs best-in-class comparison.
8. **Save the knowledge file.** In a folder you own where possible, otherwise your assistant's built-in storage, otherwise as a download.

## Files

- [SKILL.md](SKILL.md) — the workflow.
- [references/knowledge-file-template.md](references/knowledge-file-template.md) — the template for each saved knowledge file.
- [agents/openai.yaml](agents/openai.yaml) — optional display metadata and a suggested prompt.
- [README.md](README.md) — usage and licence.

## Use

Install with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 0xlloyd/best-in-class --skill best-in-class
```

For manual installation, use this repository root as the skill folder in your host's documented custom-skills location. You can also attach [SKILL.md](SKILL.md) and the [template](references/knowledge-file-template.md) to a conversation and ask your AI tool to follow them.

Example prompts:

> Give me a best-in-class croissant recipe.

> Is this the best? [paste or attach your draft]

> What does best in class look like for a product requirements document?

Fresh research needs web access; without it, the skill builds the standard from what the model already knows and marks it unverified. Tell your assistant where your knowledge library lives, and keep private notes outside this public repository. It ends by running a `session-self-learning` skill if you have one, or suggesting improvements to itself if you don't. Behaviour depends on the host and model.

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
