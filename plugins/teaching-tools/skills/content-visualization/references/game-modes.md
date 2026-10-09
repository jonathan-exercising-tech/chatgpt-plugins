# Game modes

## Selection and source of truth

If the user supplies a specific game concept, implement it. Otherwise, a request for a game, warm-up, or vocabulary game selects Mysterious Cups. Copy `../assets/game-templates/mysterious-cups.html` relative to this reference's directory; never reconstruct the approved game shell from memory.

## Adapt the preset

Edit the `questions` array: each item has `answer`, `description`, and an embedded `image` data URI. Replace all topic-specific headings, intro instructions, finish copy, and image descriptions to match the supplied content. Round count derives from `questions.length`; also update any static introductory count. Preserve the existing rewards and scoring unless a change is requested. Escape content safely when it enters HTML or JavaScript. Use words with at least two distinct letters with the existing scramble function; adapt that function to handle one-letter/repeated-letter inputs if supplied. Do not ship stale tourist-leaflet copy for a different topic.

For subject pictures follow Content Illustration; for grammar visuals follow Grammar Chart through the sibling skill links in SKILL.md. Keep controls and scores as HTML. Embed compressed pictures and retain offline fonts.

## Round rules

1. Both teams participate in every round.
2. Hint 1 is Description, Hint 2 is Picture, Hint 3 is Unscramble / Word Puzzle. Present and teach them in this order, each in its own popup.
3. A separate Reveal Answer button reveals the word.
4. Teams play rock–paper–scissors outside the interface. The teacher selects the RPS winner.
5. The winner opens the first cup and receives its reward.
6. The other team must open a different cup and receives its reward.
7. Next stays disabled until both cups have been opened. Retain Restart, progress, both scores, and final results.

## Approved layout

- Spotted cream shell, dark ink, wine, olive, and antique gold.
- Two rectangular scoreboards at top-center on one row, team name left and score right.
- Main lower area divides 2/3 for content and 1/3 for Mystery Cups on desktop.
- Three equal square hint tiles in a horizontal row, with prominent Hint 1 / Hint 2 / Hint 3 labels.
- Reveal Answer is a separate button below the tiles.
- All hints use popups. The picture is large and entirely contained in its popup. Preserve the two text popup layouts unless fixing a demonstrated defect.
- Keep the preset's narrow-screen adaptation; inspect it rather than blindly forcing desktop dimensions.

## Functional QA

- Open the standalone file at desktop and narrow width; inspect overflow, text and picture fit, and console errors.
- Open and close all three popups; verify Description → Picture → Word Puzzle labeling and content.
- Before revealing the answer, cups are locked and Next disabled.
- Reveal Answer exposes RPS selection; cups remain locked until a winner is selected.
- Test either team winning RPS. First cup rewards the winner; the second different cup rewards the other team.
- After one cup, Next remains disabled; after two, Next enables and the third cup locks.
- Next resets hints, RPS selection, and cup locks for the new round while preserving scores.
- Play every round and verify final scores/winner and progress.
- Restart from mid-game and after completion resets scores, round, hints, and locks.
- Run `scripts/validate_standalone.py` from the skill root against the adapted HTML.
