#!/usr/bin/env python3
import argparse, numpy as np, soundfile as sf

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("wav")
    args=ap.parse_args()
    x,sr=sf.read(args.wav, dtype="float32")
    if x.ndim>1: x=x.mean(axis=1)
    peak=float(np.max(np.abs(x)))
    rms=float(np.sqrt(np.mean(x*x)))
    dc=float(np.mean(x))
    print("sr:", sr, "samples:", len(x))
    print("peak:", peak, "rms:", rms, "dc:", dc)

if __name__=="__main__":
    main()
