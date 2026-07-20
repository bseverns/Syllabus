# Digital Tools and Platforms — Facilitator Launch Guide

Use this with the syllabus, weekly sessions, firmware, notebooks, assignments, hardware documents, and project brief. The course is `GO-P` only after the exact local board/toolchain and every required bench build pass preflight.

## Freeze the baseline

Before enrollment, record:

- board model/revision, logic voltage, ADC resolution, PWM pins, EEPROM/storage, and USB capability;
- Arduino IDE/board package or PlatformIO versions;
- Python/Jupyter environment and Serial-port permission path;
- required route: core Arduino firmware + Serial;
- optional routes: native USB MIDI, addressable LEDs, alternate sensors, or expanded mux;
- approved power sources, hand tools, inspection gates, and emergency/stop procedure.

Do not mix board families during first delivery unless each has its own tested pin map and compiled firmware set.

## Mandatory preflight

1. Assemble one complete team kit from `hardware/BOM_AND_KIT.md`.
2. Confirm every USB cable carries data and label each board/cable pair.
3. Compile all 12 sketches for the exact baseline board.
4. Upload and bench-test every sketch using `hardware/WIRING_BASELINE.md`.
5. Capture a known-good Serial sample matching every contract in `firmware/README.md`.
6. Test logging, CSV paths, plots, save/reopen, and submission on a student machine.
7. Run the no-hardware route using saved logs and a de-energized pin map.
8. Verify the exact multiplexer datasheet/pinout and the Week 10 storage behavior.
9. Treat Week 11 USB MIDI as optional unless the exact board/USB mode and receiving host pass.
10. Run the integrated Week 12 bench checklist and keep a reference controller out of student rotation.

## Room and staffing

- one bench per pair with a named tray and board ID;
- instructor demo/repair bench separated from learner work;
- `tested / needs checking / damaged or unknown` component bins;
- clear power-off signal and visible inspection queue;
- device/logging zone and a separate wiring zone when space permits;
- one lead for up to 12 experienced learners; add an assistant for larger or novice cohorts, mux week, and integration week.

## Default 165-minute rhythm

| Time | Move |
| --- | --- |
| 0–15 min | Goal, vocabulary, safety/voltage check, and known-good behavior |
| 15–35 min | One short code/wiring/data demonstration |
| 35–65 min | Power-off build and inspection gate |
| 65–90 min | Flash, observe, and first Serial capture |
| 90–100 min | Power-down, break, and tray reset |
| 100–130 min | Controlled change and second capture |
| 130–150 min | Plot/test, peer explanation, and recovery check |
| 150–165 min | Save, inventory, power down, reflect, and name next action |

## Plain-language launch statement

> No previous electronics or Arduino experience is expected. We will build with power off, inspect before first power, change one thing, and use Serial data to see what the board is doing. A careful diagram or test is as important as a working device.

## Common-stuck and recovery guide

| Symptom | Next move |
| --- | --- |
| Board not visible | Confirm data cable, board/port selection, permissions, driver, and one known-good board/cable; move team to saved log work |
| Upload fails | Close Serial users, reset/reconnect, verify exact board/bootloader, then use reference binary/sketch route |
| Board resets or part heats | Disconnect using local procedure; check shorts, rail voltage, current draw, and conflicting outputs before reuse |
| Analog value floats/jumps | Confirm ground/reference/wiper, input range, wire length, and one known source before adding software smoothing |
| Serial data cannot parse | Confirm baud, line ending, framing, field count, and header/contract; preserve raw transcript |
| Firmware and wiring disagree | Stop; make the pin table authoritative and change one side deliberately |
| One learner takes over | Rotate builder, reader/pin checker, operator, and logger; only operator touches power/upload controls during a run |
| Hardware remains unavailable | Use de-energized build, paper protocol/state design, saved CSV, and code tracing with the same evidence rubric |

## Access and assessment

- Provide enlarged/high-contrast pin maps and tactile/physical organization support.
- Use labels plus wire colors; never rely on color alone.
- Allow pre-bent leads, partner-directed wiring, or de-energized roles.
- Provide screen-reader-friendly code/text, captioned demos, written steps, and saved data.
- Grade safe process, system reasoning, evidence, and reproducibility—not fine-motor speed, typing, prior ownership, or flashy enclosures.

## Launch evidence

Keep compiler results, board/tool versions, wiring photos/maps, measured voltages as required locally, Serial samples, notebook smoke-test results, failed/substituted components, actual timings, access routes, and the reference-controller bench checklist. Update the package before the next run.
