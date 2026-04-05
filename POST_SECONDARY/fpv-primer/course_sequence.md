# fpv-primer course sequence

Use this when the repo needs to function as a short post-secondary module instead of a loose reading list.

## Format

- 5 sessions
- 2 to 3 hours each
- bench-first, with field work only after proof gates are passed
- baseline rig: BETAFPV Air65-class whoop with ELRS and analog video

## Session 1: stack literacy and safety doctrine

Focus:

- what FPV is as a system
- parts map and failure layers
- props-off discipline
- indoor versus outdoor operating assumptions

Read:

- `docs/00-what-is-fpv.md`
- `docs/01-safety-and-props-off.md`
- `docs/02-parts-map.md`
- `docs/13-us-operations-and-radio-compliance.md`

Artifacts:

- annotated parts map
- signed props-off / launch discipline acknowledgment
- short written narration of power, control, video, and telemetry paths

## Session 2: Air65 + ELRS minimum viable setup

Focus:

- Betaflight orientation and receiver confidence
- ELRS link proof
- modes, arming, and failsafe
- OSD choices that help decisions instead of decorate the feed

Read:

- `docs/03-build-checklist.md`
- `docs/04-betaflight-minimum-viable-setup.md`

Run:

- `labs/lab00-bench-sim.md`
- `labs/lab03-elrs-link-and-failsafe-proof.md`

Artifacts:

- completed `templates/air65-bench-proof-checklist.md`
- Betaflight screenshots or diff
- one paragraph describing what was proven and what is still unproven

## Session 3: telemetry semantics and capture

Focus:

- what counts as telemetry
- valid ranges, units, and state dependence
- short capture workflow
- bench replay as a debugging tool

Read:

- `docs/05-telemetry-exports.md`
- `docs/06-telemetry-semantics.md`
- `docs/08-bench-replay-lab.md`

Run:

- `labs/lab01-telemetry-to-midi.md`

Artifacts:

- semantics table for at least three signals
- one replayable capture
- one short log using `templates/flight-log-template.md`

## Session 4: mapping as composition

Focus:

- conditioning and shaping
- dropout behavior
- why one stable signal is worth more than many noisy ones
- comparison of mappings against the same source data

Read:

- `docs/07-mapping-cookbook.md`
- `docs/10-capture-and-obs.md`

Run:

- `labs/lab02-mapping-as-composition.md`

Artifacts:

- one completed `templates/mapping-sheet.md`
- three named mapping presets from one source signal
- one short A/B or A/B/C capture

## Session 5: troubleshooting, maintenance, and critique

Focus:

- symptom-first troubleshooting
- post-crash triage
- relaunch decisions
- communicating findings with evidence

Read:

- `docs/09-troubleshooting-tree.md`
- `docs/14-maintenance-and-post-crash-triage.md`
- `docs/11-glossary.md`

Run:

- `labs/lab04-post-crash-triage-and-relaunch.md`

Artifacts:

- completed `templates/post-crash-triage-sheet.md`
- troubleshooting narrative tied to a concrete symptom
- final portfolio bundle:
  - checklist
  - config export or screenshots
  - capture
  - mapping sheet
  - session log

## Proof gates

Do not move students into live-prop or outdoor work until they can demonstrate:

1. props-off ritual without prompting
2. correct narration of the control and failsafe path
3. a believable ELRS link proof
4. a documented relaunch decision after inspection
5. one replayable telemetry artifact

## Optional extensions

- add a simulator warm-up block before Session 2 if students are new to stick feel
- add a blackbox analysis session if the FC and storage support it
- add a field operations session only after the proof gates are met
