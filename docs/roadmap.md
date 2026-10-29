# Agrivision AI roadmap

The project is at the **starter prototype** stage. No trained model or validated crop/fertilizer engine is included.

1. **Define the scope:** agree on initial soil classes and target regions with agricultural practitioners.
2. **Collect reliable data:** gather permitted soil images with documented collection conditions and expert-checked labels.
3. **Establish a baseline:** train a reproducible image classifier and evaluate on held-out locations where possible.
4. **Add soil measurements:** accept laboratory or calibrated sensor data with units and provenance.
5. **Develop crop suitability:** include climate, rainfall, altitude, season, water availability, and regional agronomy references.
6. **Validate fertilizer guidance:** use measured inputs and trusted crop-specific recommendations; review with qualified agronomists.
7. **Field-test and monitor:** evaluate robustness, usability, uncertainty, and failures before real-world use.

## Evaluation principles

- Avoid data leakage between training and test sets.
- Report class balance and per-class metrics, not accuracy alone.
- Allow the system to abstain when confidence is low or inputs are outside the supported scope.
- Never claim that a photo measures soil chemistry or determines a fertilizer dosage.
- Keep data provenance, privacy, and licensing documented.

See [data collection guidelines](DATA_GUIDELINES.md).