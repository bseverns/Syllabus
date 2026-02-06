#!/usr/bin/env python3
"""Send one command and print responses (serial).
Use for INFO/SELFTEST style interfaces."""
import argparse, time
import serial

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--cmd", required=True)
    ap.add_argument("--timeout", type=float, default=2.0)
    args = ap.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=0.2)
    time.sleep(1.2)
    ser.write((args.cmd.strip()+"\n").encode("utf-8"))

    t0 = time.time()
    out=[]
    while time.time()-t0 < args.timeout:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line:
            out.append(line)
    ser.close()
    print("\n".join(out) if out else "(no response)")

if __name__ == "__main__":
    main()
