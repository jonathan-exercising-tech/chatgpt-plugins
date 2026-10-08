# Content and layout rules

## Preserve source authority

Treat the user's researched content as complete unless asked to review or expand it. Reorganize for readability without inventing theory, citations, exceptions, examples, or connecting sentences. If a section would read better with a lead-in sentence the source lacks, leave it out and mention it in the delivery note.

Footnotes carry only information already in the source or supplied by the user. Preserve supplied citations exactly.

## Reading flow

- Alternate explanation and structure: a short prose or label-row explanation, then a table or example, then prose again.
- Use label rows (`\LabelRow`, `\LabelLine`) for distinct uses, meanings, cases or rules: mono label at the left, content at the right. Hairline `\LabelRule` between rows.
- Put each example in an example chip (`\ExampleChip`) directly under the statement it illustrates. Chip labels: EXAMPLE, EVIDENCE, FOCUS and similar. Target form in `\Target{...}`, lead-in context in `\Context{...}`.
- Let page count grow rather than shrinking type.

## Core formula and paradigm

- One solid cobalt formula block (`\FormulaBand`) for the shortest reusable formula, white Fraunces type, parts joined by `\Plus`.
- Supporting paradigm data goes in a full-width booktabs table with evenly distributed centered columns. Shade only the column that changes.

## Slot table (grammar structure)

Use only for a structure the source explicitly teaches.

- One column per grammatical function and one row per form. The same function always sits in the same column.
- Columns for elements that move (for example an auxiliary that moves in questions) are repeated with a short sub-label such as "question only" and "statement".
- Cells that change relative to the affirmative sentence use `\Changed{...}` (solid cobalt, white text). Empty slots use `\Empty`.
- Always add `\LegendChip` explaining solid cells.
- Sentence text 12.5/16 pt, headers 7.5 pt mono. Column weights use the `Z{weight}` column type; weights sum to the number of Z columns.
- If a structure cannot fit, shorten labels or group linguistically valid adjacent words; never overlap cells.

## Comparisons and notes

- Two forms that may describe the same event: two side-by-side contrast cards (`\ContrastCard`).
- Short rules and notes: `\LabelLine` rows below the table they explain.
- Long qualifications or side information: footnotes. Inside tables or boxes use `\footnotemark[n]` in the cell and `\footnotetext[n]{...}` after the block, numbered manually in reading order.
- Do not repeat an overview verbatim in a later comparison.
