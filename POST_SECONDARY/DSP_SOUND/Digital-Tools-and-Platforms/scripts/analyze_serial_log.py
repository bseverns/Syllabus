#!/usr/bin/env python3
"""Parse a course Serial log and export a clean table plus first-look plot."""

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt


SCHEMAS = {
    1: (None, ["t_ms", "led_state"]),
    2: (None, ["t_ms", "raw_pressed", "debounced_pressed"]),
    3: (None, ["t_ms", "raw", "smoothed", "pwm"]),
    4: (None, ["t_ms", "tick", "interval_ms"]),
    5: (None, ["t_ms", "raw", "active"]),
    6: ("DATA", ["t_ms", "analog", "led_state"]),
    7: (None, ["t_ms", "channel", "value"]),
    8: (None, ["t_ms", "state", "raw"]),
    9: ("DATA", ["t_ms", "state", "raw"]),
    10: (None, ["t_ms", "raw", "mapped", "minimum", "maximum"]),
    11: ("MIDI", ["message_type", "number", "value", "channel"]),
    12: ("KNOB", ["t_ms", "control", "value", "mode"]),
}


def parse_numeric(value: str):
    try:
        return float(value)
    except ValueError:
        return None


def parse_rows(path: Path, week: int):
    prefix, fields = SCHEMAS[week]
    parsed = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            parts = [part.strip() for part in row["raw_line"].split(",")]
            if prefix is not None:
                if not parts or parts[0] != prefix:
                    continue
                parts = parts[1:]
            if len(parts) != len(fields):
                continue
            parsed.append(dict(zip(fields, parts)))
    return fields, parsed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, choices=range(1, 13), required=True)
    parser.add_argument("--infile", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, default=Path("export"))
    args = parser.parse_args()

    fields, rows = parse_rows(args.infile, args.week)
    if not rows:
        raise SystemExit("No rows matched the selected week's firmware contract.")

    args.outdir.mkdir(parents=True, exist_ok=True)
    clean_path = args.outdir / f"week{args.week:02d}_clean.csv"
    with clean_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    x_field = "t_ms" if "t_ms" in fields else None
    x_values = [parse_numeric(row[x_field]) for row in rows] if x_field else list(range(len(rows)))
    plotted = 0
    plt.figure(figsize=(9, 4.5))
    for field in fields:
        if field == x_field:
            continue
        values = [parse_numeric(row[field]) for row in rows]
        if all(value is not None for value in values):
            plt.plot(x_values, values, label=field)
            plotted += 1
    if not plotted:
        raise SystemExit("Rows parsed, but no numeric output fields were available to plot.")
    plt.xlabel(x_field or "record")
    plt.ylabel("value")
    plt.title(f"Week {args.week:02d} first-look Serial data")
    plt.legend()
    plt.tight_layout()
    plot_path = args.outdir / f"week{args.week:02d}_firstlook.png"
    plt.savefig(plot_path, dpi=150)
    print(f"Parsed {len(rows)} rows")
    print(f"Wrote {clean_path}")
    print(f"Wrote {plot_path}")


if __name__ == "__main__":
    main()
