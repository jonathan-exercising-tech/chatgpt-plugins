# QA and Packaging

## Visual QA gates

Inspect the final image at high detail and reject it if any gate fails:

1. Every required item is present exactly once.
2. No answer is leaked into an intended blank or choice.
3. Grammar, spelling, punctuation, apostrophes, numbering, and chart references match the source.
4. Formula order and auxiliary agreement are correct.
5. Timelines express the intended temporal logic.
6. No pseudo-text, malformed word, duplicate line, watermark, logo, or textbook page artifact appears.
7. Meaningful text remains readable at full-slide view.
8. Parallel cards align and use consistent padding.
9. Illustrations clarify context and do not compete with instructions.
10. The asset matches the approved pack’s palette and header geometry.

Run `scripts/inspect_render.py IMAGE --kind chart|exercise|pretest|listening` after visual inspection. Treat script output as a coarse technical check, not a substitute for reading the image.

## Targeted correction

When one defect exists, edit only that defect and repeat all invariants: preserve composition, palette, illustrations, text outside the target, dimensions, and numbering. Generate a fresh variant only when the layout itself is unusable.

## File naming

Use uppercase stable names with hyphens inside identifiers:

- Chapter chart: `CH02_CHART-2-7.png`
- Chapter pretest: `CH02_PRETEST.png`
- Session chart: `EF-S04_CHART-1-5.png`
- Drill: `EF-S04_DRILL-29A.png`
- Legacy exercise folder when already established: `EF-S03_EX-18.png`
- Answer key: `EF-S03_KEY_EX-17_EX-18.png`
- Drill Markdown: same basename with `.md` when practical.

Never rename the chart/exercise title printed inside the image. Filename normalization is external only.

## Directory structure

For chapter-only work:

```text
CH02/
├── 00_PRETEST/
├── 01_CHARTS/
├── 02_DRILLS/
└── 03_ANSWER_KEYS/
```

For a session pack:

```text
EF-S04/
├── 00_PRETEST/
├── 01_CHARTS/
├── 02_DRILLS/
├── 03_ANSWER_KEYS/
├── 04_AUDIO/
└── manifest.md
```

Create only folders that contain deliverables. Preserve user files and unrelated work.

## Markdown policy

- Do not create Markdown for charts unless explicitly requested.
- Create normalized Markdown for drills/exercises when packing or requested.
- Include title, chart scope, directions, questions, choices/blanks, and optional audio metadata.
- Keep answers in a separate `03_ANSWER_KEYS` document; omit the entire answer section when the key was skipped.
- Markdown must remain suitable for later Google Forms/Apps Script generation: stable numbering, one question per block, explicit choices, and machine-readable answer metadata only when a key exists.

## Pack manifest

When the user says `pack`, create `manifest.md` listing session/topic, included charts, drills, Markdown files, keys, audio, and omissions. Then create a ZIP named exactly after the requested pack, such as `EF-S04.zip`. Do not pack source scans unless requested.

