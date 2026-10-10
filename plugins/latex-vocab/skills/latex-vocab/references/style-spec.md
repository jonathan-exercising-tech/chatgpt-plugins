# YLC8 Vocabulary Style Specification

This specification is extracted from the the bundled master `assets/YLC8-VOCAB-MASTER.tex` (version 0.2, new font set). Treat the values in that file as authoritative; this page explains them.

## Page and engine

- Engine: XeLaTeX.
- Document class: `article`, `10pt`, `a4paper`, `landscape`.
- Geometry: `margin=20.5mm`.
- White page background; no decorative page background.
- Running header/footer: `fancyhdr`, no header rule, no footer rule.
- Header height: `14pt`; header separation: `12pt`.
- Paragraph indent: `0pt`.

## Font roles

All fonts are loaded from `fonts/` next to the `.tex` with `Path=fonts/`.

- Body and sans (`\setmainfont`, `\setsansfont`): Be Vietnam Pro: `be-vietnam-pro-regular.ttf`, bold `be-vietnam-pro-semibold.ttf`, italic `BeVietnamPro-Italic.ttf`, bold italic `BeVietnamPro-SemiBoldItalic.ttf` (real italics, no FakeSlant).
- Title: Fraunces display instance `fraunces-display.ttf` (`\DisplayFont`).
- Section headings: Fraunces heading instance `fraunces-heading.ttf` (`\HeadFont`). These static instances have no bold face; do not use `\bfseries` with them.
- IPA: Gentium Plus `GentiumPlus-Regular.ttf` (`\ipafont`).
- Row numbers and page number: IBM Plex Mono Vietnamese build (`\NumFont`).
- Do not use a sans face for the title or section headings.

## Palette

| Token | Hex | Role |
| --- | --- | --- |
| `Ink` | `#1E2933` | Title and section heading |
| `Muted` | `#61707D` | Running metadata, page number, IPA, row number |
| `Rule` | `#B8C2C9` | Reserved rule tone |
| `Header` | `#EDF2F3` | Vocabulary table header fill |

## Running header and footer

- Header left: Be Vietnam Pro, `9/13 pt`, `Muted`, document/unit label.
- Header right: Be Vietnam Pro, `9/13 pt`, `Muted`, signature/handle.
- Footer center: IBM Plex Mono `9/13 pt`, `Muted`, page number.
- No visible header/footer rules.

## Document title block

- Alignment: centered.
- Title: Fraunces display, `26/30 pt`, `Ink`.
- Gap after title: `0.35em`.
- Compiled-by line: Be Vietnam Pro, `9.5/13 pt`, `Muted`.
- Gap after the title block before content: `0.8em`.

The centered document title is intentional. Section headings below it are left-aligned.

## Section heading

- Left aligned.
- Fraunces heading, `15/18 pt`, `Ink`.
- Require about `10\baselineskip` of remaining space before starting a new section to avoid stranded headings.
- Space before heading: `1.05em`.
- Space after heading: `0.5em`.

## Vocabulary table

- Package/layout: `longtable` + `booktabs`; no vertical rules.
- Base table font: `9.5/13 pt`, hyphenation off inside the table.
- `\tabcolsep = 4pt`.
- `\arraystretch = 1.22`.
- `\extrarowheight = 0.8pt`.
- Column definitions:
  - No.: centered `m{9mm}`.
  - Word: ragged-right `p{33mm}`.
  - IPA: ragged-right `p{40mm}`.
  - POS: ragged-right `p{27mm}`.
  - Meaning: ragged-right `p{50mm}`.
  - Example: ragged-right `p{76mm}`.
- Header row: bold Be Vietnam Pro labels on `Header` (`#EDF2F3`) fill.
- Horizontal structure: `\toprule`, `\midrule`, `\bottomrule` only.
- Repeat the header on subsequent longtable pages.

### Cell typography

- Row number: IBM Plex Mono `8.5/12.5 pt`, `Muted`.
- Word: semibold Be Vietnam Pro.
- IPA: Gentium Plus `10.5/12.5 pt`, `Muted`, written with `\textcolor{Muted}{...}` (never a bare `\color` at the start of a cell; it moves the baseline).
- POS: italic Be Vietnam Pro.
- Meaning: regular Be Vietnam Pro.
- Example: italic Be Vietnam Pro, `9/12.5 pt`.

### No-IPA variant

When the source has no IPA, drop the IPA column: `C{9mm} L{42mm} L{30mm} L{62mm} L{96mm}` (No., Word, POS, Meaning, Example). Everything else is unchanged.

The approved master does not use `\raisebox`, `\strut` tricks, or manual vertical offsets for IPA. Preserve the native table baseline.

## Visual character to preserve

- Academic/editorial rather than decorative.
- Strong serif hierarchy, restrained muted metadata, generous white space.
- Dense but readable wide table; examples get the largest column.
- Section headings provide hierarchy without boxes or ornaments.
- No vertical rules, icons, badges, illustrations, gradients, shadows, or childlike styling.

## Fidelity decisions

Explicit user constraints and approved project presentation standards take precedence over this bundled specification, as stated in `SKILL.md`.

If content is longer than the sample, allow `longtable` to paginate naturally before changing type sizes or column widths. Without a higher-priority presentation instruction, actual overflow/clipping is grounds to propose a minimal, local source-value adjustment; obtain the explicit user approval required by `SKILL.md` before changing the approved typography, margins, table geometry, colors, or spacing. Overflow alone does not authorize overriding the approved template.
