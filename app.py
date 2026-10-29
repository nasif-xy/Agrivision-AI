from __future__ import annotations

import streamlit as st
from PIL import UnidentifiedImageError

from src.agrivision.image_utils import get_image_summary, open_uploaded_image

st.set_page_config(
    page_title="Agrivision AI",
    page_icon="🌱",
    layout="wide",
)

st.title("🌱 Agrivision AI")
st.caption("Soil image intake and measured-data workspace · Early prototype")

st.warning(
    "This is a starter prototype, not a validated soil diagnostic system. "
    "It does not currently classify soil or calculate fertilizer dosages."
)

st.markdown(
    """
    Agrivision AI is being developed to combine soil photographs, measured soil
    properties, and local growing conditions into more useful agricultural
    decision support.
    """
)

photo_column, data_column = st.columns([1, 1])

with photo_column:
    st.subheader("1. Soil photograph")
    uploaded_file = st.file_uploader(
        "Upload a clear soil image",
        type=["jpg", "jpeg", "png", "webp"],
        help="For future model development, collect images in varied lighting and record their locations and reference labels separately.",
    )

    if uploaded_file is not None:
        try:
            image = open_uploaded_image(uploaded_file.getvalue())
            st.image(image, caption="Uploaded soil image", use_container_width=True)
            summary = get_image_summary(image)
            st.write(f"**Image dimensions:** {summary['width']} × {summary['height']} pixels")
            st.write(f"**Color mode:** {summary['mode']}")
            st.info(
                "An image can provide visual clues about soil appearance, but it cannot "
                "reliably determine pH, nutrient concentrations, or fertilizer rates."
            )
        except (ValueError, UnidentifiedImageError):
            st.error("This file could not be read as a valid image. Please try another JPG, PNG, or WebP file.")

with data_column:
    st.subheader("2. Optional measured soil data")
    st.write("Enter values from a soil laboratory report or suitable calibrated instrument. Leave unknown values blank.")

    with st.form("soil_measurements"):
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=None, step=0.1, format="%.1f")
        nitrogen = st.number_input("Nitrogen (N) — reported units", min_value=0.0, value=None, step=1.0)
        phosphorus = st.number_input("Phosphorus (P) — reported units", min_value=0.0, value=None, step=1.0)
        potassium = st.number_input("Potassium (K) — reported units", min_value=0.0, value=None, step=1.0)
        organic_matter = st.number_input("Organic matter (%)", min_value=0.0, max_value=100.0, value=None, step=0.1)
        submitted = st.form_submit_button("Review entered measurements")

    if submitted:
        values = {
            "pH": ph,
            "Nitrogen": nitrogen,
            "Phosphorus": phosphorus,
            "Potassium": potassium,
            "Organic matter (%)": organic_matter,
        }
        provided = {name: value for name, value in values.items() if value is not None}
        if provided:
            st.write("**Values entered**")
            for name, value in provided.items():
                st.write(f"- {name}: {value}")
            st.info(
                "These values are displayed for record-keeping only. No interpretation or fertilizer "
                "recommendation is generated until validated regional thresholds and crop-specific guidance are implemented."
            )
        else:
            st.info("No measurements were entered.")

st.divider()
st.subheader("Planned next steps")
st.markdown(
    """
    - Build and validate a soil-image dataset with expert-checked labels.
    - Train and evaluate a baseline soil-type classifier.
    - Incorporate laboratory or sensor measurements for soil chemistry.
    - Add crop and fertilizer guidance based on local agronomic references.
    """
)
st.caption("Research prototype. Confirm agricultural decisions with soil testing and qualified local advice.")
