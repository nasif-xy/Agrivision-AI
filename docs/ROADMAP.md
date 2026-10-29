# Agrivision AI — Development Roadmap

## Phase 1: Define the problem
- Choose the initial target users and use cases with Ethiopian agricultural practitioners.
- Define soil classes that can be distinguished consistently from photographs.
- Document the intended geographic coverage and known limitations.

## Phase 2: Build a trustworthy dataset
- Collect soil photographs using a repeatable protocol.
- Record sample ID, collection date, approximate region, image conditions, and expert-confirmed reference class.
- Where fertility is studied, link samples to laboratory measurements such as pH, N, P, K, and organic matter.
- Keep personally identifying information and exact farm coordinates out of public datasets unless explicitly needed and consented to.
- Split train, validation, and test data by sample/site where possible, not just by near-duplicate image.

## Phase 3: Computer-vision baseline
- Start with a reproducible baseline model and transfer learning.
- Compare against a simple baseline; report per-class precision, recall, F1, confusion matrix, and dataset composition.
- Evaluate robustness across cameras, lighting, moisture, and locations.
- Show uncertainty and avoid a prediction when the input is out of scope.

## Phase 4: Soil measurement support
- Accept laboratory or calibrated sensor measurements with explicit units.
- Validate ranges and retain the measurement source/date.
- Do not infer soil chemistry from a photograph alone.

## Phase 5: Crop suitability
- Include soil properties, local climate, rainfall, altitude, season, irrigation/water availability, and crop variety.
- Use regionally appropriate and traceable agronomic references.
- Validate outputs with agricultural experts and field observations.

## Phase 6: Fertilizer guidance
- Require appropriate measured inputs and crop-specific context.
- Use validated local guidance; show assumptions, units, and source.
- Do not provide dosage estimates from image appearance alone.
- Test recommendations with qualified agronomists before deployment.

## Phase 7: Deployment and monitoring
- Test with intended users and low-connectivity conditions.
- Measure usability and model performance across regions.
- Version datasets/models, document failures, and provide a route to report incorrect advice.
