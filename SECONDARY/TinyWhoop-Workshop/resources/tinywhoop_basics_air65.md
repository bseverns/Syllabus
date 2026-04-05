# Tiny Whoop Basics Using an Air65-Style Example

This doc gives instructors and students one concrete reference platform for beginner discussions: a **65 mm brushless whoop** like the **BETAFPV Air65** with an **ELRS 2.4 GHz** control link and an **analog 5.8 GHz** FPV system.

Use it to explain what the parts are and how the signals move through the quad.

## What is a tiny whoop?

A tiny whoop is a very small quadcopter, usually built for:

- indoor flight
- short flights on 1S batteries
- low mass and ducted prop safety
- beginner practice, racing, or fast backyard laps

They are not toys in the "no consequences" sense. They are small aircraft with spinning props, batteries, radios, and configuration software.

## The main parts

### Frame and ducts

- The **frame** holds everything together.
- The **ducts** protect props, reduce wall strikes, and make indoor flying more forgiving.
- Cracks in the ducts or frame can change how the quad flies.

### Props

- Props turn motor power into lift and thrust.
- Bent, chipped, or loose props make the quad noisy, weak, or unstable.
- Props are consumable parts. Students should expect to replace them.

### Motors

- Brushless tiny-whoop motors spin the props.
- On an Air65-style build, each motor is controlled separately.
- Hair, dust, carpet fibers, or bent shafts can cause rough motor behavior after crashes.

### Flight controller (FC)

- The **flight controller** is the quad's brain.
- It reads pilot commands and sensor data, then decides how each motor should respond.
- Betaflight mainly talks to this board.

### ESCs

- **ESC** means electronic speed controller.
- ESCs take commands from the FC and drive the motors.
- In a whoop, the ESCs are usually built into the main board.

### 5-in-1 board

Many beginner whoops now use a **5-in-1** style board. That usually means one compact board handles several jobs:

- flight control
- ESCs
- OSD
- radio receiver functions or receiver integration
- VTX or video-related integration

Students should understand that one board can still contain multiple systems.

### Camera

- The FPV camera sees what the quad sees.
- Camera angle affects how fast the quad feels in flight.
- After a crash, camera angle often shifts before anything else visibly breaks.

### Analog VTX

- The **video transmitter (VTX)** sends camera video to goggles or a receiver.
- In an analog setup, the picture is low latency but not HD.
- The VTX is not the same thing as the control link.

### ELRS receiver link

- **ExpressLRS (ELRS)** is the radio-control link between the pilot's transmitter and the quad.
- It carries stick and switch commands.
- If the ELRS link fails, the quad may failsafe even if the video feed still looks fine.

### Antenna

- The antenna matters for both durability and signal quality.
- If an antenna is cut, pinched, or ripped loose, control or video performance can suffer immediately.

### Battery

- Tiny whoops usually run on **1S LiPo or LiHV batteries**.
- Battery condition affects punch, stability, and flight time.
- Puffy or damaged batteries should not go back into the flight line.

## The three main systems students should separate

### 1. Power system

Battery -> FC / ESC board -> motors

This system makes the quad move.

### 2. Control system

Pilot radio -> ELRS link -> FC -> ESCs -> motors

This system tells the quad what the pilot wants.

### 3. Video system

Camera -> analog VTX -> goggles / ground receiver

This system lets the pilot see from the quad's point of view.

Students often blur these together. Do not let them.

## Air65-style talking points

If you are teaching around a BETAFPV Air65-style whoop, these beginner-friendly points are useful:

- It is a **65 mm class brushless whoop** built for light, agile indoor flight.
- The product line uses an **Air Brushless Flight Controller (5IN1)** style board.
- The product page describes a **C03 FPV Micro Camera** and an adjustable camera angle.
- BETAFPV support materials for the Air65 Champion mention **ELRS 2.4G**, a default **analog VTX** frequency point, and a default **25 mW** VTX output.

Do not teach students to memorize a spec sheet. Teach them to inspect and verify their own actual hardware.

## Questions students should be able to answer

- Which part makes lift?
- Which part sends my stick commands?
- Which part sends video to goggles?
- Which failures are safe to troubleshoot on the bench?
- Which failures mean "do not fly again until checked"?
