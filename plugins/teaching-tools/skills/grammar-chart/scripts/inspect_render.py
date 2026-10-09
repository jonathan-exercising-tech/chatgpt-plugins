#!/usr/bin/env python3
"""Coarse technical inspection for EF grammar renders."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageStat


NAME_PATTERNS = {
    "chart": re.compile(r"^(?:CH\d{2}|EF-S\d{2})_CHART-\d+-\d+[A-Z]?\.png$"),
    "exercise": re.compile(r"^EF-S\d{2}_(?:DRILL|EX)-\d+[A-Z]?\.png$"),
    "pretest": re.compile(r"^(?:CH\d{2}|EF-S\d{2})_PRETEST\.png$"),
    "listening": re.compile(r"^EF-S\d{2}_(?:DRILL|EX)-\d+[A-Z]?\.png$"),
}


def rgb_distance(a: tuple[float, ...], b: tuple[int, int, int]) -> float:
    return sum((a[i] - b[i]) ** 2 for i in range(3)) ** 0.5


def inspect(path: Path, kind: str) -> list[str]:
    issues: list[str] = []
    if not NAME_PATTERNS[kind].match(path.name):
        issues.append(f"filename does not match the {kind} convention")

    with Image.open(path) as image:
        image = image.convert("RGB")
        width, height = image.size
        if (width, height) != (1536, 1024):
            issues.append(f"non-default dimensions: {width}x{height}")
        ratio = width / height
        if not 1.45 <= ratio <= 1.55:
            issues.append(f"unexpected aspect ratio: {ratio:.3f}")

        top = image.crop((0, 0, width, max(1, int(height * 0.12))))
        top_mean = ImageStat.Stat(top).mean
        if rgb_distance(tuple(top_mean), (10, 45, 120)) > 120:
            issues.append("header is not predominantly cobalt/navy")

        whole_mean = ImageStat.Stat(image).mean
        if max(whole_mean) - min(whole_mean) < 8:
            issues.append("image appears unusually low in color variation")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("--kind", choices=sorted(NAME_PATTERNS), required=True)
    args = parser.parse_args()

    if not args.image.is_file():
        print(f"FAIL: file not found: {args.image}")
        return 2

    issues = inspect(args.image, args.kind)
    if issues:
        print("CHECK:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("PASS: dimensions, filename, aspect ratio, and coarse palette checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
