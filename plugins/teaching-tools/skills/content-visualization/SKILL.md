---
name: content-visualization
description: Create, rebuild, or edit slide-like interactive visual lessons, infographic decks, chart explainers, classroom vocabulary games, and standalone HTML presentations. Use when Codex needs to turn lesson content, Markdown, data, diagrams, or generated illustrations into a self-contained interactive HTML file with a centered 16:9 stage, clickable section navigation, back/next and keyboard controls, embedded compressed raster assets, responsive layout, and optional portable-folder output. Do not use when the required final deliverable is specifically PPTX, Google Slides, a static raster chart, or a conventional website.
---

# Content Visualization

Build a presentation that behaves like slides while retaining HTML's flexibility.

## Read first

- Read [references/design-system.md](references/design-system.md) for layout, palette, typography, and image-fit rules.
- Read [references/pedagogy-and-contrast.md](references/pedagogy-and-contrast.md) for grammar lessons, comparison-first sequencing, two-picture semantic pairs, and staged rule discovery.
- Read [references/output-modes.md](references/output-modes.md) before choosing standalone versus portable-folder output.
- Read [references/template-schema.md](references/template-schema.md) when filling the bundled HTML template.
- Read [references/qa.md](references/qa.md) before final delivery.
- For lessons, start from [assets/standalone-template.html](assets/standalone-template.html) unless editing an existing approved file. For games, use the game routing below.

## Core architecture

Keep three layers separate:

1. **Presentation shell:** section navigation, progress, controls, keyboard behavior, fullscreen, and responsive stage.
2. **Editable content:** headings, labels, explanatory text, accessible descriptions, HTML/SVG charts, and interaction states.
3. **Rendered visual assets:** illustrations, maps, textured scenes, and other imagery that would be inefficient or brittle in CSS.

Keep text outside raster images whenever practical. Ask image generation for no words, labels, numbers, logos, or watermarks; overlay the final wording in HTML.

## Workflow

### 1. Analyze the source

- Extract the lesson or narrative structure before designing.
- Define one central idea per screen.
- Group screens into three to seven clickable sections.
- Identify which visuals are exact data/diagram work and which are illustrative.
- Preserve supplied facts and wording unless the user asks for editing.
- For grammar or concept teaching, build a contrast map before choosing a layout: known form, target form, constants, changed element, context trigger, meaning contrast, common confusion, and discovery question.
- Prefer `Context -> Notice -> Compare -> Discover -> Check -> Produce` over explanation-first sequencing.
- Do not reveal the completed rule before learners have seen enough evidence to notice the target difference.

### 2. Select the visual method

- Use semantic HTML/CSS for text, cards, labels, timelines, controls, and simple shapes.
- Use SVG, Canvas, or a chart library only when exact geometry or data interaction materially helps.
- Use image generation or an applicable illustration skill for complex scenes, characters, maps, and editorial artwork.
- Never spend substantial time recreating a complex illustration with CSS merely to keep it "pure HTML."
- Avoid external CDN dependencies in standalone mode.
- When two grammar meanings or forms are contrasted, default to a two-picture semantic pair when imagery can make both meanings memorable.
- Keep the same character, topic, framing logic, and visual style across the pair whenever practical. Change only the semantic cue needed by the contrast.
- Place one learner-readable sentence with each image. Keep the two sentences as close to a minimal pair as grammar allows.
- Keep exact grammar structure, token highlighting, arrows, timelines, and reveal states in HTML/SVG when embedding them in a lesson.

#### Route educational visuals

- **Grammar structure → `grammar-chart`:** grammar charts, pretests, drills/exercises, listening sheets, answer-key visuals, EF-series, Nous/Hermes cobalt-and-cream requests, or precise grammar/timeline/token layouts. Read and follow [Grammar Chart](../grammar-chart/SKILL.md), including its image-generation and QA workflow. Preserve its own cobalt-and-cream visual DNA; do not recolor it to the lesson shell. Keep exact wording in HTML/SVG when that improves reliability in an HTML lesson.
- **Subject illustration → `content-illustration`:** people, animals, plants, objects, places, natural-history plates, construction sequences, engraving, watercolor-under-ink, monochrome scientific plates, or handwritten annotations. Read and follow [Content Illustration](../content-illustration/SKILL.md). Preserve its engraved scientific-book style; do not request photorealism, modern vectors, logos, or fake raster text. Overlay important wording in HTML.
- Use HTML/CSS/SVG directly for text, controls, scoreboards, simple timelines, and exact geometry. Do not call both image skills by habit. If both seem applicable, choose by the asset's teaching purpose: grammar structure versus subject illustration. A lesson may use both for distinct assets, each with one clear visual authority.

