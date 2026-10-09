#!/usr/bin/env python3
"""Embed the bundled teaching font system into a standalone HTML file."""

from __future__ import annotations

import argparse
import base64
from pathlib import Path


FONT_FILES = {
    "{{FONT_FRAUNCES_WOFF2}}": "fraunces-bold-vietnamese.woff2",
    "{{FONT_PLEX_REGULAR_WOFF2}}": "ibm-plex-mono-regular-vietnamese.woff2",
    "{{FONT_PLEX_SEMIBOLD_WOFF2}}": "ibm-plex-mono-semibold-vietnamese.woff2",
    "{{FONT_BEVN_REGULAR_WOFF2}}": "be-vietnam-pro-regular.woff2",
    "{{FONT_BEVN_SEMIBOLD_WOFF2}}": "be-vietnam-pro-semibold.woff2",
    "{{FONT_BEVN_EXTRABOLD_WOFF2}}": "be-vietnam-pro-extrabold.woff2",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path, help="Standalone HTML file to update in place")
    args = parser.parse_args()
    html_path = args.html.resolve()
    if not html_path.is_file():
        raise SystemExit(f"HTML file not found: {html_path}")

    font_dir = Path(__file__).resolve().parent.parent / "assets" / "fonts"
    source = html_path.read_text(encoding="utf-8")
    missing = [token for token in FONT_FILES if token not in source]
    if missing:
        raise SystemExit("Font markers are missing or already embedded: " + ", ".join(missing))

    for token, filename in FONT_FILES.items():
        font_path = font_dir / filename
        if not font_path.is_file():
            raise SystemExit(f"Bundled font not found: {font_path}")
        source = source.replace(
            token, base64.b64encode(font_path.read_bytes()).decode("ascii")
        )
    html_path.write_text(source, encoding="utf-8")
    print(f"Embedded {len(FONT_FILES)} font files into {html_path}")


if __name__ == "__main__":
    main()
