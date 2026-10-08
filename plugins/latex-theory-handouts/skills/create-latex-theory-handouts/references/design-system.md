# Approved design system (v3, editorial)

## Page and typography

- Build with XeLaTeX on A4 portrait paper. Margins 17 mm, bottom margin 22 mm.
- Body: Be Vietnam Pro Regular at 10/15 pt (bold = SemiBold, italic = Regular with FakeSlant 0.18).
- Display and headings: Fraunces static instances (`fraunces-display.ttf` for the title, `fraunces-heading.ttf` for headings and subheads). They have no bold face, so never use bold or `\textbf` inside them.
- Labels, tags, table headers and footer: IBM Plex Mono (Vietnamese build). Tags are letter-spaced.
- Title 34/38 pt Fraunces Display. Mono eyebrow above it at 8.5/11 pt in cobalt. Muted subtitle at 11.5/16 pt.
- Section heading: number, cobalt middle dot and heading on one baseline at one size, 14/18 pt Fraunces Heading with letter spacing. Followed by a 13 mm cobalt rule, 1.2 pt thick, then an optional one-line muted description at 9/12 pt. Keep headings with at least eight following baselines using `needspace`.
- Subhead 12/15 pt Fraunces Heading. Row lead lines 11.5/15 pt semibold.
- Footnotes 8/11 pt. Footer label and page number 7.5/10 pt mono (signature 8/10 italic).
- No first-line indent; paragraph spacing 0.42 baselineskip.
- The arrow glyph is absent from Be Vietnam Pro: use `\Arrow` (Latin Modern Math).

## Palette

Cobalt `#0053FD`, Ink `#172033`, Muted `#596276`, Rule `#CBD3E1`, Tint `#F2F6FF`, BadgeFill `#E8F0FF`.
Cobalt appears only on: mono tags, target forms in examples, the section dot and rule, the formula block, changed cells, legend chip.
No gradients, shadows, decorative icons, or extra accent colors. The user prints in black and white: solid cobalt blocks carry white text so they stay readable in grayscale.

## Section rhythm

About one and a half body lines of space before each section, then heading, cobalt rule, optional description, content. Do not use numbered badges.

## Rules and tables

Booktabs style: 0.6 pt Ink outer rules, 0.35 pt header rule, 0.35 pt Rule-colored row rules, no vertical rules. Alternate prose and tables; never stack full-width tables back to back.

## Headers, fields, footer

- No running header. The document label appears only in the footer.
- NAME and CLASS fields only on student handouts.
- Thin footer rule in Rule color, mono document label at left, page number centered, signature at right. This footer is the only running page furniture.

## Offline font portability

Keep `fonts/` beside the working `.tex`. Load every font from that folder (only Latin Modern Math for the arrow is a system font). Confirm with `pdffonts` that the fonts are embedded. Keep the OFL license files in `fonts/`.
