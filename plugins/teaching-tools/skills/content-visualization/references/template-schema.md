# Template schema

Replace the template tokens with escaped HTML content.

## Section tabs

Insert one button per section into `{{SECTION_TABS}}`:

```html
<button class="section-tab" type="button" data-target="0">
  <span class="tab-no">01</span><span class="tab-label">Hook</span>
</button>
```

Use consecutive `data-target` values. A section may contain more than one slide; give those slides the same `data-section`.

## Slides

Insert one or more articles into `{{SLIDES_HTML}}`:

```html
<article class="slide" data-index="0" data-section="0" aria-labelledby="slide-title-0">
  <div class="slide-copy">
    <p class="eyebrow">Pattern · Teaching point 01</p>
    <h1 class="slide-title" id="slide-title-0">One central idea</h1>
    <p class="lead">Keep the explanation concise and editable.</p>
    <div class="teaching-note">Optional teaching cue</div>
  </div>
  <div class="visual-board">
    <img class="embedded-visual" src="{{VISUAL_DATA_URI}}" alt="Concrete description of the visual.">
    <div class="board-title"><strong>Visual title</strong></div>
    <div class="phase-row" aria-label="Visual stages">
      <div class="phase-card"><span class="phase-name">Stage one</span><span class="phase-desc">Short cue</span></div>
      <div class="phase-card"><span class="phase-name">Stage two</span><span class="phase-desc">Short cue</span></div>
      <div class="phase-card"><span class="phase-name">Stage three</span><span class="phase-desc">Short cue</span></div>
    </div>
  </div>
</article>
```

Use unique heading IDs. The script activates the first slide automatically.

## Alternative visual content

Replace the image and overlay contents of `.visual-board` with semantic HTML, inline SVG, Canvas, or a locally bundled chart implementation when the content requires exact data interaction. Retain the board ratio or deliberately update both the frame and visual ratio.

## Comparison-first grammar slide

Use `.slide--comparison` when two images and two sentences teach a semantic or structural contrast:

```html
<article class="slide slide--comparison" data-index="0" data-section="0" aria-labelledby="slide-title-0">
  <div class="comparison-heading">
    <p class="eyebrow">Notice the difference</p>
    <h1 class="comparison-title" id="slide-title-0">Same trip. Different message.</h1>
    <p class="discovery-prompt">Which sentence gives a finished time?</p>
  </div>
  <div class="compare-grid" id="compare-0">
    <figure class="contrast-card">
      <img class="contrast-visual" src="{{VISUAL_A_DATA_URI}}" alt="Concrete description of the first meaning.">
      <figcaption class="contrast-sentence"><span class="sentence-line">I <span class="token token-past">visited</span> Da Lat <span class="token token-time">in 2024</span>.</span></figcaption>
    </figure>
    <figure class="contrast-card">
      <img class="contrast-visual" src="{{VISUAL_B_DATA_URI}}" alt="Concrete description of the second meaning.">
      <figcaption class="contrast-sentence"><span class="sentence-line">I <span class="token token-aux">have</span> <span class="token token-past">visited</span> Da Lat <span class="token token-experience">before</span>.</span></figcaption>
    </figure>
  </div>
  <div class="discovery-actions">
    <button class="compare-btn" type="button" data-compare-target="compare-0" aria-pressed="false">Highlight the difference</button>
    <button class="reveal-btn" type="button" data-reveal-target="rule-0">Reveal the rule</button>
  </div>
  <div class="rule-reveal" id="rule-0" hidden>Specific finished time → Past Simple. Life experience without a finished time → Present Perfect.</div>
</article>
```

On the initial observation screen, omit `.is-highlighted` from tokens; it is not decorative default state. The compare state is a learner action, not automatic: give `.compare-grid` (or the relevant wrapper) a unique `id`, then add a button with `data-compare-target="that-id"` in `.discovery-actions`. The template's bundled script toggles `.is-highlighted` on that element and flips the button's `aria-pressed`/label when clicked — this is what actually applies the `.is-highlighted .token-*` colors defined in the design system. A comparison slide without this button never reaches the compare stage. Use distinct image markers and run the embedding script once per marker.

Keep complete example sentences horizontal by default. Wrap each sentence in `.sentence-line`; never make individual words or grammar tokens grid rows. Use vertical sentence stacking only when the user explicitly requests a transformation or sentence-map activity.

## Required document tokens

- `{{DOCUMENT_TITLE}}`
- `{{COURSE_KICKER}}`
- `{{COURSE_TITLE}}`
- `{{SECTION_TABS}}`
- `{{SLIDES_HTML}}`
- One image marker per raster visual, such as `{{VISUAL_DATA_URI}}`
- Six bundled-font markers beginning with `{{FONT_...}}`; replace them together with `python3 scripts/embed_fonts.py OUTPUT.html`

Run the font embedding script once, then run the visual embedding script once per image marker. Use distinct markers when slides use different visuals.
