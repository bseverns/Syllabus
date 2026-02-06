#!/usr/bin/env python3
"""Quick plotter for serial_logger outputs."""
import sys, csv
import numpy as np
import matplotlib.pyplot as plt

def main(path):
    times = []
    values = []
    with open(path, "r", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            raw = row["raw_line"]
            # try parse 't_ms,value' else treat as single value
            if "," in raw:
                parts = raw.split(",")
                try:
                    tms = float(parts[0])
                    v = float(parts[1])
                    times.append(tms/1000.0)
                    values.append(v)
                except Exception:
                    pass
            else:
                try:
                    values.append(float(raw))
                    times.append(len(values))
                except Exception:
                    pass

    if not values:
        print("No numeric values parsed.")
        return

    plt.figure()
    plt.plot(times, values)
    plt.title(path)
    plt.xlabel("time (s)")
    plt.ylabel("value")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/plot_csv.py export/week01.csv")
        raise SystemExit(2)
    main(sys.argv[1])
