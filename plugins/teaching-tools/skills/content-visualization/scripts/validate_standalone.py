#!/usr/bin/env python3
"""Perform static QA on a standalone content-visualization HTML file."""

from __future__ import annotations

import argparse
import base64
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.urls: list[str] = []
        self.asset_urls: list[str] = []
        self.scripts: list[str] = []
        self._script_parts: list[str] | None = None
        self._script_type = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        for key in ("src", "href", "poster"):
            if values.get(key):
                self.urls.append(values[key] or "")
        if tag in ("img", "audio", "video", "source", "script"):
            for key in ("src", "poster"):
                if values.get(key):
                    self.asset_urls.append(values[key] or "")
        if tag == "link" and values.get("rel") in ("stylesheet", "icon", "preload"):
            if values.get("href"):
                self.asset_urls.append(values["href"] or "")
        if tag == "script":
            self._script_parts = []
            self._script_type = values.get("type") or ""

    def handle_data(self, data: str) -> None:
        if self._script_parts is not None:
            self._script_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_parts is not None:
            if self._script_type not in ("application/json", "application/ld+json"):
                self.scripts.append("".join(self._script_parts))
            self._script_parts = None
            self._script_type = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.html.is_file():
        raise SystemExit(f"File not found: {args.html}")
    text = args.html.read_text(encoding="utf-8")
    inspector = Inspector()
    inspector.feed(text)

    errors: list[str] = []
    warnings: list[str] = []
    duplicate_ids = sorted({item for item in inspector.ids if inspector.ids.count(item) > 1})
    if duplicate_ids:
        errors.append("duplicate IDs: " + ", ".join(duplicate_ids))
    external = [url for url in inspector.asset_urls if re.match(r"^(?:https?:)?//", url)]
    if external:
        errors.append("external asset URLs: " + ", ".join(external[:5]))
    unembedded_assets = [
        url for url in inspector.asset_urls
        if not url.startswith(("data:", "#"))
    ]
    if unembedded_assets:
        errors.append("unembedded local assets: " + ", ".join(unembedded_assets[:5]))
    markers = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", text)))
    if markers:
        errors.append("unresolved template markers: " + ", ".join(markers))
    for required in ("content-stage", "section-nav", "control-dock"):
        if required not in text:
            errors.append(f"missing required shell component: {required}")
    if "name=\"viewport\"" not in text and "name='viewport'" not in text:
        errors.append("missing viewport meta tag")

    embedded_bytes = 0
    for payload in re.findall(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", text):
        try:
            embedded_bytes += len(base64.b64decode(payload, validate=True))
        except ValueError:
            errors.append("invalid embedded image base64")

    font_payloads = re.findall(r"data:font/woff2;base64,([A-Za-z0-9+/=]+)", text)
    if len(font_payloads) < 6:
        errors.append(f"expected 6 embedded WOFF2 fonts; found {len(font_payloads)}")
    embedded_font_bytes = 0
    for payload in font_payloads:
        try:
            embedded_font_bytes += len(base64.b64decode(payload, validate=True))
        except ValueError:
            errors.append("invalid embedded font base64")
    for family in ("CV Fraunces", "CV IBM Plex Mono", "CV Be Vietnam Pro"):
        if family not in text:
            errors.append(f"missing bundled font family: {family}")

    node = shutil.which("node")
    if node:
        checker = "new Function(require('fs').readFileSync(0,'utf8'))"
        for index, script in enumerate(inspector.scripts, 1):
            result = subprocess.run(
                [node, "-e", checker], input=script, text=True, capture_output=True
            )
            if result.returncode:
                errors.append(f"inline script {index} does not parse")
    elif inspector.scripts:
        warnings.append("Node.js unavailable; inline JavaScript was not parsed")

    file_bytes = args.html.stat().st_size
    if file_bytes > 25 * 1024 * 1024:
        warnings.append("file exceeds 25 MB; consider portable-folder mode")
    elif file_bytes > 15 * 1024 * 1024:
        warnings.append("file exceeds 15 MB; report the size to the user")
    if not re.search(r"<img\b|<svg\b|<canvas\b", text, re.I):
        warnings.append("no embedded raster, SVG, or Canvas visual detected")

    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        f"PASS: {args.html} | {file_bytes} bytes | "
        f"{embedded_bytes} embedded image bytes | {embedded_font_bytes} embedded font bytes | "
        f"{len(inspector.scripts)} inline scripts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
