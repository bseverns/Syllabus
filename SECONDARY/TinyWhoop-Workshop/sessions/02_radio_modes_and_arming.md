# Week 2 - Radio, Modes & Arming

**Theme:** Make the real radio match the control habits students are practicing.
**Tuesday focus:** Simulator control drills, radio link, Receiver tab, channel map, and AUX switches
**Thursday focus:** Modes, arming logic, props-off motor testing, and simulator gate practice
**Class length:** Two 90-minute meetings

---

## Goals

By the end of the week, students will:

- Bind or verify the bind between radio and whoop.
- Use simulator drills to connect stick movement to roll, pitch, yaw, and throttle.
- Explain that ELRS is the control link, not the FPV video link.
- Use the Receiver tab to confirm correct channel mapping.
- Identify roll, pitch, yaw, throttle, and AUX channels.
- Configure arming and a beginner-friendly flight mode.
- Perform safe arming and motor tests with props off.
- Complete one repeatable simulator drill using calm stick inputs.

---

## Instructor Prep

- Test your demo rig with a radio.
- Confirm binding, channel mapping, AUX switches, and arming behavior.
- Prepare a quick sketch of roll, pitch, yaw, throttle, and AUX channels.
- Decide which flight mode students should use first, usually Angle for beginners.
- Have a plan for students whose radios do not bind during class.
- Prepare a VelociDrone drill that isolates one axis at a time: straight line, turn, or figure-eight.

---

## Materials

- Student quads and radios
- Laptops with Betaflight Configurator
- USB data cables
- VelociDrone station or projected demo station
- Projector or whiteboard
- Small prop tools if props need to be removed

---

## Tuesday Class - Simulator Control & Receiver Tab

### 0:00-0:15 - Simulator Stick Warm-Up

Students run or observe a short drill:

- throttle: lift and settle
- yaw: point the nose intentionally
- roll/pitch: move through a simple line

Ask students to name which stick motion caused which aircraft motion.

### 0:15-0:25 - Safety Re-Center

- Revisit the bench rule: props off before any motor or arming test.
- Add the radio habit: radio on before battery; battery off before radio off.
- Ask students to point to their arming switch if they already know it.

### 0:25-0:40 - Binding & Receiver Types

- Explain that different whoops use different receiver protocols.
- Introduce **ELRS 2.4 GHz** as the control link for many beginner whoops.
- Separate control from video again:
  - ELRS carries commands.
  - Analog VTX carries camera video.
- Demo the signs of a healthy link on your hardware.

Students:

- Confirm that their radios are bound or work with you to bind them.
- If binding fails, join a partner with a working setup so they can continue the Receiver tab work.

### 0:40-1:10 - Receiver Tab Deep Dive

On the projector:

- Open the **Receiver** tab.
- Move each stick slowly.
- Name the axes:
  - Roll/Aileron
  - Pitch/Elevator
  - Yaw/Rudder
  - Throttle
- Show how a channel map such as AETR or TAER affects interpretation.

Students:

1. Open their own Receiver tab.
2. Move one stick at a time and verify the expected bar moves.
3. Flip switches and identify at least one AUX channel.
4. Note anything confusing in their tune log or notebook.
5. Compare the Receiver tab bars to what they felt in the simulator warm-up.

### 1:10-1:22 - Fixing Channel Confusion

- Help students correct channel map issues if needed.
- Emphasize that "moving bars" is not enough; each stick must move the correct axis.
- Have pairs check each other's stick response.

### 1:22-1:30 - Exit Ticket

Students answer:

- Which channel or AUX switch will probably become my arming switch?
- What is one sign that the radio link is not working?
- Which simulator movement helped me understand the Receiver tab?

---

## Thursday Class - Modes, Arming & Simulator Gate Practice

### 0:00-0:10 - Setup Check

- Confirm props are removed for any bench tests.
- Confirm radios are on and the correct model memory is selected.
- Review the difference between a switch being assigned and an aircraft being safe to arm.

### 0:10-0:40 - Modes Tab

On the projector:

- Open the **Modes** tab.
- Demonstrate:
  - ARM mode on a dedicated switch.
  - Angle mode for early flights.
  - Optional second mode such as Horizon or Acro Trainer if appropriate.

Students:

1. Assign ARM to a clear AUX range.
2. Assign Angle to a separate AUX range or default state.
3. Save and test switch behavior.
4. Say out loud which switch arms the quad.

### 0:40-1:05 - Arming Logic

- Show that Betaflight may refuse to arm for good reasons.
- Introduce arming flags as useful messages, not annoyances.
- Have students practice:
  - disarmed state
  - arm switch on
  - arm switch off
  - explaining what they expect before trying it

### 1:05-1:20 - Motors Tab Safety Demo

On the projector:

- Open the **Motors** tab on a props-off demo rig.
- Show the safety checkbox.
- Spin motors at low speed one at a time.
- Listen for normal vs rough motor sounds.

Students may test only under instructor supervision. Keep the focus on safe procedure, not throttle excitement.

### 1:20-1:27 - Simulator Gate Practice

Students try a simple gate or straight-line drill using the same calm arming/reset routine:

- start/reset
- lift
- pass through one gate or marker
- land/reset

Keep the goal clean control, not lap time.

### 1:27-1:30 - Exit Ticket

Students answer:

- What three conditions should be true before you arm?
- What should you do immediately after a crash?
- What simulator drill should I repeat before real flight?

---

## Evidence of Learning

- Student verifies correct stick motion in the Receiver tab.
- Student identifies an AUX switch.
- Student demonstrates or describes a safe props-off arm/disarm sequence.
- Student completes or explains one repeatable VelociDrone control drill.

---

## Notes & Variations

- If binding takes too long, protect Receiver tab understanding and move motor testing to Week 3.
- If technical setup slows down, keep the simulator station active so students still get useful control reps.
- If students are already experienced, add endpoint checking and failsafe discussion.
- Keep a written list of radio brand/protocol issues so repeated problems become a shared troubleshooting resource.
