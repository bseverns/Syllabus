#!/usr/bin/env python3
"""Generate simple audio samples for labs.

Creates wav files in `data/audio_samples/`:
- sine_440.wav
- square_440.wav
- noise.wav
"""
from pathlib import Path
import numpy as np
import soundfile as sf

OUT = Path(__file__).resolve().parents[1] / "data" / "audio_samples"
OUT.mkdir(parents=True, exist_ok=True)

def norm(x):
    m = np.max(np.abs(x))
    return x / m if m > 0 else x

def main():
    sr = 48000
    dur = 2.0
    t = np.arange(int(sr*dur)) / sr

    sine = np.sin(2*np.pi*440*t)
    square = np.sign(sine)
    noise = np.random.randn(len(t)) * 0.2

    sf.write(OUT / "sine_440.wav", norm(sine), sr)
    sf.write(OUT / "square_440.wav", norm(square), sr)
    sf.write(OUT / "noise.wav", norm(noise), sr)
    print(f"Wrote samples to: {OUT}")

if __name__ == "__main__":
    main()
