# Decision map

The rounds in SKILL.md each settle a bundle of decisions at once. This map lists, per round, what a direction must decide and how to render it, with modules for each medium. Use the modules that match the media in the brief; a system for a website and LinkedIn uses both.
Every decision a round settles goes into the decision log with its ID, even when the bundle settled it implicitly, so update mode can re-check it later. Anything not needed is logged as "not needed" rather than left out.

## Contents

1. Round 1: Direction
2. Round 2: Foundations
3. Round 3: Components (web, social, slides, app, print)
4. Round 4: Motion (web, social, video)
5. Round 5: Imagery and voice
6. Round 6: Data and infographics
7. Derived details (the review batch)
8. Extra layers from inspirations

## 1. Round 1: Direction

Each of the ten directions is a full mockup in the main medium (a homepage for a website, a cover plus one content slide for social), combining:

| ID | Decision |
|---|---|
| D1 | Colour strategy: how much colour, and where it lives (base, accents, backgrounds) |
| D2 | Signature colour |
| D3 | Type character: one family or a pairing, and its personality |
| D4 | Shape language: square, soft, pill, organic, outlined or flat |
| D5 | Density and layout character: airy or dense, grid or editorial, centred or asymmetric |
| D6 | Motion character: still, subtle, expressive or kinetic |
| D7 | Convention stance: which category conventions are broken and which are followed on purpose |

Spread the ten directions widely: different colour strategies, type characters and motion characters, at least two that use something from the art-of-the-possible research, and one AI default within the brief.

## 2. Round 2: Foundations

Each direction is a complete specimen: palette with ramps and roles, type scale in real copy, spacing and shape shown on a sample layout.

| ID | Decision | Tokens |
|---|---|---|
| F1 | Palette: signature, supporting colours, neutrals, built in OKLCH | `color.brand.*`, `color.neutral.*` |
| F2 | Ramps: steps per colour | `color.*.50`–`900` |
| F3 | Roles: page, surface, card, border, text, muted text, emphasis, highlight, focus | `color.bg`, `color.text`… |
| F4 | Status and data colours, or a way to show good and bad without them | `color.status.*`, `color.data.*` |
| F5 | Dark theme: whether, and how roles map | dark set |
| F6 | Type family or families, with licence and language coverage | `font.family.*` |
| F7 | Type scale per medium (web uses rem; social uses px on the slide size) | `font.size.*` |
| F8 | Weights, line heights, letter-spacing, case and punctuation rules | `font.*` |
| F9 | Spacing scale and grid per medium | `space.*`, `layout.*` |
| F10 | Radius, borders and elevation | `radius.*`, `border.*`, `shadow.*` |
| F11 | Texture or surface treatment, if any | recorded in DESIGN.md |

Check contrast for every role pairing before showing a direction.

## 3. Round 3: Components

Each direction is the whole kit assembled into real pages or sequences, with states shown.

### Web module

| ID | Component | States and variants to show |
|---|---|---|
| W1 | Navigation: header, menu, mobile menu | default, active page, open menu, scrolled |
| W2 | Hero | with image or media, with motion |
| W3 | Buttons and links | primary, secondary, ghost; hover, focus, pressed, disabled, loading |
| W4 | Forms: text field, select, checkbox, radio, toggle | empty, filled, focus, error, disabled |
| W5 | Cards and content blocks | default, hover, featured |
| W6 | Lists and tables | header, row hover, empty, mobile layout |
| W7 | Feedback: alerts, toasts, empty states, loading, skeletons | each status |
| W8 | Overlays: modal, drawer, tooltip, popover | open, focus trapped |
| W9 | Footer | full and compact |
| W10 | Tags, badges, avatars, breadcrumbs, pagination, tabs | default, active |
| W11 | Breakpoints and responsive behaviour | phone, tablet, desktop |

### Social module

| ID | Template | Notes |
|---|---|---|
| S1 | Cover (carousel and single post) | the only slide seen in the feed |
| S2 | Content slide (step, point, quote) | |
| S3 | Data slide | links to round 6 |
| S4 | Comparison slide (before and after, do and don't) | |
| S5 | Checklist or list slide | |
| S6 | End slide with one ask | |
| S7 | Author block, footer and progress | |
| S8 | Profile banner and photo treatment | respect the platform's photo overlap |
| S9 | Video and motion post frame | links to round 4 |

Use each platform's current sizes (for LinkedIn carousels, PDF pages at 1080 x 1350).

### Slides, app and print modules

- **Slides:** title, section, content, data, quote, end; speaker-safe areas.
- **App:** tab bar, top bar, list rows, sheets, inputs, empty and error states, platform conventions to keep or break.
- **Print:** formats, bleed and safe areas, CMYK proofing notes for high-chroma colours.

## 4. Round 4: Motion

Each direction runs live (CSS or SVG animation in the preview, or a frame strip when live preview isn't possible). "Still" is one of the ten, never the default.

| ID | Decision | Tokens |
|---|---|---|
| M1 | Motion character and what motion means in the system (state change, story, delight) | recorded in DESIGN.md |
| M2 | Durations | `duration.*` |
| M3 | Easing curves, including springs if used | `easing.*` |
| M4 | Web: micro-interactions (hover, press, focus), page and view transitions, scroll-driven reveals | recorded in DESIGN.md |
| M5 | Social: animated carousels or video carousels, kinetic type, animated charts, loop length, export format (MP4, GIF, Lottie) | recorded in DESIGN.md |
| M6 | Signature motion: one movement people recognise the brand by | recorded in DESIGN.md |
| M7 | What never moves | recorded in DESIGN.md |
| M8 | Reduced-motion behaviour | recorded in DESIGN.md |

## 5. Round 5: Imagery and voice

Each direction is shown in place on the round 3 components.

| ID | Decision |
|---|---|
| I1 | Photography: subject, light, framing, treatment |
| I2 | Illustration, 3D or generative imagery, if any, and its rules |
| I3 | Iconography: set, weight, size, licence |
| I4 | Graphic devices: patterns, shapes, motifs from the subject's story |
| I5 | Voice: personality, vocabulary, words to use and avoid |
| I6 | Copy patterns: headlines, buttons, errors, empty states, hooks, calls to action |

## 6. Round 6: Data and infographics

Each direction is a set of charts and stats using the user's real numbers.

| ID | Decision |
|---|---|
| G1 | Chart palette and how the key value is marked (never by colour alone) |
| G2 | Chart types in the kit (bar, line, dot grid, step, table, diagram) and the ones ruled out |
| G3 | Labelling: direct labels or legends, number formatting |
| G4 | Stat treatment: size, weight, colour, units |
| G5 | Diagrams and flows: shapes, connectors, annotation style |
| G6 | Motion for data, if any: how charts build or update |

## 7. Derived details (the review batch)

After the rounds, derive and show together, for review rather than one by one: exact ramp steps, every component state, durations and easings per interaction, breakpoints, spacing per component, focus styles, export settings per medium. Log each with source "derived from" the round decision it follows from.

## 8. Extra layers from inspirations

Add one row per layer the user accepted from an inspiration (for example a texture, grid or illustration language). Give it its own round of ten directions when it changes the look, or settle it in the derived batch when it's small, and record its source inspiration.
