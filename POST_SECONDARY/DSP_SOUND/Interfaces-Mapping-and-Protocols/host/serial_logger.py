#!/usr/bin/env python3
"""Serial logger: reads newline lines and writes to CSV.

Usage:
  python host/serial_logger.py --port YOUR_PORT --baud 115200 --outfile export/week01.csv --seconds 30
"""
import argparse, csv, time
import serial

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--outfile", required=True)
    ap.add_argument("--seconds", type=float, default=30.0)
    args = ap.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    time.sleep(2.0)
    t0 = time.time()

    with open(args.outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["host_time_s", "line"])
        while time.time() - t0 < args.seconds:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line:
                continue
            w.writerow([time.time(), line])
            print(line)

    ser.close()
    print("Wrote", args.outfile)

if __name__ == "__main__":
    main()
