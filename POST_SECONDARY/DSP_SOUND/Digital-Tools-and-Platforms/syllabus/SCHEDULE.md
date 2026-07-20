# 12-Week Schedule

## Week 1 — Hello, board
- Blink, Serial print, reading the console
- Firmware: `firmware/week01_blink_hello/`
- Lab: `labs/week01_serial_basics.ipynb`
- HW: `assignments/hw01_setup.md`

## Week 2 — Buttons and debouncing
- Digital input, pullups, debounce as a *design choice*
- Firmware: `firmware/week02_button_debounce/`
- Lab: `labs/week02_debounce_analysis.ipynb`
- HW: `assignments/hw02_buttons.md`

## Week 3 — Analog inputs (pots) + mapping
- AnalogRead, scaling, deadband, smoothing
- Firmware: `firmware/week03_pot_pwm/`
- Lab: `labs/week03_analog_mapping.ipynb`
- HW: `assignments/hw03_analog.md`

## Week 4 — Timing without delay
- millis(), tick loops, scheduling
- Firmware: `firmware/week04_metronome/`
- Lab: `labs/week04_timing_jitter.ipynb`
- HW: `assignments/hw04_timing.md`

## Week 5 — Sensors + thresholds
- photoresistor / distance sensor, hysteresis
- Firmware: `firmware/week05_sensor_threshold/`
- Lab: `labs/week05_thresholds.ipynb`
- HW: `assignments/hw05_sensors.md`

## Week 6 — Serial protocol as a contract
- framing, parsing, commands
- Firmware: `firmware/week06_serial_protocol/`
- Lab: `labs/week06_protocol_design.ipynb`
- HW: `assignments/hw06_protocol.md`

## Week 7 — Multiplexing (more inputs than pins)
- CD4051/4067 style; scanning patterns; settling time
- Firmware: `firmware/week07_mux_scan/`
- Lab: `labs/week07_mux_scan.ipynb`
- HW: `assignments/hw07_mux.md`

## Week 8 — LED feedback systems
- State-driven discrete LEDs; optional locally preflighted addressable-LED extension
- Firmware: `firmware/week08_led_feedback/`
- Lab: `labs/week08_led_design.ipynb`
- HW: `assignments/hw08_leds.md`

## Week 9 — State machines + modes
- interfaces that remember, mode switching
- Firmware: `firmware/week09_state_machine/`
- Lab: `labs/week09_state_machines.ipynb`
- HW: `assignments/hw09_states.md`

## Week 10 — Calibration + persistence
- calibration routines, storing values (EEPROM)
- Firmware: `firmware/week10_calibration_eeprom/`
- Lab: `labs/week10_calibration.ipynb`
- HW: `assignments/hw10_calibration.md`

## Week 11 — MIDI (optional track)
- CC + Note messages, mapping controls to messages
- Firmware (Teensy recommended): `firmware/week11_usb_midi/`
- Lab: `labs/week11_midi_basics.ipynb`
- HW: `assignments/hw11_midi.md`

## Week 12 — Build week
- assemble a small controller (4 knobs + 4 buttons + LEDs)
- Project: `project/PROJECT_BRIEF.md`
- Firmware baseline: `firmware/week12_controller/`
- HW: `assignments/hw12_build.md`
- Demo + critique
