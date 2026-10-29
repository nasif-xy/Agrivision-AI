# Soil Data Collection Guidelines

A reliable agricultural model depends on the quality and representativeness of its labels. Do not treat a folder of unverified internet images as ground truth.

## For every image
- Assign a unique sample ID.
- Record the capture date and general region when safe and appropriate.
- Record camera/device if available, lighting, soil moisture condition, and capture protocol.
- Keep the original image and a documented processed copy.
- Obtain permission to collect and use the image; remove faces, vehicle plates, and unrelated personal details.

## For soil type labels
- Define each class before collection.
- Prefer labels confirmed by a qualified person or an appropriate laboratory/field method.
- Record ambiguous cases rather than forcing a label.
- Ensure each class includes different locations, seasons, cameras, and conditions.

## For fertility measurements
- Link the soil sample to laboratory or calibrated sensor measurements.
- Record units, method, date, and sample depth.
- A visual label such as “dark soil” is not a substitute for measured N, P, K, pH, or organic matter.

## Dataset splitting and evaluation
- Keep related photos of the same sample in a single split.
- Prefer site- or farm-separated test data to measure generalization.
- Report class balance, missing data, and known geographic bias.
- Do not report accuracy until a model has been evaluated on a held-out test set.

## Privacy and sharing
- Do not publish exact farm coordinates or identifiable farmer information by default.
- Obtain explicit permission before redistributing contributed data.
- Document source, license, consent status, and any restrictions for every dataset.
