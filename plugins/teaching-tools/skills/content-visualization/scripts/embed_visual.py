#!/usr/bin/env python3
"""Resize, compress, and embed a raster visual in an HTML template."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import tempfile

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_image", type=Path)
    parser.add_argument("--html", required=True, type=Path)
    parser.add_argument("--marker", default="{{VISUAL_DATA_URI}}")
    parser.add_argument("--output-html", required=True, type=Path)
    parser.add_argument("--output-webp", required=True, type=Path)
    parser.add_argument("--max-width", type=int, default=1536)
    parser.add_argument("--quality", type=int, default=84)
    parser.add_argument(
        "--portable",
        action="store_true",
        help="Reference the WebP relatively instead of embedding a data URI.",
    )
    return parser.parse_args()


def atomic_write(path: Path, text: str) -> None:
    mode = (path.stat().st_mode & 0o777) if path.exists() else 0o644
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        handle.write(text)
        temp_name = handle.name
    os.replace(temp_name, path)
    path.chmod(mode)


def main() -> int:
    args = parse_args()
    if not 1 <= args.quality <= 100:
        raise SystemExit("--quality must be between 1 and 100")
    if args.max_width < 64:
        raise SystemExit("--max-width must be at least 64")
    if not args.input_image.is_file() or not args.html.is_file():
        raise SystemExit("Input image and HTML template must exist")

    source_bytes = args.input_image.stat().st_size
    with Image.open(args.input_image) as image:
        image.load()
        original_size = image.size
        if image.width > args.max_width:
            height = round(image.height * args.max_width / image.width)
            image = image.resize((args.max_width, height), Image.Resampling.LANCZOS)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "transparency" in image.info else "RGB")
        args.output_webp.parent.mkdir(parents=True, exist_ok=True)
        image.save(
            args.output_webp,
            "WEBP",
            quality=args.quality,
            method=6,
            exact=image.mode == "RGBA",
        )
        final_size = image.size

    html = args.html.read_text(encoding="utf-8")
    marker_count = html.count(args.marker)
    if marker_count == 0:
        raise SystemExit(f"Marker not found: {args.marker}")

    if args.portable:
        replacement = os.path.relpath(
            args.output_webp.resolve(), args.output_html.resolve().parent
        ).replace(os.sep, "/")
        mode = "portable"
    else:
        payload = base64.b64encode(args.output_webp.read_bytes()).decode("ascii")
        replacement = f"data:image/webp;base64,{payload}"
        mode = "standalone"

    atomic_write(args.output_html, html.replace(args.marker, replacement))
    result = {
        "mode": mode,
        "source_bytes": source_bytes,
        "webp_bytes": args.output_webp.stat().st_size,
        "original_dimensions": original_size,
        "final_dimensions": final_size,
        "markers_replaced": marker_count,
        "output_html": str(args.output_html.resolve()),
        "output_webp": str(args.output_webp.resolve()),
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
