# EEPROM + LED Guide

- Use `EEPROM.get(addr, obj)` / `EEPROM.put(addr, obj)` (on AVR include `<EEPROM.h>`).
- Debounce writes; only write when values change.
- For status LEDs on Uno, prefer a simple bargraph (e.g., 8 LEDs via resistor network) to visualize scene/state/signal.
- Store: scene index, CC map, last speed/tempo, calibration constants.
