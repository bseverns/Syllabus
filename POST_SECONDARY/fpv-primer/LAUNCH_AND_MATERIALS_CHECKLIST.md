# FPV Systems Primer — Launch and Materials Checklist

This checklist packages the five-session sequence for supervised post-secondary delivery. It does not authorize flight. Local policy, site approval, instructor signoff, current law, and the actual equipment control every live-prop activity.

## Choose the delivery boundary

Mark one before enrollment:

- **Bench-only:** props remain removed for the entire course. This is a complete delivery path.
- **Indoor micro-flight:** adds simulator and supervised whoop flight after every proof gate.
- **Field-capable:** adds a separate approved operating framework, airspace/site review, radio plan, pilot requirements, and weather/emergency plan.

When any requirement is unresolved, use bench-only. Do not improvise a flight block because the hardware appears to work.

## Materials per team of 2–3

- one uniquely labeled whoop-class teaching rig and manufacturer documentation;
- one assigned, correctly configured transmitter/radio;
- one Betaflight-compatible computer, data cable, charger, and approved software image;
- one current-limiting device/smoke stopper appropriate to the rig;
- eye protection for anyone near intentional motor-output tests;
- one nonflammable battery-handling surface and approved 1S charging/storage system;
- small tool/inspection kit, spare known-good props, and parts containers;
- printed or private digital copies of the bench-proof checklist, flight/session log, mapping sheet, and crash-triage sheet.

For the room:

- instructor-controlled battery charging/storage area and damaged-pack quarantine process;
- `props off / grounded / bench-proven / flight-authorized` labels;
- fire/emergency equipment required by the host's battery-safety plan;
- projected instructor station with a known-good rig and saved baseline configuration;
- safe motor-test enclosure or equivalent local procedure if motor output is tested;
- simulator stations for any cohort new to stick control;
- approved indoor flight zone only when live-prop work is in scope.

## Instructor preflight

- Inventory rig, radio, battery, charger, cable, firmware, and software versions by team.
- Back up every known-good configuration before students connect.
- Confirm the official Betaflight receiver, arming, and failsafe guidance for the installed version.
- Perform the entire props-off bench checklist on the instructor rig.
- Verify that signal-loss behavior is understood and tested with props removed.
- Test capture, export, replay, MIDI monitor, file naming, and storage on a student machine.
- Write the local battery response, power authority, grounding, and relaunch rules.
- Recheck current FAA, FCC, site, institutional, and insurance requirements before any flight block.
- Prepare paper parts maps, screenshots, sample configuration exports, and recorded telemetry for equipment downtime.

## Default 150-minute rhythm

| Time | Move |
| --- | --- |
| 0–15 min | Roles, stop conditions, goal, and proof required today |
| 15–35 min | Instructor demonstration on a known-good rig or replay dataset |
| 35–70 min | Team bench/lab work with props-off check visible |
| 70–80 min | Power-down, battery/room check, and break |
| 80–120 min | Second proof round, replay, mapping, or troubleshooting |
| 120–140 min | Artifact completion and instructor proof gate |
| 140–150 min | Power-down, inventory, grounding/relaunch status, and next step |

## Evidence by session

| Session | Minimum evidence |
| --- | --- |
| 1 — stack/safety | Annotated parts map, safety acknowledgment, and narrated power/control/video/telemetry paths |
| 2 — configuration proof | Completed bench-proof checklist, saved configuration/diff, and proven-versus-unproven note |
| 3 — telemetry | Defined signal semantics, replayable capture, and session log |
| 4 — mapping | Mapping sheet, three controlled variants or one stable mapping, and comparison note |
| 5 — troubleshooting/critique | Symptom-first narrative, triage or recovery decision, and portfolio bundle |

## Roles

Rotate `operator`, `observer/logger`, and `power authority`. Only the named power authority connects or disconnects a battery during a test. An instructor—not a student checklist or software screenshot—controls advancement to motor or flight activity.

## No-hardware and low-tech-exposure route

A student may complete the systems-learning target with a de-energized parts rig, printed screenshots, known-good configuration export, and recorded telemetry. They can identify the stack, annotate settings, rehearse checklists, compare replay mappings, and make grounding decisions without powering or flying a craft.

Use plain language before acronyms:

- **flight controller (FC):** the small computer coordinating the craft;
- **receiver (RX):** the part receiving control data from the radio;
- **video transmitter (VTX):** the part sending camera video;
- **control link:** the radio path used to command the craft;
- **telemetry:** reported measurements or state information;
- **failsafe:** the planned response when the control link is lost;
- **arming:** entering a state where motor output can be enabled;
- **configuration backup/diff:** a saved record of settings used for recovery or comparison.

Say this on Day 1:

> Prior flight experience is not expected. Calm proof, clear notes, and knowing when to stop matter more than speed or confidence. You may learn from a de-energized rig or recorded dataset while a hardware problem is resolved.

## Stop and recovery rules

Stop, disconnect only according to the local power procedure, and alert the instructor for unexpected heat, odor, smoke, battery damage, unexplained rebooting, unintended motor output, uncertain failsafe, mismatched control movement, damaged wiring, or a test plan that is no longer clear.

When hardware or software fails, preserve the state, label the rig `grounded`, record the symptom, and move the team to a known-good replay/case dataset. Do not borrow another team's flight-authorized rig or change multiple settings to “see what happens.”
