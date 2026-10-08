---
name: create-latex-worksheets
description: Create, rebuild, or edit editorial XeLaTeX A4 worksheets, exercises, tests, and answer keys from supplied teaching material using the bundled v3 Fraunces, Be Vietnam Pro, IBM Plex Mono, and cobalt template. Use for exercise-first classroom PDFs and editable sources; use create-latex-theory-handouts for theory-first notes.
---

# Create LaTeX Worksheets — v3

1. Read the supplied questions, instructions, and answer key. Preserve wording, numbering, question types, and question–answer relationships. Do not invent replacement content unless asked.
2. Copy [assets/worksheet-master.tex](assets/worksheet-master.tex) and `assets/fonts/` into a working folder, with `fonts/` beside the document. The 36-question present-perfect worksheet is demonstration content: replace it with the user's material, keeping the approved preamble and components.
3. Preserve A4 geometry, Fraunces headings, Be Vietnam Pro body, IBM Plex Mono metadata, cobalt palette, student fields, answer space, section rhythm, and footer. Use the master's question and answer macros. Keep the answer key separate from student questions.
4. Default to no signature. For explicitly supplied identity text, follow [references/signatures.md](references/signatures.md). Never infer contact information.
5. Compile twice using `bash scripts/compile_verify.sh /absolute/path/worksheet.tex`. Dependencies: XeLaTeX with the template packages, Latin Modern Math, and Poppler (`pdfinfo`, `pdftoppm`, `pdffonts`). The bundled fonts must stay beside the source.
6. Read [references/qa.md](references/qa.md), render and inspect every page, and repair observed defects. Verify all questions map to the correct answers, numbering remains continuous, and writing space fits the response expected.
7. Deliver the verified PDF and editable source with fonts. Exclude private signature configuration from public source bundles. Report page count, checks actually performed, and unresolved limitations.

Use an available native LaTeX editor for supported standalone documents. This bundled multi-file font project requires a compatible XeLaTeX environment; do not claim successful compilation when the environment is unavailable.
