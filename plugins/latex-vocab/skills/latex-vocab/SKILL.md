---
name: latex-vocab
description: Create, rebuild, or edit LaTeX vocabulary handouts that must match the approved YLC8 vocabulary visual DNA. Use when the user mentions YLC8 vocab, vocab-ylc8, YLC8-VOCAB, latex-vocab, asks for a vocabulary/glossary handout in the same style, or wants a lesson vocabulary table derived from this master. This skill is specialized for vocabulary handouts; use a general LaTeX workflow for ordinary portrait documents, papers, reports, books, or Beamer slides.
---

# LaTeX Vocab

Reproduce the approved YLC8 vocabulary handout faithfully (version 0.2: Be Vietnam Pro / Fraunces / Gentium Plus / IBM Plex Mono font set, replacing the earlier Latin Modern + Noto Serif set). Treat the bundled master as the YLC8 presentation reference; do not redesign it from memory.

## Authority and scope

Canonical/user-approved content controls wording and vocabulary–IPA relationships. Current user instructions and the project's Production Protocol govern execution. Explicit user constraints, approved project templates, and project-specific visual rules take precedence over this skill's presentation defaults, including the bundled master and style specification. Preserve the YLC8 rules below unless that higher presentation authority specifies otherwise; never silently override an approved standard.

This skill supplies specialist production guidance and mandatory QA. The project's Production Protocol orchestrates production; its Definition of Done determines completion.

## Required references

Before creating or editing a YLC8-style vocabulary handout, read [references/style-spec.md](references/style-spec.md) completely.

Use [assets/YLC8-VOCAB-MASTER.tex](assets/YLC8-VOCAB-MASTER.tex) as the structural master. Copy it, together with `assets/fonts/`, into the task project and edit the copy. Never modify the bundled asset in place.

If the source has no IPA at all (for example a teacher list with only Vietnamese meanings), use [assets/VOCAB-MASTER-noipa.tex](assets/VOCAB-MASTER-noipa.tex) instead. It is the same master with the IPA column removed (columns `C{9mm} L{42mm} L{30mm} L{62mm} L{96mm}`, macro `\Vocab{word}{POS}{meaning}{example}`). Never invent IPA to fill the column; offer to add it afterwards for the teacher to check.

## Workflow

1. Extract only the content required by the user. Preserve wording, IPA, POS, meanings, examples, section order, and requested metadata unless correction is explicitly requested.
2. Structure vocabulary rows as `Word | IPA | POS | Meaning | Example` and group them under section headings when sections exist.
3. Copy the bundled master and `fonts/` to the output project. Generate a sibling `vocab-sections.tex` containing only `\VocabSection`, `\VocabTableStart`, `\Vocab`, and `\VocabTableEnd` calls.
4. Replace document-specific metadata such as class/unit/title/signature (`\fancyhead[L]`, `\fancyhead[R]`, title and compiled-by line; no personal signature is set by default; add only metadata explicitly provided by the user) in the copied master only when the task calls for different metadata. Do not change typography, margins, table geometry, colors, or spacing without explicit user approval.
5. Escape LaTeX-special characters in content while preserving intended emphasis. Keep IPA inside the `\Vocab` IPA field; do not wrap IPA in manual baseline adjustments.
6. Compile with XeLaTeX. Run once, and run a second time only when page numbering/references or a first-pass layout condition requires it.
7. Render and inspect the PDF for overflow, clipping, missing glyphs, table-header repetition, header/footer collision, and the mandatory specialist QA below. Use moderate resolution initially and closer views where glyphs or alignment require them. Re-render changed output and rerun affected checks; compilation or source inspection alone cannot satisfy visual QA. Do not perform repeated cosmetic optimization after the approved DNA renders correctly.

## Content syntax

Use this pattern in `vocab-sections.tex` (argument order: word, IPA, POS, meaning, example; the no-IPA master takes four arguments, without IPA). When the source has no section headings, omit `\VocabSection` and use a single table:

```tex
\VocabSection{City Landmarks \& Tourism}
\VocabTableStart
\Vocab{complex}{/ˈkɒmpleks/}{noun}{khu liên hợp}{The new sports complex has a large swimming pool.}
\Vocab{subway station}{/ˈsʌbweɪ ˌsteɪʃn/}{noun phrase}{ga tàu điện ngầm}{I will meet you at the subway station at 7 PM.}
\VocabTableEnd
```

Reset `vocabno` only when the user explicitly wants numbering to restart. By default, numbering continues across sections as in the master.

## Font integrity

Fonts live in `assets/fonts/` and are loaded with `Path=fonts/`. Copy the whole `fonts/` folder next to the `.tex` file (the master will not compile without it).

