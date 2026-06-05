
import numpy as np
import pandas as pd

np.random.seed(42)

NUM_SAMPLES = 500

RANGES = {
    "Cr": (16, 19),
    "Ni": (6, 9),
    "Mo": (1, 3),
    "Mn": (1, 4),
    "C":  (0.01, 0.05),
    "Si": (0.2, 0.8)
}

alloys = []

for i in range(NUM_SAMPLES):

    comp = {
        element: np.random.uniform(low, high)
        for element, (low, high)
        in RANGES.items()
    }

    total = sum(comp.values())
    comp["Fe"] = 100 - total
    comp["ID"] = f"A{i+1}"

    alloys.append(comp)

df = pd.DataFrame(alloys)

cols = [
    "ID","Fe","Cr","Ni",
    "Mo","Mn","C","Si"
]

df = df[cols]

df.to_excel(
    "candidate_c_alloys.xlsx",
    index=False
)

df.to_excel(
    "candidate_c_alloys.xlsx",
    index=False
)

print("Alloy dataset generated.")
print(df.head())