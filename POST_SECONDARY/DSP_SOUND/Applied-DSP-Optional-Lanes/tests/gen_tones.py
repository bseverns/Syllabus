#!/usr/bin/env python3
import argparse, numpy as np, soundfile as sf, os

def sine(sr, dur, hz, amp=0.2):
    t=np.arange(int(sr*dur))/sr
    return (amp*np.sin(2*np.pi*hz*t)).astype(np.float32)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sr", type=int, default=48000)
    ap.add_argument("--dur", type=float, default=2.0)
    ap.add_argument("--outdir", default="tests/assets")
    args=ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    sf.write(f"{args.outdir}/sine_440.wav", sine(args.sr,args.dur,440), args.sr)
    sf.write(f"{args.outdir}/sine_1000.wav", sine(args.sr,args.dur,1000), args.sr)
    print("Wrote assets to", args.outdir)

if __name__=="__main__":
    main()
