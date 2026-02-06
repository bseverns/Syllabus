#!/usr/bin/env python3
"""Bridge Serial lines to MIDI CC messages (optional lane).

Expected line:
  CC,<cc>,<val_0_127>,<channel_1_16>

Requires: mido + python-rtmidi + pyserial
"""
import argparse, time
import serial

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True)
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--midi_out", required=True)
    args = ap.parse_args()

    import mido
    ser = serial.Serial(args.port, args.baud, timeout=1)
    time.sleep(2.0)
    out = mido.open_output(args.midi_out)

    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 4 or parts[0] != "CC":
            continue
        cc = int(parts[1]); val = int(parts[2]); ch = int(parts[3])
        out.send(mido.Message("control_change", control=cc, value=val, channel=max(0, min(15, ch-1))))

if __name__ == "__main__":
    main()
