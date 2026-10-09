# Content Analysis

## 1. Establish authority

Use this order:

1. User corrections in the current request.
2. Supplied answer key for correctness only.
3. Normalized Markdown.
4. Textbook image.
5. Existing approved render for visual style, never as a substitute for missing content.

If Markdown and the scan conflict, resolve obvious OCR corruption from the scan. Ask only when the difference changes the answer or grammar rule.

## 2. Extract before rendering

Create a private content specification containing:

- asset type and source chart(s);
- exact visible title and subtitle;
- directions;
- numbered items and subitems;
- blanks, choices, word banks, notes, and vocabulary glosses;
- grammar target and semantic contrasts;
- answer-key availability and whether it must be omitted;
- illustration opportunities that clarify meaning.

Do not begin image generation from raw OCR fragments.

## 3. Normalize OCR safely

- Repair broken line wraps, ligatures, apostrophes, and obvious OCR noise.
- Preserve contractions such as `haven’t`, `I’ve`, and `it’s` accurately.
- Preserve blanks as visible answer spaces; do not fill them unless the source intentionally includes a worked example.
- Keep textbook chart/exercise labels inside the image unchanged.
- Remove website watermarks, page numbers, crop seams, scan shadows, and answer-key text.
- Do not rewrite examples merely to sound more modern.

## 4. Analyze the teaching logic

For charts, identify:

- central formula or contrast;
- time relationship and timeline invariants;
- signal words;
- affirmative, negative, yes/no question, and WH-question forms when relevant;
- exceptions and high-value warnings;
- one concise takeaway question.

For exercises, identify:

- response mode: blank, multiple choice, ordering, matching, error correction, reading, or listening;
- whether one worked example is present;
- grouping that should remain together;
- visual clues that can clarify context without revealing the answer;
- whether the exercise needs multiple pages.

## 5. Split decisions

Split an exercise into `A`, `B`, etc. when one image would force body text below 22 px, cramped blanks, or illustrations below useful size. Keep numbering continuous and put the same directions on each part when it helps independent use.

Never silently omit questions to fit one canvas.

