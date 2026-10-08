# Compilation and visual QA

## Compile

1. Copy the master and the `fonts/` folder beside the task `.tex`.
2. Compile with XeLaTeX twice (the script does both): `bash scripts/compile_verify.sh /absolute/path/file.tex`.
3. Confirm the PDF exists and is A4, then render every page to PNG and look at each one.

## Inspect every page

Reject the output if any of these remain:

- overfull boxes, clipped text, missing glyphs ("Missing character" in the log), accidental blank pages;
- a section heading orphaned at the bottom of a page;
- a section number, cobalt dot and heading not on one baseline at one size;
- a tag, label or chip label sitting above or below the first line of its row;
- slot-table columns misaligned, header cells on different baselines, or the changed cell not matching the legend;
- tables stacked back to back with no explanatory prose between them, or heavy full-width rules;
- footnotes colliding with the footer, duplicated footnote numbers, or core content hidden in a footnote;
- footer label, page number or signature collisions, or a running header reappearing;
- cobalt used outside its approved roles, or unembedded fonts.

Harmless underfull warnings are acceptable only after visual inspection.

## Known pitfalls

- A bare `\color` at the start of a table cell or paragraph box shifts the baseline of that cell. Start such macros with `\leavevmode`.
- `\footnote` does not work inside tables or boxes; use `\footnotemark[n]` and `\footnotetext[n]`.
- Column type letters can clash with existing ones (`W` is already defined); the template uses `Y`, `L`, `Z`.
- Fraunces has no bold face; do not apply bold to it.

## Deliver

Report: XeLaTeX success; page count and A4; that every page was inspected; any intentional warning or content gap; links to the PDF and the `.tex` source (with `fonts/`).

## Review-only compiler warnings

On some XeTeX installations, microtype reports unknown slots for unused inherited accented characters, and Computer Modern reports math size substitutions. The bundled script intentionally returns status 3 for warnings so they receive review. A reviewer may accept only these warnings after confirming every page visually, all PDF fonts embedded, and no missing glyphs or overfull boxes. Status 3 is not automatic QA success; other warnings must be investigated.
