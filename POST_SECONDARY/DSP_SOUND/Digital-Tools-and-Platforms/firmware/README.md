# Firmware Baseline

Each folder contains one Arduino-style sketch matching the syllabus. The minimum baseline uses core Arduino APIs and targets Uno/Nano-style 5V boards with a 10-bit ADC unless the sketch says otherwise. Adapt pin numbers, ADC resolution, voltage, USB mode, and EEPROM behavior only after checking the exact local board.

| Week | Sketch | Serial contract |
| --- | --- | --- |
| 1 | `week01_blink_hello` | `t_ms,ledState` |
| 2 | `week02_button_debounce` | `t_ms,rawPressed,debouncedPressed` |
| 3 | `week03_pot_pwm` | `t_ms,raw,smoothed,pwm` |
| 4 | `week04_metronome` | `t_ms,tick,interval_ms` |
| 5 | `week05_sensor_threshold` | `t_ms,raw,active` |
| 6 | `week06_serial_protocol` | `DATA,t_ms,analog,led`; commands documented in sketch |
| 7 | `week07_mux_scan` | `t_ms,channel,value` |
| 8 | `week08_led_feedback` | `t_ms,state,raw` |
| 9 | `week09_state_machine` | `EVENT,MODE,state` and `DATA,t_ms,state,raw` |
| 10 | `week10_calibration_eeprom` | `t_ms,raw,mapped,min,max` |
| 11 | `week11_usb_midi` | `MIDI,CC,number,value,channel`; optional Teensy USB MIDI |
| 12 | `week12_controller` | `BUTTON,...` and `KNOB,...` event records |

## Safety and verification

- Power off before wiring changes.
- Match local logic/ADC voltage; never assume Uno wiring applies to a 3.3V board.
- Use current-limiting resistors with discrete LEDs.
- Verify the exact multiplexer pinout from its datasheet.
- Back up EEPROM/configuration before experimenting with persistence.
- Compile every sketch for the chosen board, then test on one instructor bench before student use.
- The Week 11 Serial route is required; USB MIDI is optional and board/toolchain-specific.
