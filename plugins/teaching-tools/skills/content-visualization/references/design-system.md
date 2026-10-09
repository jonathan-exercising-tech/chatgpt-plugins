# Design system

## Visual direction

Use a flat Nous/Hermes educational presentation style: editorial rather than corporate, bright rather than dark, and structured rather than decorative.

### Palette

| Role | Color |
|---|---|
| Shell background | `#EEE9DC` |
| Shell spots | `#596226` at about 22% opacity |
| Paper stage | `#F7F1E3` |
| Primary ink | `#2A241F` |
| Muted ink | `#746A5F` |
| Wine interaction | `#8C1D40` |
| Olive structure | `#596226` |
| Soft olive border | `#A8AD72` |
| Warm cream | `#E8DFC7` |
| Antique gold | `#C8A15A` |
| Off-white card | `#FFFDF7` |

Use dark brown and olive for hierarchy. Reserve wine for the main action, changed grammar token, or one display-title accent. Use antique gold sparingly for a secondary tape or time cue.

## Presentation shell

- Center a 16:9 content rectangle.
- Keep navigation above and controls below, outside the stage.
- Use a visible but quiet spot pattern: small olive circular dots on the light cream shell at a regular 22 px rhythm. Keep the paper stage plain so text remains easy to read.
- Limit the top section navigator to about 40–50% of stage width.
- Put number and section name on one line: `01 Hook`, `02 Concept`, `03 Pattern`.
- Keep the active tab wine with cream/off-white text.
- Keep Back and Next adjacent at bottom center.
- Use compact outline icon buttons at bottom left and right.

## Content stage

- Prefer a two-column teaching layout: concise explanation on the left, one dominant visual on the right.
- Treat that two-column layout as a general-purpose default, not a grammar default.
- For grammar discovery, prefer equal comparison cards or a form-switch layout when the learning goal is to notice a difference.
- Use one central idea per screen.
- Keep generous negative space and align to a consistent internal grid.
- Use Fraunces Bold for short display titles, IBM Plex Mono for technical labels and metadata, and Be Vietnam Pro for body copy, grammar examples, navigation, and controls.
- Keep Fraunces out of complete example sentences, buttons, and dense explanations.
- Keep IBM Plex Mono to eyebrows, step numbers, time/context badges, and compact metadata.
- Avoid long centered paragraphs.
- Keep body copy editable HTML, not raster text.

## Grammar comparison stage

- Give parallel meanings equal visual weight.
- Use mirrored card structure: image, sentence, context cue, then optional meaning cue.
- Keep one sentence directly associated with each image.
- Keep complete example sentences horizontal by default, including all colored grammar tokens.
- Preserve common sentence material and highlight only the changed tokens after the initial observation state.
- Use wine for auxiliary or changed structural paths, olive for finished-time or contextual signals, and dark brown for invariant sentence material.
- Keep rule boxes hidden until the discovery state.
- Avoid placing a long explanatory column beside two comparison images.
- Never stack individual words vertically unless the user explicitly requests a transformation or sentence-map activity.

## Raster illustration panel

- Match the frame ratio to the source image ratio.
- The bundled panel defaults to 3:2.
- Use `object-fit: cover` only when ratios match or cropping is deliberately composed.
- Use `object-fit: contain` only when visible empty space is intentionally designed.
- Treat unexplained bands between image and frame as a defect.
- Keep titles and stage labels as HTML overlays.
- Request clear negative space where overlays will sit.

## Flat-design rules

- Use hard or very restrained shadows.
- Prefer 1–3 px navy rules and simple paper-cut blocks.
- Use one subtle rotation or tape motif at most per region.
- Avoid glassmorphism, neon glow, glossy buttons, and deep photographic gradients.
- Use illustration texture inside the image, not across interface controls.

## Responsive behavior

- Preserve 16:9 on ordinary desktop projection.
- Stack text and visual below approximately 620 px.
- Let section navigation scroll horizontally on narrow screens.
- Maintain 44 px minimum control targets.
- Do not shrink body text below comfortable classroom reading size.
