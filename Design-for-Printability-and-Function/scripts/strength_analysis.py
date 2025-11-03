"""Quick analysis for class test data.
Usage: place CSVs in ../data and run this script to print summary stats.
"""
import pandas as pd
from pathlib import Path

data_dir = Path(__file__).resolve().parent.parent / "data"
files = list(data_dir.glob("*.csv"))
if not files:
    print("No CSV files found in data/. Add logs and re-run.")
    raise SystemExit(0)

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
numeric_cols = [c for c in ["force_N", "cycles_to_failure"] if c in df.columns]
group = df.groupby(["material","layer_height","infill","perimeters","orientation"])[numeric_cols].mean().reset_index()
print("=== Averages by setting combo ===")
print(group.to_string(index=False))
