# Design Patterns (embedded instruments)

## 1) Cadence
Establish a stable rhythm:
- sample inputs at a fixed rate (e.g., 1 kHz for buttons, 200 Hz for knobs)
- send outputs at a capped rate (e.g., 100 Hz MIDI/Serial)
- update LEDs at a lower priority (e.g., 60 Hz)

## 2) Separate concerns
- read inputs → generate events
- process events → update state
- render outputs → protocol + LEDs

## 3) Define loss policies
If overwhelmed, decide what you drop:
- drop redundant knob updates first
- never drop button edges if you can help it

## 4) Make failure legible
- print INFO banner
- maintain error codes
- provide a reliable factory reset
