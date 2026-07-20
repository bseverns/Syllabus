# Choir Divider — Facilitator Launch Checklist

This lab remains `PILOT` until an experienced facilitator physically builds and verifies the exact local version. Use this checklist to make that verification reproducible and to support a supervised first delivery.

## Delivery boundary

- 2 sessions × 90–120 minutes
- one 5V logic bench per pair
- solderless, instructor-approved AE Modular BRAEDBOARD or equivalent setup
- no mains wiring, battery modification, or connection to an unverified external voltage
- headphones or conservative monitor level for patch listening

The complete minimum build is an external known-good clock into the CD4017, a visible counting output, one early-reset cycle, and three patchable rhythmic outputs. The internal 555 and CD40106 cleanup stages are extensions.

## Physical verification before enrollment

Using the exact local boards, IC variants, power system, jacks, and patch destination:

1. Inventory and label every part from `parts/parts-list.md`.
2. Build the external-clock minimum path from power-off state.
3. Measure +5V at the CD4017 power pins and confirm ground before inserting/applying clock.
4. Prove Q0–Q9 count in order with the LED and series resistor.
5. Prove Q3 reset produces the repeating Q0–Q2 three-step cycle.
6. Prove Q4 and Q5 produce four- and five-step cycles.
7. Prove the PATTERN diode-OR node returns low through its pull-down.
8. Patch each intended output into the exact destination module and confirm safe, useful behavior.
9. Build and verify the optional 555 and 40106 paths separately if students will use them.
10. Photograph the known-good build, record measured voltages, list substitutions, and save one working patch diagram.

Do not move the offering to `GO-P` until this checklist has been completed and the first delivery confirms timing, parts quantities, and common failure points.

## Room and materials prep

- one labeled tray per pair using the exact quantities in `parts/parts-list.md`;
- power kept off until rail orientation and IC placement are inspected;
- separate `tested`, `needs checking`, and `damaged/unknown` bins;
- projected pin-accurate netlist and 555 layout;
- printed student guide, worksheet, node-labeling exercise, and patch recipes;
- one de-energized parts/diagram station for learners waiting on hardware;
- one known-good external clock and one known-good audio/visual destination;
- eye protection where required by local bench policy and a clear drink-free work zone.

## Default session flow

### Session 1 — Make time visible

- 0–10: welcome, plain-language signal path, and power-off rule
- 10–25: identify rails, IC notch/pin 1, resistor/LED/diode orientation
- 25–45: build and inspect power/decoupling with power off
- 45–55: facilitator measurement gate, then power down
- 55–65: break and tray reset
- 65–95: add external clock and CD4017 control connections
- 95–110: count outputs with LED and record evidence
- 110–120: power down, photograph, worksheet, inventory

### Session 2 — Turn steps into groove

- 0–15: rebuild/inspect last known-good state
- 15–35: expose three Q outputs and verify one at a time
- 35–55: add Q3 early reset and prove the three-step cycle
- 55–65: break and power-down check
- 65–90: patch recipe test at conservative level
- 90–105: optional pattern OR, internal clock, or cleanup extension
- 105–120: recording, diagram, reflection, power down, inventory

## Plain-language opening

Say this:

> You do not need electronics or music-synthesis experience. We will build one named node at a time with power off, ask for an inspection before power, and use a light before we use sound. Careful measurement matters more than speed.

Shared words:

- **clock:** a repeating high/low pulse;
- **counter:** a chip that advances to the next output on each clock edge;
- **output/Q step:** the counter pin active at that moment;
- **reset:** a signal that returns the counter to Q0;
- **division/cycle length:** how many visible steps occur before repetition;
- **decoupling capacitor:** a nearby part that helps keep chip power stable;
- **pull-down resistor:** a connection that gives a signal a clear low state when nothing drives it;
- **node:** connected points treated as one electrical location.

## Roles and access

Rotate `builder`, `reader/pin checker`, and `meter/worksheet recorder`. A learner may complete the conceptual target with the de-energized board, node map, LED observations, patch design, or recorded reference signals.

- Use pin numbers and physical landmarks; do not rely on wire color alone.
- Read each connection aloud and provide enlarged pin maps.
- Offer pre-bent leads or assistance placing small parts.
- Do not assess fine-motor speed, previous synthesis vocabulary, or solo troubleshooting.

## Stop and recovery guide

Power down immediately for heat, odor, unexpected voltage, an IC inserted backward, uncertain rail orientation, unintended always-high output, or unclear wiring.

| Symptom | Power-off check |
| --- | --- |
| No count | Power pins, pin 13 low, pin 15 low, then clock at pin 14 |
| Multiple/unsteady steps | Decoupling, short clock wiring, and optional 40106 cleanup |
| Reset length is wrong | Confirm the reset source: Q3 = 3 visible steps, Q4 = 4, Q5 = 5 |
| Pattern stays high | Verify diode direction and 100k PATTERN pull-down |
| Sound patch misbehaves | Return to LED proof and the instructor's known-good destination |
| Team loses the working state | Restore the reference photo/node checklist; change one connection at a time |

## Pilot evidence

Record the platform/IC variants, measured rail voltage, clock source, successful reset lengths, patch destinations, build time per stage, failed/substituted parts, access supports, photographs, and all changes required before another run.
