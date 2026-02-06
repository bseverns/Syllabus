# Troubleshooting (common)

- Serial ports: macOS `/dev/cu.usbmodem*`, Linux `/dev/ttyACM*`, Windows `COM*`
- If the device lags: you're printing too fast or blocking in `loop()`
- If MIDI doesn't appear: confirm a virtual port exists; install `python-rtmidi`
- If WebSerial fails: use Chrome/Edge and serve from localhost/HTTPS
