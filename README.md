# Agrivision AI 🌱

**AI-assisted soil assessment and crop suitability for Ethiopian agriculture.**

Agrivision AI is an early-stage research project exploring how soil photographs, measured soil data, and local growing conditions could support better-informed agricultural decisions.

> **Status: Starter prototype.** The current app supports image upload and recording optional measurements. It does not yet classify soil, estimate fertility, or recommend crop/fertilizer rates. No trained model is included.

## The problem

Soil characteristics influence crop growth and nutrient management. A future mobile-friendly tool could help organize soil observations and make reliable agricultural information easier to access.

## Planned capabilities

- **Soil image classification:** explore visible soil categories such as sandy, clay-rich, and loamy soil using a properly labelled dataset.
- **Soil measurements:** record pH, nitrogen (N), phosphorus (P), potassium (K), and other measured properties.
- **Crop suitability:** combine soil properties with rainfall, temperature, altitude, season, and water availability.
- **Fertilizer guidance:** provide cautious, source-backed guidance only when enough reliable measurements and crop-specific recommendations are available.
- **Explainable results:** show inputs, uncertainty, sources, and limitations.

## Important scientific limitation

A photograph alone cannot reliably measure soil pH, NPK concentrations, organic matter, or the exact fertilizer quantity required. Appearance changes with moisture, lighting, camera, and location. The project will distinguish **visual predictions** from **measured soil properties** and will not present an unvalidated estimate as a laboratory result.

Crop recommendations must also account for local climate and agronomic evidence. The system is intended to support—not replace—soil testing or advice from qualified agricultural professionals.

## Run the prototype

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/nasif-xy/Agrivision-AI.git
cd Agrivision-AI
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies and launch:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Run tests:

```bash
python -m pytest
```

## Repository structure

```text
Agrivision-AI/
├── app.py
├── docs/
│   ├── ROADMAP.md
│   ├── roadmap.md
│   └── DATA_GUIDELINES.md
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── models/
│   └── README.md
├── src/agrivision/
│   ├── __init__.py
│   └── image_utils.py
├── tests/
│   └── test_image_utils.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Development roadmap

1. Define the initial soil classes and target regions with agricultural practitioners.
2. Collect diverse, permitted soil photos and reliable reference labels.
3. Keep train, validation, and test sets separated by sample/site where possible to reduce data leakage.
4. Train and evaluate a baseline image classifier; report per-class precision/recall and a confusion matrix.
5. Incorporate measured soil chemistry and locally appropriate agronomic references.
6. Build crop-suitability logic that includes climate and growing conditions.
7. Validate recommendations with agricultural experts and field trials before real-world use.
8. Document limitations, model version, data sources, and performance.

Read the [roadmap](docs/roadmap.md) and [data collection guidelines](docs/DATA_GUIDELINES.md) before contributing datasets or recommendation rules.

## Responsible use

This project is for learning and research. Do not use it as the sole basis for fertilizer application, crop selection, or other decisions that could affect a farmer's livelihood. Confirm important decisions with soil testing and qualified local agricultural advice.

## Data and privacy

No dataset or trained model is bundled yet. Do not upload private farmer information, precise farm coordinates, or third-party images unless permission and licensing conditions allow it. See [data/README.md](data/README.md).

## License

This project is licensed under the MIT License; see [LICENSE](LICENSE).

---

**Built with a focus on responsible AI for Ethiopian agriculture.**
