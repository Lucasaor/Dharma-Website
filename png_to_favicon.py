#!/usr/bin/env python3
"""Convert a PNG image into a favicon.ico file.

Usage:
    python png_to_favicon.py input.png
    python png_to_favicon.py input.png -o favicon.ico
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def convert_png_to_favicon(input_path: Path, output_path: Path) -> None:
    """Convert a PNG image to favicon.ico with common icon sizes."""
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]

    with Image.open(input_path) as img:
        # Keep transparency if present and normalize mode for ICO export.
        img = img.convert("RGBA")
        img.save(output_path, format="ICO", sizes=sizes)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a PNG image into a favicon.ico file"
    )
    parser.add_argument("input", type=Path, help="Path to the PNG file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("favicon.ico"),
        help="Output .ico file path (default: favicon.ico)",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    if args.input.suffix.lower() != ".png":
        raise ValueError("Input file must be a .png image")

    convert_png_to_favicon(args.input, args.output)
    print(f"Favicon created: {args.output}")


if __name__ == "__main__":
    main()
