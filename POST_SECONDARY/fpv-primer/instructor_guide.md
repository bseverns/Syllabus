# Instructor guide

This guide assumes a post-secondary lab or studio context where students need enough rigor to operate hardware safely and discuss it precisely.

## Baseline assumptions

- students are working in pairs or trios
- the default rig is a BETAFPV Air65-class whoop with ELRS and analog video
- Betaflight Configurator is available on lab machines
- the course can stay bench-only if proof standards are not met

## Required teaching stance

Treat this repo as a systems literacy module, not a hype unit and not a race clinic.

Students should leave being able to:

- name the stack layers
- prove receiver, arming, and failsafe behavior
- capture one small dataset they actually trust
- explain why a relaunch is or is not justified

## Suggested room setup

- one bench station per group
- prop bin with clearly separated fresh and damaged props
- battery-safe charging area
- one projected Betaflight walkthrough station
- one quarantine area for damaged packs or grounded rigs

## Instructor prep checklist

Before the first meeting:

1. verify each Air65-class rig binds correctly to its assigned ELRS radio
2. confirm Betaflight connection on at least one student machine image
3. decide whether the course is bench-only, indoor-only, or may include outdoor work
4. print or duplicate the checklist and triage templates
5. define the local rule for who can authorize a relaunch after a crash

## What counts as proof

Students are not done because they "set it up."

Proof means they can show evidence for the following:

- receiver channels move as expected in Betaflight
- arming is intentional and not mapped by accident
- signal loss behavior was tested, not merely discussed
- the source signal in a mapping has defined semantics and a valid range
- crash inspection includes a specific relaunch or ground decision

## Common Air65 / ELRS failure patterns to watch for

- wrong receiver protocol selected after flashing or reset
- bind mismatch between radio model and receiver state
- students trusting RSSI alone when link quality is the more relevant field
- ducts or canopy shifted enough to change handling after minor crashes
- hair or debris in tiny motors
- damaged props treated as "good enough" because the craft still lifts

## Teaching moves that improve rigor

- ask students to narrate the stack before touching settings
- require screenshots, diffs, and written notes instead of oral memory
- separate "works" from "proven" in critique language
- stop the lab when students start theorizing before checking the first obvious layer

## When to stay bench-only

Keep the cohort bench-only when:

- students cannot perform the props-off ritual reliably
- failsafe has not been proven on the actual rig
- batteries are being handled casually
- students cannot distinguish control-link failure from video failure
- post-crash inspections are superficial

## Optional simulator block

If students are new to stick feel, add 20 to 30 minutes of simulator time before live-prop sessions. The simulator is not a substitute for hardware systems literacy, but it lowers the cognitive load when students first combine line-of-sight judgment, FPV view, and throttle control.
