#!/usr/bin/env python3
"""Log loop timing reports (expects firmware printing: LOOP,<t_us> lines)."""
import argparse, csv, time
import serial

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--seconds", type=float, default=10.0)
    ap.add_argument("--outfile", default="export/loop.csv")
    args = ap.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    time.sleep(1.5)
    t0 = time.time()

    rows = []
    while time.time() - t0 < args.seconds:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line.startswith("LOOP,"):
            try:
                us = int(line.split(",")[1])
                rows.append((time.time(), us))
            except:
                pass

    ser.close()
    with open(args.outfile, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["host_time_s", "loop_us"])
        w.writerows(rows)

    print("Wrote", args.outfile, "rows:", len(rows))

if __name__ == "__main__":
    main()
