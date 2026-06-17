"""
Generate the shared simulated NIEHS biomarker dataset used throughout the
Jupyter (morning) and marimo (afternoon) sessions.

This is a Python re-implementation of the `biomarker_data` dataset from the
R Markdown / Quarto workshop (N=200, seed=42, PFOA/cholesterol/age/sex/site).
Exact values will differ from the R version (different RNG algorithms), but
the structure, distributions, and "story" are the same -- this keeps the
day's running example consistent with prior NIEHS trainings.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 200

participant_id = np.arange(1, n + 1)
age = np.round(rng.normal(48, 14, n)).astype(int)
sex = rng.choice(["Female", "Male"], size=n, p=[0.55, 0.45])
pfoa_serum = np.round(rng.lognormal(mean=0.8, sigma=0.9, size=n), 2)
cholesterol = np.round(rng.normal(210, 38, n)).astype(int)
site = rng.choice(
    ["Research Triangle Park", "Durham", "Chapel Hill"], size=n
)

biomarker_data = pd.DataFrame(
    {
        "participant_id": participant_id,
        "age": age,
        "sex": sex,
        "pfoa_serum": pfoa_serum,
        "cholesterol": cholesterol,
        "site": site,
    }
)

biomarker_data.to_csv("biomarker_data.csv", index=False)
print(biomarker_data.head())
print(f"\nShape: {biomarker_data.shape}")
print(f"\nSites: {biomarker_data['site'].value_counts().to_dict()}")
