# Research standard

Use these eight criteria to research a design system the way a senior designer would, before proposing any options.
Each criterion gives the generic habit to avoid, what good practice does instead, and why it matters, so the research can be adapted to any project.

## 1. The subject's own story

- **Generic habit:** starting from trends, design galleries and moodboard sites.
- **Good practice:** research the project's own history, place, era, materials, people and audience first, and note anything with a visual trace (old signage, packaging, documents, buildings, local typography, materials the product is made of).
- **Why:** this is where options nobody else can copy come from, and it gives every bespoke option a reason the user can explain. Identity studios routinely find their strongest type and colour ideas here, such as a typeface from the same year an organisation was founded, or lettering from the period of a building.
- **When there's little history:** use the audience's world instead (their tools, places, rituals and the objects they handle).

## 2. The category map

- **Generic habit:** ignoring competitors, or quietly imitating them.
- **Good practice:** collect four to eight others in the same category (direct competitors, plus one or two the user admires). For each, note colour, type, imagery, layout, shape and tone. Name the conventions most of them share and the space nobody occupies.
- **Why:** without a map, work drifts toward category norms because everyone draws on the same references.
- **The user's call:** experts disagree on when to break conventions. Breaking helps when the category looks the same and the brand can back up being different; following helps when trust depends on familiarity or the difference lies elsewhere (service, price). Breaking them is the default stance in this skill; following one must be the user's deliberate choice, logged with its reason.

## 3. Type chosen from purpose

- **Generic habit:** scrolling a font menu until something looks nice, and previewing with placeholder text.
- **Good practice:** start from tone, reading context (long reading, scanning, data, display), and reading duration. Test every candidate with the user's real copy at real sizes, from caption to display.
- **Why:** placeholder text hides problems with letter frequency, word length, numerals and rhythm; a face that sings in a headline can tire readers in a paragraph.

## 4. Pairing rationale

- **Generic habit:** "they look good together".
- **Good practice:** pair by contrast of role (display versus text, or text versus data) with shared DNA (similar x-height, proportions, era or designer). State the reasoning for every pair. Superfamilies (serif, sans and mono designed together) are the low-risk route; one well-chosen family with several weights is often enough.
- **Why:** mismatched x-heights make two faces look like different sizes at the same point size, and pairs with no shared DNA feel accidental.
- **Check:** keep to two or three families; compare x-heights side by side at the body size.

## 5. Colour built for the medium

- **Generic habit:** picking hex values by eye, then checking contrast at the end.
- **Good practice:** work in OKLCH, where lightness matches what the eye sees across hues. Build ramps by holding hue and stepping lightness, check contrast as each colour is created (`scripts/color_check.py`), and check gamut for the medium: sRGB for most screens, Display P3 for modern screens if wanted, and a print proof for anything with high chroma going to print.
- **Why:** in HSL, a yellow and a blue with the same lightness value look very different, so accessible and attractive palettes become a trade-off. Perceptual spaces remove most of that trade-off.
- **Tests:** WCAG 2 contrast (4.5:1 body text, 3:1 large text and interface elements) as the legal baseline, APCA as a second opinion for reading comfort, and a grayscale pass so meaning never relies on hue alone.

## 6. Practical fitness

- **Generic habit:** assuming any font or colour can be used anywhere.
- **Good practice:** before a typeface becomes an option, check its licence (desktop, web and app use are often licensed separately; open-licence fonts such as those under the SIL Open Font License are free for commercial use), language coverage for every language the system needs, the weights and styles available, optical sizes, and file weight for the web.
- **Why:** a beautiful font that can't be legally or technically shipped is not an option. Free sources include Google Fonts and Fontshare; independent foundries offer more distinctive faces at a cost.

## 7. Provenance and divergence

- **Generic habit:** references from the same galleries everyone uses, and options with no stated origin.
- **Good practice:** draw references from outside design galleries (archives, signage, print, film, architecture, nature, the subject's world). Label every option as AI default or bespoke using `references/ai-defaults.md`, and trace each bespoke option to the brief, a named inspiration or a research finding.
- **Why:** telling an AI tool to avoid defaults only moves it to the next most common choice. A stated source is what makes an option specific to this project.

## 8. The art of the possible

- **Generic habit:** designing for the medium as it was a few years ago: static images, two web-safe weights, sRGB only, fade-in animations.
- **Good practice:** for each medium in the brief, look up what current technology supports and what the most inventive work in and outside the category is doing, then turn the strongest ideas into directions. Examples to check, not a fixed list:
  - **Web:** variable fonts and optical sizes, wide-gamut (Display P3) colour, container queries, scroll-driven animation, view transitions, `:has()`-driven states, SVG and canvas generative patterns, WebGL and 3D, live data.
  - **Social:** animated and video carousels, kinetic typography, animated charts, loops, Lottie and short motion posts, platform features that change how content is seen.
  - **Slides and video:** motion templates, data that builds on screen, variable-font animation.
  - **Imagery:** generative or procedural patterns built from the brand's own shapes, 3D renders, AI-assisted imagery where the brief allows it.
- **Why:** a system that only uses what everyone already uses can't trace its own trail. Offering what's possible lets the user choose ambition knowingly instead of defaulting to static.
- **Check:** for each idea, note browser or platform support, file size, accessibility (reduced motion, contrast, alt text) and how hard it is to produce every week, so the user sees the cost before choosing.

## Sharing the research

Summarise visually in a few short sections: the subject's story (what has a visual trace), the category map (conventions to break and any to keep), type and colour directions (with licence and contrast notes), the art of the possible for each medium (with cost notes) and open questions for the user. List sources.
