# Week 01 — Hello, board (blink + serial window)

## Goals
- Upload firmware successfully and confirm your toolchain is real.
- Use Serial as an observation window, not a magic spell.
- Capture a log and plot it in Python.

## Session arc (timed)
1. Warm-up (10 min): what’s the smallest thing a computer can do that still feels alive?
2. Mini-lecture (20–30 min): pins, voltage, boot/reset, Serial as a wire-level diary
3. Build + flash (40–60 min): flash Week01 sketch; verify LED + Serial output
4. Observe + log (20 min): log 10–30s to CSV; plot basic results
5. Share-out (15 min): students show port name + one failure they hit
6. Close (10 min): set the rhythm: wire → flash → log → commit

## Prep (instructor)
- Verify at least one board works on the classroom machines.
- Have spare USB data cables.
- Decide how students will find serial ports on their OS.
- Project the [Arduino Uno orientation reference](../../../../SECONDARY/robotic-vibes/assets/hardware-references/arduino-uno.jpg) while naming the local board's USB connector, reset button, and headers; its [CC BY 2.0 attribution](../../../../SECONDARY/robotic-vibes/assets/hardware-references/README.md) is maintained with the asset.

## Links
- `firmware/week01_blink_hello/`
- `labs/week01_serial_basics.ipynb`
- `assignments/hw01_setup.md`
