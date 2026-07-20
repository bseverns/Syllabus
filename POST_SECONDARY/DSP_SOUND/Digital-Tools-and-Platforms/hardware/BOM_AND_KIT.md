# Digital Tools and Platforms — Bill of Materials

Choose and freeze one baseline board before ordering. Quantities below support one team of two using the Uno-compatible minimum route; multiply by teams, then add the listed spares.

## Per-team core kit

| Item | Quantity | Notes |
| --- | ---: | --- |
| Arduino Uno/Nano-compatible board or documented local equivalent | 1 | Known logic voltage, ADC resolution, USB/Serial behavior, and EEPROM support |
| USB data cable | 2 | Charge-only cables are not substitutes |
| Full or half breadboard | 1 | Label power rails and note any split rails |
| Male-male jumper wires | 30 | Mixed lengths; use labels as well as color |
| 10k linear potentiometers | 4 | Capstone controls; one used from Week 3 onward |
| Momentary buttons | 4 | Capstone controls; active-low internal-pullup baseline |
| Standard LEDs | 6 | Three required for state feedback plus spares |
| 220–330 ohm LED resistors | 8 | Match LED/board safely; never omit current limiting |
| 10k resistors | 4 | Sensor divider/optional external bias experiments |
| Photoresistor or approved analog sensor | 1 | Potentiometer is the complete Week 5 fallback |
| CD4051B-compatible analog multiplexer | 1 | Exact datasheet and voltage compatibility required |
| 100nF ceramic capacitors | 4 | Local decoupling/noise experiments |
| Small removable labels | 1 sheet | Board ID, pins, cable, team, tested/needs-checking |
| Project base/enclosure material | 1 set | Cardboard/foam board is acceptable |

## Per-team optional extension kit

- Teensy 4.x or another locally verified native USB-MIDI board;
- approved addressable LED strip/ring, data resistor, bulk capacitor, power plan, and pinned library;
- alternate analog sensors with known voltage/interface requirements;
- CD4067-class 16-channel mux after the eight-channel baseline is proven;
- knobs, panel hardware, headers/connectors, and enclosure parts.

## Shared room equipment

- one multimeter per two teams;
- instructor computer and known-good board/cable;
- USB hub only if externally powered/approved and pretested;
- wire cutters/strippers and other host-approved hand tools;
- component organizer and `tested / needs checking / damaged or unknown` bins;
- printed board pin maps and exact mux datasheets;
- optional oscilloscope or logic analyzer for demonstration;
- loaner mice, headphones, and accessible input options for documentation/data work.

## Spares for each eight teams

- 2 boards, 6 USB data cables, 2 breadboards;
- 8 pots, 8 buttons, 12 LEDs, 20 LED resistors;
- 3 multiplexers, 20 capacitors, and 40 jumper wires;
- at least one fully built, labeled, known-good reference rig kept out of student circulation.

## Do not purchase until the board choice is frozen

Confirm logic voltage, ADC resolution, PWM pins, EEPROM/storage behavior, USB connector, Serial port permissions, native MIDI capability, driver needs, and available current. The instructor records all substitutions and updates pin maps/firmware constants before students receive kits.
