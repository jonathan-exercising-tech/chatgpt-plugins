---
name: create-latex-theory-handouts
description: Create, rebuild, or edit editorial XeLaTeX theory handouts, grammar notes, reference sheets, and lesson summaries from user-supplied researched content. Use when Codex needs to turn Markdown, textbook theory, or teacher-authored notes into a theory-first A4 PDF and editable .tex source with the approved Fraunces, Be Vietnam Pro and IBM Plex Mono typography, cobalt palette, label rows, example chips, slot tables, footnotes, and signature profiles. Not for exercise-first worksheets or tests; use create-latex-worksheets for those.
---

# Create LaTeX Theory Handouts (v3, editorial)

Turn supplied, researched teaching content into a designed, theory-first handout that reads like a reference sheet rather than plain text. Treat the user's content as authoritative; improve hierarchy and layout, do not expand the lesson.

## Read the required resources

Before creating or editing a handout:

1. Read [references/design-system.md](references/design-system.md) completely.
2. Read [references/content-layout.md](references/content-layout.md) completely.
3. Read [references/qa.md](references/qa.md) completely before compiling or delivering.
4. Copy [assets/theory-handout-master.tex](assets/theory-handout-master.tex) and the bundled `assets/fonts/` directory as the starting point. Keep `fonts/` beside the task `.tex`. Do not recreate the preamble from memory.

## Follow the workflow

1. Inspect only the supplied source and directly relevant attachments.
2. Preserve the user's wording, terminology, language, examples and section order unless restructuring is requested.
3. Do not research, invent or silently add theory, examples, or lead-in sentences. Flag a genuine content gap only when it prevents coherent layout.
4. Resolve only choices that materially change the artifact: title, student fields, signature profile, language, whether ancillary material becomes footnotes. Infer a signature only from explicit context; otherwise use `none`.
5. Copy the master, replace its demonstration content, keep the approved typography, margins, palette, footer, section rhythm and footnote styling.
6. Map the source into the smallest useful set of sections, one conceptual task per section.
7. Alternate prose and structure: explanation, then table or example, then prose. Never stack full-width tables.
8. Compile with XeLaTeX, run the bundled QA script, render every page and inspect it.
9. Deliver the final PDF and the editable `.tex` with its `fonts/` folder. Include only requested supporting files.

## Choose components deliberately

- Title block: mono eyebrow, Fraunces title, muted subtitle; NAME/CLASS fields only for student handouts.
- `\LabelRow` / `\LabelLine` with `\LabelRule`: distinct uses, meanings, cases or short rules; mono label left, content right.
- `\ExampleChip{LABEL}{sentence}`: examples under the statement they illustrate; `\Target{}` for the target form, `\Context{}` for muted lead-in.
- `\FormulaBand`: one concise core formula as a solid cobalt block; join parts with `\Plus`.
- Paradigm table: booktabs, evenly distributed, centered, changing column shaded Tint.
- Slot table with `\Changed{}`, `\Empty` and `\LegendChip`: only when the source teaches a sentence structure.
- `\ContrastCard`: two forms that may describe the same event.
- Footnotes inside tables or boxes: `\footnotemark[n]` plus `\footnotetext[n]{...}`.

## Configure an optional signature

Default to no signature. Read [references/signatures.md](references/signatures.md) only when the user explicitly supplies a signature. Never infer contact details or restore legacy personal profiles.

## Compile and verify

Run:

```bash
bash scripts/compile_verify.sh /absolute/path/to/handout.tex
```

The script compiles twice, checks A4, renders every page and greps the log for overfull boxes and missing characters. Fix observed defects rather than compressing type or removing content to reduce page count.