- Be Vietnam Pro (regular, semibold, real italic, real semibold italic): table body, vocabulary words (semibold), POS and examples (italic), running header metadata, compiled-by line.
- Fraunces (`fraunces-display.ttf` for the title, `fraunces-heading.ttf` for section headings): title and section headings only. The static instances have no bold face, so never apply `\bfseries` to them.
- Gentium Plus: IPA only (`\ipafont`).
- IBM Plex Mono (Vietnamese build): row numbers and page number only (`\NumFont`).
- Never substitute with Arial, Calibri, Helvetica, DejaVu Sans, Latin Modern or Noto Serif. Never use fake slant for italics; the real italic files are bundled.
- If a font file is missing, report it before changing the font system. Do not silently choose a fallback and call it faithful.
- Inside table cells never start a cell with a bare `\color{...}`; it shifts the baseline of that cell (the old IPA drift bug). Use `\textcolor{...}{...}` as the master does.
- All fonts are SIL OFL; licences are bundled in `assets/fonts/`.

## Orientation rule

Vocabulary handouts using this DNA are A4 landscape by default because the six-column table needs width. This rule does not imply that ordinary documents should be landscape; leave general portrait documents to the general LaTeX workflow.

## Guardrails

- Do not add illustrations, icons, badges, gradients, shadows, thick frames, decorative graphics, or vertical table rules.
- Do not invent extra vocabulary, definitions, synonyms, CEFR labels, grammar notes, or exercises.
- Strip decorative source quotation marks around examples only if told so or if the source quotes are clearly a Markdown artefact; say so in the report. Do not rewrite the preamble or swap packages when the bundled master already compiles.
- Do not change font sizes or line spacing to make content fit until genuine overflow is confirmed. Prefer natural longtable pagination.
- Keep examples italic and vocabulary headwords bold exactly as defined by the master.

## Mandatory specialist QA

Collect these checks into the task's acceptance checklist. Compare against the authoritative content and approved template, and record each result with the candidate revision and actual entry/page coverage in the production trace. Inspect every vocabulary–IPA pair; for a short handout, visually inspect every rendered page. These checks supplement the PDF checks in workflow step 7.

### QA-LV-01 — Vocabulary–IPA Pairing

- **Inspect:** Compare every rendered vocabulary entry and its IPA against the authoritative source, preserving the association through row/order changes. Do not validate only against generated LaTeX.
- **Failure:** Wrong word–IPA pairing, including row/order changes that break association.
- **Severity:** MAJOR.
- **Rerun after:** Relevant content, row-order, table-structure, or pagination changes.

### QA-LV-02 — IPA Alignment

- **Inspect:** This known recurring regression requires special attention in the **rendered PDF**, not only LaTeX source or compilation status. Verify that IPA stays visually associated and correctly aligned with its vocabulary entry according to the approved template.
- **Stress cases:** Long vocabulary items, IPA diacritics, glyphs with different vertical extents, wrapped definitions, and rows near page boundaries. Exercise these in a representative fixture when absent from the artifact; never add invented stress content to canonical content. Record fixture coverage separately from final-candidate coverage.
- **Failure:** IPA visibly drifts into another row, becomes detached from its vocabulary item, or alignment creates reading ambiguity.
- **Severity:** MAJOR when association/readability is impaired; MINOR for harmless optical baseline variation. A harmless optical variation may be recorded as a MINOR finding with PASS when the required association and approved-template alignment remain satisfied.
- **Rerun after:** Fonts, table macros, row spacing, column widths, page geometry, or shared layout rules change; also after content or pagination changes affecting these stress cases. Inspect repaired rows and other affected rows/pages as a rendered-output regression check.

### QA-LV-03 — IPA Glyph Integrity

- **Inspect:** Compare rendered IPA characters with the authoritative transcriptions at sufficient magnification to inspect diacritics; font/build diagnostics supplement visual inspection.
- **Failure:** Missing glyphs, replacement characters, malformed diacritics, or font fallback that materially damages readability.
- **Severity:** MAJOR.
- **Rerun after:** IPA content, fonts/fallbacks, encoding, font packages, or rendering-engine changes.

### QA-LV-04 — Wrapping Integrity

- **Inspect:** Read wrapped vocabulary, IPA, and definition cells together in the rendered PDF, including long entries and wrapped definitions.
- **Failure:** Wrapping detaches vocabulary, IPA, and definition in a way that creates ambiguity.
- **Severity:** MAJOR when association becomes unclear.
- **Rerun after:** Content, fonts, column widths, table macros, row spacing, or pagination changes affecting wrapping.

### QA-LV-05 — Page Boundary Integrity

- **Inspect:** Examine entries immediately before and after each rendered page boundary, including continued tables, against the source for completeness.
- **Failure:** Clipped rows, orphaned IPA, broken word–IPA association, unintended overlap, or incomplete entries.
- **Severity:** MAJOR.
- **Rerun after:** Content/order, table structure/macros, fonts, row spacing, column widths, page geometry, or pagination changes.

## Completion report

Include the master used (with or without IPA), any column dropped and why, quote handling, page count, whether all requested rows are present, whether severe overflow/missing glyphs remain, and the final `.tex`/`.pdf` paths. Include the status, QA evidence/coverage, and unresolved findings required by the project's Production Protocol and Definition of Done.
