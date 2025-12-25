# MIDI Quick Reference

**Status bytes (hex)**
- Note On: `0x90 | ch`  data1=note  data2=velocity
- Note Off: `0x80 | ch`
- Control Change: `0xB0 | ch`  data1=cc  data2=value
- Program Change: `0xC0 | ch`  data1=program
- Pitch Bend: `0xE0 | ch`  data1=LSB  data2=MSB (center=8192)

**Value ranges**
- Channels: 1‑16 (encoded 0‑15)
- CC numbers: 0‑119 (7‑bit)
- Values: 0‑127

**Serial‑MIDI on Uno (bridge on host)**
- Uno prints raw bytes over 115200 serial; host app bridges to virtual MIDI.

**DIN‑5 MIDI OUT (31250 baud)**
- Use `Serial` @ 31250 (MIDI library) on a hardware UART. Wiring: TX→220Ω→DIN pin 5; +5V→220Ω→DIN pin 4; GND→DIN pin 2.
