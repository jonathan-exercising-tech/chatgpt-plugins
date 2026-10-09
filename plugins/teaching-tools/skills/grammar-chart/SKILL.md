---
name: grammar-chart
description: Analyze textbook images or normalized Markdown and render consistent EF-series English grammar charts, pretests, drills, exercises, listening worksheets, and answer-key visuals in the established Nous/Hermes cobalt-and-cream style. Use when Codex is asked to render, recreate, modernize, rename, organize, or pack English grammar lesson images; convert textbook chart/exercise content into classroom-ready raster visuals; preserve textbook chart names while standardizing filenames; or prepare matching Markdown only for drills/exercises.
---

# Grammar Chart

Produce accurate, projector-readable English grammar visuals with a stable visual DNA and file system.

## Required companion skill

Read and follow the installed `imagegen` skill completely before generating or editing any raster image. Use its built-in image-generation path by default.

## Workflow

1. Identify the asset type: `chart`, `pretest`, `drill/exercise`, `listening`, or `answer key`.
2. Read [content-analysis.md](references/content-analysis.md). Extract exact content from the source before designing.
3. Read [visual-dna.md](references/visual-dna.md) for every render.
4. Read the matching section in [layouts.md](references/layouts.md).
5. Inspect at least one bundled style authority from `assets/` with `view_image`. If the current project already contains a later approved render, prefer that as the primary style authority.
6. Create a structured `scientific-educational` image-generation prompt. Label each input image as either content source, style reference, or edit target.
7. Render one asset per image-generation call. Default to 1536 × 1024 landscape unless the source or user requires another format.
8. Inspect the generated image at high detail. Apply [qa-and-packaging.md](references/qa-and-packaging.md). Make targeted single-change edits when needed.
9. Save non-destructively under the standardized name. Never alter the chart/exercise number shown inside the image merely to match the filename.
10. Return a direct link to the final file and briefly report its dimensions and coverage.

## Content policy

- Treat supplied textbook images or normalized Markdown as the content authority.
- Preserve grammar, numbering, directions, blanks, choices, punctuation, and instructional intent.
- Do not show or infer an answer key unless the user supplies or explicitly requests it.
- When the user says to skip a key, omit it from both the image and Markdown.
- Charts produce images only unless Markdown is explicitly requested.
- Drills/exercises produce Markdown only when the user requests it or when packing the lesson.
- Listening exercises may reference an audio file, Drive ID, or form upload; do not embed fabricated audio controls in a static worksheet.
- Improve hierarchy and illustration, not the underlying task difficulty.

## Prompt construction

Build prompts in this order:

1. Use case and output purpose.
2. Exact title, badge, directions, sentences, formulas, labels, and notes.
3. Semantic layout: timelines, comparisons, forms, question flow, or exercise sequence.
4. Visual DNA and grid constraints.
5. Grammar invariants and text that must be verbatim.
6. Avoid list: pseudo-text, answer leakage, wrong tense, tiny type, malformed timelines, logos, watermarks, and textbook page artifacts.

For text-heavy images, quote every required string and explicitly require verbatim spelling, punctuation, contractions, and numbering.

## Continuity rules

- Use the most recently approved project render as the strongest style reference.
- Keep cobalt header, warm cream cards, periwinkle borders, orange/gold semantic accents, watercolor line art, and orbital motifs consistent across a pack.
- Vary illustrations to match the lesson, but keep stroke weight, saturation, character treatment, and card geometry stable.
- Use blue for an action/state connected to the reference time or NOW; use orange for a completed event, contrast, warning, or key grammar signal.

## Resources

- [content-analysis.md](references/content-analysis.md): transcription, normalization, and instructional analysis.
- [visual-dna.md](references/visual-dna.md): palette, typography, canvas, spacing, alignment, illustration, and density.
- [layouts.md](references/layouts.md): templates for charts, exercises, pretests, listening, and answer keys.
- [qa-and-packaging.md](references/qa-and-packaging.md): inspection gates, naming, Markdown, and pack structure.
- `scripts/inspect_render.py`: deterministic dimensions, naming, margins, and coarse palette checks.
- `assets/style-chart.png`, `assets/style-exercise.png`, and `assets/style-listening.png`: approved style authorities.
