# Parts map

Use this as the minimum viable parts-and-failures briefing for a modern FPV stack.

## 1. Frame

What it does:

- holds geometry, mounting, and structural alignment
- sets motor spacing and mechanical durability

Failure signs:

- cracked arms or ducts
- delamination, flex, or stripped mounting holes
- changing tune behavior after a crash

What breaks when it fails:

- alignment
- vibration profile
- trust in the rest of the stack

## 2. Motors and props

What they do:

- turn electrical power into thrust and control authority

Failure signs:

- bent shafts
- chipped props
- rough bearings
- hot motors
- desync, stutter, or uneven idle

What breaks when they fail:

- lift
- stability
- current draw assumptions

## 3. ESCs

What they do:

- translate FC motor commands into timed power for each motor

Failure signs:

- desync
- one motor not starting cleanly
- overheating
- burnt MOSFET smell
- inconsistent startup tones

What breaks when they fail:

- motor control
- safe arming
- confidence in the power stage

## 4. Flight controller (FC)

What it does:

- reads receiver input and sensors
- runs the control loop
- sends commands to ESCs
- hosts configuration, OSD, logging, and often telemetry functions

Failure signs:

- wrong orientation
- sensor drift
- random reboots
- USB instability
- arming flags you cannot clear

What breaks when it fails:

- the whole interpretation layer of the vehicle

## 5. Receiver (RX)

What it does:

- receives pilot commands from the radio link

Failure signs:

- no stick motion in Betaflight
- bad channel mapping
- low link quality
- unexpected failsafe

What breaks when it fails:

- pilot authority
- valid control assumptions

## 6. Camera and VTX

What they do:

- camera captures view
- VTX sends it to goggles or a receiver

Failure signs:

- black screen
- noisy image
- overheating
- wrong channel / band
- damaged antenna or pigtail

What breaks when they fail:

- situational awareness
- video evidence
- OSD visibility

## 7. Antennas

What they do:

- make radio and video systems usable instead of theoretical

Failure signs:

- poor range
- sudden breakup
- visible damage or missing strain relief

What breaks when they fail:

- link reliability

## 8. Battery, connector, and straps

What they do:

- provide energy and physical retention

Failure signs:

- puffing
- voltage sag
- hot connector
- torn lead
- battery ejection in a crash

What breaks when they fail:

- flight duration
- voltage stability
- fire safety margin

## 9. Optional systems

### GPS
- useful for navigation, rescue, or data overlays
- irrelevant to many bench-first workflows, but critical in some field contexts

### Blackbox storage
- dataflash, SD card, or serial logger
- essential when the teaching goal includes repeatable diagnosis

### Barometer / compass / extra sensors
- context dependent
- often noise sources if misunderstood

## Signal-chain summary

### Power path
Battery -> regulators / ESC power stage -> motors and electronics

### Control path
Radio -> receiver -> FC -> ESCs -> motors

### Video path
Camera -> VTX -> goggles / receiver

### Telemetry path
FC / receiver / sensors -> OSD, serial stream, blackbox, logs, exported data

## Teaching move

Ask students to point at each part and answer:

- what does it do?
- what fails if it disappears?
- how would I prove that failure on the bench?
