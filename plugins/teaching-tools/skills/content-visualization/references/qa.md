# QA checklist

## Visual QA

- Content stage is centered and preserves 16:9.
- Illustration frame and image ratios match.
- No accidental letterboxing, clipping of essential subjects, or broken image icon.
- Top navigator is compact and single-row.
- Active section is obvious without relying only on subtle color differences.
- Olive spot shell is visibly patterned but does not compete with the plain paper stage.
- Text remains readable at projected size.
- Short display headings render in Fraunces, technical labels in IBM Plex Mono, and learner-facing text in Be Vietnam Pro.
- Vietnamese title diacritics do not collide, clip, or trigger an unexpected fallback face.
- Wine is reserved for the main action or changed element; olive carries structure and context.
- No unresolved placeholder text appears.

## Pedagogical QA

- A learner can identify the intended difference within three to five seconds after the compare state is shown.
- Parallel sentences preserve the same character, topic, and as much wording as grammar permits.
- Only one new instructional variable is contrasted per screen.
- Two-picture pairs use equal visual weight and the images communicate distinct meanings rather than decorative variety.
- Raster images contain no pseudo-text, letters, numbers, labels, logos, or watermarks.
- The initial observation state does not leak the completed rule.
- Highlighting marks only the changed token group and remains semantically consistent across the lesson.
- The rule follows evidence and a learner prompt.
- Each reveal adds new instructional information.
- Complete example sentences read horizontally at desktop and narrow widths; grammar tokens do not become separate vertical rows.

## Interaction QA

- Every section tab is clickable.
- Back and Next update slide, current count, progress, and active tab.
- Left/Right, Home, and End keys work.
- Fullscreen button works when supported.
- Orientation control accurately reports its state.
- Every `.slide--comparison` has a working `data-compare-target` button that toggles `.is-highlighted` on its `.compare-grid`; a comparison slide with no compare trigger has silently skipped the compare stage.
- Back/Next show a visibly different (dimmed, non-pointer) state at the first and last slide, not just `disabled` in the DOM.
- Focus indicators are visible.
- Reduced-motion preference is respected.

## Standalone QA

- No `http://` or `https://` dependencies remain.
- CSS and JavaScript are inline.
- All six `{{FONT_...}}` markers are gone and every bundled `@font-face` uses an embedded WOFF2 data URI.
- Required raster assets use `data:image/...` URIs.
- IDs are unique.
- Inline JavaScript parses successfully.
- File size is reported when above 15 MB and reconsidered above 25 MB.

## Delivery QA

- Open the HTML from the filesystem, not only through a development server.
- Check one desktop viewport and one narrow viewport.
- Render a PNG preview at 1440×900 or another 16:10 canvas that shows the entire shell.
- Deliver the HTML and preview with clear filenames.
