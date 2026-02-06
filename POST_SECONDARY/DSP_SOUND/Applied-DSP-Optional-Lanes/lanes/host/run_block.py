#!/usr/bin/env python3
import argparse, numpy as np, soundfile as sf

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--block", required=True, choices=["waveshaper","compressor"])
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", dest="outp", required=True)
    args=ap.parse_args()

    x,sr=sf.read(args.inp, dtype="float32")
    if x.ndim==1: x=x[:,None]

    if args.block=="waveshaper":
        from dsp.effects.waveshaper import process
        y=np.stack([process(x[:,ch], drive=2.0, mix=1.0, post=0.6, mode="tanh") for ch in range(x.shape[1])], axis=1)
    else:
        from dsp.dynamics.compressor import Compressor
        comp=Compressor(sr, threshold_db=-18.0, ratio=4.0, attack_ms=10, release_ms=120)
        ys=[]
        for ch in range(x.shape[1]):
            yy,_=comp.process(x[:,ch])
            ys.append(yy)
        y=np.stack(ys, axis=1)

    sf.write(args.outp, y, sr)
    print("Wrote", args.outp)

if __name__=="__main__":
    main()
