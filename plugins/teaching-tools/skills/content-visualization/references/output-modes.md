# Output modes

## Standalone HTML — default

Choose this when the user wants one portable file, offline projection, email transfer, or simple archiving.

- Embed WebP images as data URIs.
- Embed the bundled fonts with `python3 scripts/embed_fonts.py`; do not depend on installed system fonts or a font CDN.
- Keep CSS and JavaScript inline.
- Avoid CDN fonts, icon packages, analytics, and network calls.
- Target under 25 MB unless the user accepts a larger file.
- Prefer WebP quality 82–86 and a maximum long edge of 1536 px for ordinary slide panels.

Benefits: one file, no broken paths, works offline.

Tradeoff: base64 adds about one third to the compressed asset bytes and large decks become harder to edit.

## Portable folder

Choose this for image-heavy decks, frequent asset replacement, or projected standalone size above 25 MB.

Structure:

```text
lesson/
├── index.html
└── assets/
    ├── visual-01.webp
    └── visual-02.webp
```

Keep paths relative. Do not require a build server unless the interaction genuinely needs one.

Keep fonts embedded in `index.html` even in portable-folder mode. Their compact Vietnamese/Latin subsets are shared interface dependencies.

## Hosted application

Choose only when the user needs shared live state, authentication, remote data, analytics, collaboration, or publishing.

Do not escalate a simple teaching deck into a hosted app without a concrete need.

## Visual selection

| Content | Preferred method |
|---|---|
| Exact chart or numeric comparison | HTML/SVG/Canvas chart |
| Simple process or timeline | HTML/CSS or SVG |
| Complex scene, map, character, texture | Rendered raster illustration |
| Labels and explanatory text | HTML overlay |
| Repeated icons and simple markers | Inline SVG |
| Video or heavy media | Portable folder or hosted mode |

## Size decisions

- Under 15 MB: standalone is comfortable.
- 15–25 MB: standalone remains reasonable; report the size.
- Over 25 MB: recommend portable folder or reduce image count/resolution.
- Never reduce legibility merely to meet an arbitrary file-size target.
