# Session 2 – Radio, Modes & Arming

**Theme:** What your hands are saying to the drone.  
**Duration:** 90–120 minutes

---

## Goals

By the end of this session, students will:

- Bind or verify the bind between radio and whoop.
- Use the Receiver tab to confirm correct channel mapping.
- Configure arming and basic flight modes.
- Perform safe arming tests with props off.

---

## Instructor Prep

- Test your demo rig with a radio:
  - Confirm binding
  - Check channel mapping
  - Verify Modes tab behavior
- Prepare a short slide or whiteboard sketch explaining:
  - Roll, pitch, yaw, throttle
  - AUX channels as “extra switches”

---

## Materials

- Student quads and radios
- Laptops with Betaflight Configurator
- USB data cables
- Projector or whiteboard

---

## Schedule (example for 2 hours)

### 0:00–0:10 – Safety Re–Center

- Revisit safety rules from Session 1.
- Add one new, radio–specific rule:
  - “Radio on before battery; battery off before radio off.”

### 0:10–0:30 – Binding & Receiver Types

Brief talk/demo:

- Explain that different whoops use different receiver protocols.
- Show how your demo rig indicates a successful bind (LED behavior, Betaflight status).
- Model a simple binding process for your hardware.

Students:

- Confirm that their radios are bound to their whoops, or work with you to bind them.
- If binding fails for any student, pair them with a partner who has a working rig so they can still follow along in Betaflight.

### 0:30–1:00 – Receiver Tab Deep Dive

On the projector:

- Open the **Receiver** tab.
- Move each stick slowly; show the channel response:
  - Roll (Aileron)
  - Pitch (Elevator)
  - Yaw (Rudder)
  - Throttle
- Explain channel map (e.g., AETR vs TAER).

Students:

1. Open their own Receiver tab.
2. Verify that moving each stick does what they expect.
3. Identify one or more AUX channels that move when they flip a switch.

Help them adjust channel map if needed so sticks line up with the expected axes.

### 1:00–1:30 – Modes & Arming Logic

On the projector:

- Open the **Modes** tab.
- Demonstrate:
  - ARM mode on a dedicated switch.
  - A simple stabilized flight mode (Angle).
  - Optionally, a second mode like Horizon or Acro Trainer.

Students:

1. Assign ARM to an AUX channel and define a safe range (on/off).
2. Assign ANGLE mode to another AUX range.
3. Save and test:
   - With props off and only USB + battery if required by your hardware.

Reinforce:

- Do not arm on the bench with props installed.
- Always know which switch is your arming switch.

### 1:30–1:50 – Safe Motor Testing

On the projector:

- Open the **Motors** tab on your demo rig with props removed.
- Show how to:
  - Use the safety check box.
  - Spin individual motors at low speed.
  - Feel for vibration or weird sounds.

Students:

- Remove props if any are still installed.
- Briefly test motor spin–up with your supervision, focusing on:
  - Recognizing normal vs abnormal sounds.
  - Confirming that arming/disarming works as expected.

### 1:50–2:00 – Wrap & Exit Ticket

Ask students to:

- Demonstrate safe arming/disarming (props off) on the bench.
- Answer on a notecard or in a notebook:
  - “What three conditions should be true before you arm your whoop?”

Collect questions that surfaced (e.g., about specific radio brands) to address next time or in office hours.

---

## Notes & Variations

- If many students struggle with binding, consider grouping:
  - “Bound and working” students help others under your supervision.
- For time–limited classes, you can move Motors tab testing to Session 3 and just focus on Receiver + Modes today.
