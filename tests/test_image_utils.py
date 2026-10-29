from io import BytesIO

import pytest
from PIL import Image

from src.agrivision.image_utils import get_image_summary, open_uploaded_image


def make_png() -> bytes:
    image = Image.new("RGB", (32, 24), (120, 90, 60))
    output = BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()


def test_open_uploaded_image_returns_rgb_image():
    image = open_uploaded_image(make_png())
    assert image.mode == "RGB"
    assert image.size == (32, 24)


def test_empty_upload_is_rejected():
    with pytest.raises(ValueError, match="empty"):
        open_uploaded_image(b"")


def test_invalid_upload_is_rejected():
    with pytest.raises(ValueError):
        open_uploaded_image(b"this is not an image")


def test_image_summary_reports_dimensions_and_mode():
    image = open_uploaded_image(make_png())
    assert get_image_summary(image) == {
        "width": 32,
        "height": 24,
        "mode": "RGB",
    }
