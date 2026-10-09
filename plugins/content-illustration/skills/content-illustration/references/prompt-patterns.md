# Prompt Patterns and Style Anchors

Use these patterns as decision guidance, not mandatory wording. Quote any required in-image text exactly.

## Select reference assets

- Human portrait or figure: `assets/style-references/human-einstein-master.png`
- Animal, plant, or annotated natural history: `assets/style-references/animal-thylacine-master.png`
- Construction or process sequence: `assets/style-references/construction-stone-arch-master.png`
- Pure engraving discipline or dense technical diagrams: `assets/style-references/engraving-technical-reference.jpg`
- Botanical palette and isolated specimen composition: `assets/style-references/botanical-color-reference.jpeg`

Use one primary anchor and at most one supporting anchor unless a genuine multi-mode comparison requires more. Label each image's role and state what must not be copied.

## Shared prompt core

```text
Use case: scientific-educational
Asset type: educational illustration
Primary request: <subject and teaching purpose>
Input images: <style role for each selected anchor; not subjects to copy>
Style/medium: historical scientific-book illustration; smooth black engraved contours; deliberate parallel hatching; sparse cross-hatching; clean warm-white paper
Composition: <single study, annotated plate, comparison, or ordered sequence>
Color mode: <transparent watercolor beneath visible black ink | pure black ink only>
Text (verbatim): <exact short lines, or none>
Constraints: authored illustration; readable teaching action; accurate anatomy or geometry; generous negative space
Avoid: photorealism; photo tracing; skin gradients; fuzzy graphite; global paper texture; sepia wash; glossy digital rendering; pseudo-text; watermark
```

## Human prompt additions

Require historical illustrated-book realism, economical facial construction, grouped engraved hair, selected clothing folds, plausible simplified hands, and volume created by line density. State that recognizability must come from drawn structure rather than photographic rendering.

## Natural-history prompt additions

Name the diagnostic anatomy that must be visible. Allow one large colored study and one or two smaller monochrome details. Keep habitat sparse. For extinct species, distinguish documented features from speculation.

## Construction prompt additions

List each stage explicitly. Require the same structure and viewpoint across panels, temporary supports in the correct stages, plausible joints or load paths, and arrows only where they explain the process. Avoid modern machinery unless requested.

## Handwritten-note prompt additions

Provide 3–7 short exact strings. Specify placement, leader-line target, handwriting ink color, and prohibition on added words. After generation, read every line visually; retry if any spelling or Vietnamese diacritic is wrong.

