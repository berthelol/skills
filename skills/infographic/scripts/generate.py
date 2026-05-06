"""Generate a modern operator-style infographic via OpenAI gpt-image-2.

Usage from a skill workflow:
    from generate import render
    render(
        prompt="...full prompt text...",
        out_name="my-piece",
        size="4:5",                                  # "4:5", "1:1", or "16:9"
        reference_images=["logo1.png", "avatar.png"],
        out_dir="infographics/outputs",
        assets_dir="infographics/assets",
    )

Or as CLI:
    OPENAI_API_KEY=sk-... python3 generate.py path/to/prompt.txt my-piece 4:5 logo1.png avatar.png
"""
from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

from openai import OpenAI

SIZE_MAP = {
    "4:5": "1024x1536",
    "1:1": "1024x1024",
    "16:9": "1536x1024",
}

DEFAULT_MODEL = "gpt-image-2"


def render(
    prompt: str,
    out_name: str,
    size: str = "4:5",
    reference_images: list[str] | None = None,
    out_dir: str | Path = "infographics/outputs",
    assets_dir: str | Path = "infographics/assets",
    model: str = DEFAULT_MODEL,
    quality: str = "high",
) -> Path:
    """Render an infographic.

    Returns the path to the saved PNG.

    If reference_images are provided, uses client.images.edit so the model treats
    them as visual references (logos, avatar, screenshots). Otherwise uses
    client.images.generate.
    """
    if size not in SIZE_MAP:
        raise ValueError(f"size must be one of {list(SIZE_MAP)}, got {size!r}")

    api_size = SIZE_MAP[size]
    out_dir = Path(out_dir)
    assets_dir = Path(assets_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = OpenAI()
    print(f"Generating {out_name} ({size} → {api_size}) via {model}...")

    if reference_images:
        files = []
        for fname in reference_images:
            p = assets_dir / fname
            if not p.exists():
                raise FileNotFoundError(f"Reference image not found: {p}")
            files.append(open(p, "rb"))
        try:
            result = client.images.edit(
                model=model,
                image=files,
                prompt=prompt,
                size=api_size,
                quality=quality,
            )
        finally:
            for f in files:
                f.close()
    else:
        result = client.images.generate(
            model=model,
            prompt=prompt,
            size=api_size,
            quality=quality,
        )

    image_b64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_b64)
    out_path = out_dir / f"{out_name}.png"
    out_path.write_bytes(image_bytes)
    print(f"Saved: {out_path}")
    return out_path


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Render an infographic via gpt-image-2")
    parser.add_argument("prompt_file", help="Path to a text file containing the full prompt")
    parser.add_argument("out_name", help="Output filename stem (no extension)")
    parser.add_argument("size", choices=list(SIZE_MAP), default="4:5", nargs="?")
    parser.add_argument("reference_images", nargs="*", help="Filenames inside assets_dir")
    parser.add_argument("--out-dir", default="infographics/outputs")
    parser.add_argument("--assets-dir", default="infographics/assets")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    args = parser.parse_args()

    prompt = Path(args.prompt_file).read_text()
    render(
        prompt=prompt,
        out_name=args.out_name,
        size=args.size,
        reference_images=args.reference_images or None,
        out_dir=args.out_dir,
        assets_dir=args.assets_dir,
        model=args.model,
        quality=args.quality,
    )
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
