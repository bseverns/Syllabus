# Protocol cheat sheet

## Serial
- bytes over USB
- needs framing (newlines, length prefixes, or binary packets)
- great for debugging + configuration

## I2C (preview)
- two-wire bus (SDA/SCL)
- addresses devices, used for sensors/displays

## SPI (preview)
- fast, chip-select based
- often used for displays, SD cards

## MIDI (optional)
- message-based control language for music tools
- common messages: CC, NoteOn/Off, Pitch Bend
