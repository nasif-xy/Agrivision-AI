from __future__ import annotations

from io import BytesIO
from PIL import Image, UnidentifiedImageError


ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}


def open_uploaded_image(image_bytes: bytes) -> Image.Image:
    """Decode and validate uploaded image bytes; return a detached RGB image."""
    if not image_bytes:
        raise ValueError("The uploaded image is empty.")

    try:
        with Image.open(BytesIO(image_bytes)) as image:
            if image.format not in ALLOWED_FORMATS:
                raise ValueError("Unsupported image format.")
            image.load()
            return image.convert("RGB")
    except UnidentifiedImageError:
        raise ValueError("The uploaded file is not a supported image.") from None


def get_image_summary(image: Image.Image) -> dict[str, int | str]:
    """Return basic metadata without attempting to infer soil properties."""
    width, height = image.size
    return {
        "width": width,
        "height": height,
        "mode": image.mode,
    }
