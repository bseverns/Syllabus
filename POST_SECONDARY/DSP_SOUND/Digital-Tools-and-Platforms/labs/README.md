# Lab and Serial-Analysis Start Here

The weekly notebooks are editable analysis scaffolds. Each expects a raw capture written by `scripts/serial_logger.py` to `export/weekXX.csv`. The firmware contracts are listed in `firmware/README.md`.

## Capture

From the course root, replace the port with the verified local port:

```bash
python scripts/serial_logger.py \
  --port /dev/cu.usbmodem123 \
  --baud 115200 \
  --seconds 30 \
  --outfile export/week05.csv
```

Close Arduino Serial Monitor and any other program using the port first.

## Structured first-look route

Students who need a working parser before modifying a notebook can run:

```bash
python scripts/analyze_serial_log.py \
  --week 5 \
  --infile export/week05.csv \
  --outdir export
```

This writes a cleaned CSV and first-look plot. It filters mixed protocol/event streams to the main numeric record for Weeks 6, 9, 11, and 12. Students still annotate the evidence, calculate the assignment-specific measure, and explain limitations.

## Notebook route

1. Open the matching notebook.
2. Confirm its `weekXX.csv` path exists.
3. Read `raw_line`, split on commas, and keep only records matching the week's contract.
4. Convert numeric fields deliberately; preserve malformed/error messages separately when the assignment needs them.
5. Label axes with units and record firmware/board versions.
6. Save outputs before submission.

## No-live-board route

Use an instructor-provided redacted capture from the same firmware version. A saved dataset is a complete route for plotting, protocol, state, calibration, and critique work while hardware is repaired.