#### Choose the game format

- Follow a specific game concept supplied by the user.
- When the user requests a game, warm-up game, or vocabulary game without a specific format, use **Mysterious Cups** by default. Read [references/game-modes.md](references/game-modes.md) and copy [assets/game-templates/mysterious-cups.html](assets/game-templates/mysterious-cups.html) into the task workspace. Never rebuild the cups or game shell from memory.
- Adapt content, questions, embedded pictures, and round count while preserving both teams opening different cups each round. The game preset's layout and controls take precedence over the generic slide-shell steps below.
- Ask about game changes only when missing information materially changes scoring or rules; do not ask the user to choose a format when this default applies.

### 3. Build the shell

- Copy the selected lesson or game template to the task workspace. The game preset already embeds fonts and has no template tokens.
- Run `python3 scripts/embed_fonts.py OUTPUT.html` after copying the template so the approved Fraunces, IBM Plex Mono, and Be Vietnam Pro system remains available offline. Do this before standalone validation.
- Replace every `{{TOKEN}}`; never deliver unresolved template markers.
- Keep the main content rectangle at 16:9.
- Keep top navigation and bottom controls outside the content rectangle.
- Place Back and Next together beneath the stage, centered.
- Place the flow/orientation icon at bottom left and fullscreen at bottom right.
- Make section tabs clickable and keyboard navigation functional.
- Use a compact, single-row section label such as `03 Pattern`, not a stacked number and label.
- Select a screen archetype from the pedagogy reference before filling the slide. Do not force every teaching screen into the default explanation-left/visual-right layout.
- For comparison screens, use equal visual weight, mirrored card structure, and synchronized grammar-token colors.

### 4. Prepare raster visuals

- Render the illustration at an aspect ratio matching its intended frame.
- Default to 3:2 for the right-hand visual panel in the bundled template.
- Run `scripts/embed_visual.py` to resize, compress to WebP, and either embed or write a portable asset.
- Use quality 82–86 by default and cap the long edge at the actual presentation need, normally 1536 px.
- Confirm the final `<img>` and its container use the same aspect ratio. Do not hide a ratio mismatch with accidental letterboxing.

Example:

```bash
python3 scripts/embed_visual.py illustration.png \
  --html lesson.html \
  --marker '{{VISUAL_DATA_URI}}' \
  --output-html lesson.html \
  --output-webp lesson-visual.webp \
  --max-width 1536 \
  --quality 84
```

For a portable-folder output, add `--portable` and keep the generated WebP beside the HTML.

### 5. Add interactions

- Support click navigation, Left/Right arrow keys, Home/End, and fullscreen.
- Update `aria-current`, visible slide state, current count, and progress together.
- Retain visible focus states and usable labels on icon-only buttons.
- Respect `prefers-reduced-motion`.
- Do not make orientation switching mandatory; keep it as a compact optional control.
- For discovery screens, stage information in this order: unmarked examples, changed-token highlight, learner prompt, then rule reveal.
- Require a learner decision or spoken observation before revealing an answer when the lesson design calls for student-centered discovery.

### 6. Verify and deliver

- Run `scripts/validate_standalone.py OUTPUT.html`.
- Render or open the HTML at desktop and narrow widths when browser tooling is available.
- Inspect image fit, text overflow, section state, controls, and fullscreen.
- Inspect whether the intended difference is visible within three to five seconds, whether comparison sentences preserve a common context, and whether imagery clarifies meaning instead of merely decorating the slide.
- Deliver the final HTML plus a PNG preview. Deliver the compressed WebP separately only when useful to the user.

## Output defaults

- Default to a single standalone HTML file for lessons and decks that remain below roughly 25 MB.
- Switch to portable-folder mode when many high-resolution images would make the HTML cumbersome.
- Keep the approved spotted cream shell, cream paper stage, dark brown ink, wine interaction states, olive structural accents, and restrained antique gold unless the user requests another visual system.
- Use flat editorial design. Avoid glossy 3D, excessive shadows, generic corporate gradients, and ornamental clutter.

## Stop conditions

- Ask before changing verified lesson facts, grading logic, or answer keys.
- Ask when the output mode materially affects distribution and the user's preference is unknown for a projected file above 25 MB.
- Do not silently replace a requested PPTX deliverable with HTML; use the presentation workflow instead.
