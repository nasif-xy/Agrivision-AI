# Agrivision AI 🌱

**AI-assisted soil assessment and crop suitability for Ethiopian agriculture.**

Agrivision AI is a research and development project exploring how computer vision and soil measurements can help farmers and agricultural students understand soil characteristics and make better-informed crop choices.

> **Project status: Early-stage prototype.** A trained model and validated field recommendations are not included yet. This repository provides the project foundation and development plan; it does not claim that soil analysis is already accurate or production-ready.

## The problem

Soil characteristics influence which crops grow well and how nutrients should be managed. Farmers may have limited access to laboratory testing and timely agronomic advice. A mobile-friendly tool could help organize soil observations and make reliable agricultural information easier to access.

## Planned capabilities

- **Soil image classification:** explore visible soil categories such as sandy, clay-rich, and loamy soil using a properly labeled dataset.
- **Soil measurements:** record pH, nitrogen (N), phosphorus (P), potassium (K), and other measurements when supplied by a soil test or appropriate sensor.
- **Crop suitability:** combine soil data with location, rainfall, temperature, altitude, season, and water availability.
- **Fertilizer guidance:** provide cautious, source-backed guidance only when enough reliable measurements and crop-specific recommendations are available.
- **Farmer-friendly experience:** build toward a simple interface suitable for local use and future language support.

## Important scientific limitation

A photograph alone cannot reliably measure soil pH, NPK concentrations, organic matter, or the exact fertilizer quantity required. Image appearance also changes with moisture, lighting, camera, and location. Agrivision AI will therefore distinguish **visible-image predictions** from **measured soil properties** and will not present an unvalidated estimate as a laboratory result.

Crop recommendations must also account for local climate and agronomic evidence. The system is intended to support—not replace—soil testing or advice from qualified agricultural professionals.

## How it is planned to work

1. Collect soil images and trustworthy labels from diverse Ethiopian locations.
2. Document dataset sources, permissions, collection conditions, and label quality.
3. Split data by sample/site where possible to reduce data leakage.
4. Train and evaluate a baseline image classifier before considering more complex models.
5. Add structured soil measurements and contextual crop-suitability rules.
6. Evaluate with agricultural experts and field observations before real-world use.

## Repository structure

```text
Agrivision-AI/
├── app.py                  # Streamlit prototype
├── src/
│   └── agrivision/
│       ├── __init__.py
│       └── soil_data.py    # Input validation and cautious guidance
├── tests/
│   └── test_soil_data.py
├── data/
│   └── README.md           # Dataset instructions; no private data committed
├── models/
│   └── README.md           # Model artifacts and training status
├── docs/
│   └── roadmap.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

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

## Dataset and model status

No dataset or trained model is bundled at this stage. See [data/README.md](data/README.md) and [models/README.md](models/README.md) before adding data or model artifacts. Do not upload private farmer information or datasets unless their licenses and consent conditions permit it.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for the planned milestones, evaluation criteria, and risk controls.

## Contributing

Issues, dataset documentation, agronomy references, and code contributions are welcome. Please explain the source of any dataset or recommendation rule and avoid presenting unvalidated results as established facts.

## License

This project is licensed under the MIT License; see [LICENSE](LICENSE).

---

**Built with a focus on responsible AI for Ethiopian agriculture.**
