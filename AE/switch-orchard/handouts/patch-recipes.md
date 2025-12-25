# Patch recipes — Switch Orchard (AE Modular)

## 1) Rotating modulation (CV)
- Put 4 different LFOs/envelopes into X0–X3
- Z → a destination (filter, VCA, pitch, etc.)
- Scanner mode: clock advances which modulation source is active

## 2) Audio texture switch
- Put 2–4 audio sources into Xn
- Z → VCA/mixer
- Manual mode: perform a “DJ cross-route” (hard cuts, not fades)

## 3) One source, many destinations (demux)
- Put audio/CV into Z
- Take outputs from several Xn into different destinations
- Scan which destination is currently receiving the signal

## 4) Rhythm distributor
- Put a trigger stream into Z
- X0–X3 go to different drum hits
- Scanner makes the same rhythm “walk” across voices
