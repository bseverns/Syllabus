# Week 1 - Ground School & First Connection

**Theme:** Fly first in the simulator, then learn what makes flight possible.
**Tuesday focus:** First VelociDrone hook, safety, parts, signal flow, and rules
**Thursday focus:** Betaflight connection, baseline backup, FC orientation, and simulator reps
**Class length:** Two 90-minute meetings

---

## Goals

By the end of the week, students will:

- Understand basic safety expectations for the workshop.
- Complete a first VelociDrone control attempt and name one flight habit to practice.
- Identify major components of a tiny whoop quadcopter.
- Explain the difference between the control link, the video link, and the power system.
- Connect their quad to Betaflight Configurator.
- Export and save a configuration backup.
- Verify that the FC orientation matches the physical quad.

---

## Instructor Prep

- Confirm all machines can open the Betaflight Configurator app or web tool.
- Test one demo quad from USB connection through backup export.
- Print or share `materials/Safety_Agreement_student.md`.
- Print or share `materials/Preflight_Checklist_student.md`.
- Print or share `materials/Betaflight_Config_Worksheet_student.md`.
- Print or post `materials/Whoop_Down_Learning_Board.md`.
- Read `resources/tinywhoop_basics_air65.md` so you can narrate one concrete signal path.
- Read `resources/us_indoor_outdoor_flight_rules.md` and decide whether this course is indoor-only or may include outdoor flight.
- Set up VelociDrone before students arrive, with a simple map and at least one radio/controller tested.

---

## Materials

- Student tiny whoops and radios
- Laptops/desktops with Betaflight access
- USB data cables, including spares known to carry data
- VelociDrone station or projected demo station
- Betaflight configuration worksheet
- Whoop down learning board
- Projector or large display
- Whiteboard or large paper for shared safety rules

---

## Tuesday Class - First Flight Hook, Parts & Rules

### 0:00-0:10 - Welcome & First Hook

- Introduce the 10-week Tuesday/Thursday structure.
- Explain that the course builds control first, then uses safety and technical work to make more flying possible.
- Show one short VelociDrone demo lap or crash-and-retry sequence.

### 0:10-0:30 - VelociDrone First Control Attempt

Students rotate through a quick first attempt, or watch a projected demo if stations are limited:

- arm or start the sim
- lift off
- try one straight move
- try one turn
- land or reset

Frame crashes as useful information. Ask students what felt hard: throttle, turning, orientation, or landing.

### 0:30-0:45 - Safety Agreement

- Establish the first safety rules:
  - Props off on the bench.
  - No arming in hands or near faces.
  - Goggles stay in the pilot area.
  - Crash means disarm first, then inspect.
- Have students read, discuss, and sign the safety agreement if your program uses one.
- Invite students to add one room-specific rule; write final rules visibly.
- Connect the rules to the simulator hook: the real room needs habits the simulator can practice without breaking props.

### 0:45-1:05 - Anatomy of a Tiny Whoop

- Have students hold quads with batteries unplugged.
- Point out:
  - frame and ducts
  - props and motors
  - AIO FC/ESC board
  - receiver and antenna
  - camera and VTX if present
  - battery lead and connector
- On an Air65-style example, show where the USB connector and any boot button/pads live.

### 1:05-1:20 - Three Systems, Not One Mystery

Use the board or projector to separate:

- **Power system:** battery -> FC/ESC board -> motors
- **Control system:** radio -> ELRS receiver link -> FC -> ESCs -> motors
- **Video system:** camera -> analog VTX -> goggles/receiver

Ask:

- What still works if video drops?
- What still works if the radio link drops?
- Which failures are safe to investigate on the bench?

### 1:20-1:30 - Indoor vs Outdoor Rules

- Explain that indoor flight is governed mostly by school, site, and safety rules.
- Explain that outdoor flight adds FAA, airspace, weather, site, and radio-equipment concerns.
- State the course default clearly: indoor-first unless the instructor has approved outdoor operations.

---

## Thursday Class - Betaflight Connection, Backup & Simulator Reps

### 0:00-0:10 - Safety Re-Entry

- Revisit the signed safety rules.
- Confirm today's bench rule: no battery and no props-on motor tests unless explicitly directed.
- Ask students to identify the USB connector and battery lead before opening laptops.

### 0:10-0:25 - Betaflight Tour

On the projector:

- Launch Betaflight Configurator.
- Show Connect/Disconnect.
- Briefly tour:
  - Setup
  - Configuration
  - Receiver
  - Modes
  - Motors
  - OSD
- Emphasize that the goal is controlled observation, not random slider changes.

### 0:25-1:05 - First Connections

Students:

1. Plug in the whoop by USB with no battery connected unless your hardware requires otherwise.
2. Confirm the correct port and click **Connect**.
3. On the Setup tab, gently tilt the quad and verify that the on-screen model moves the same way.
4. Note firmware target and version if visible.
5. Record the connection and board-orientation checks in the Betaflight configuration worksheet.

Circulate for:

- USB cable issues
- driver or permission issues
- confusing port names
- mismatched FC orientation

### 1:05-1:20 - Baseline Backup

Students:

1. Export a configuration backup.
2. Save it to a known location.
3. Use a clear filename such as `studentname-whoop1-baseline.json`.
4. Write down where the backup lives.
5. Add the file name and location to the Betaflight configuration worksheet.

If students cannot connect, pair them with a working rig so they still see the backup workflow.
If a student is blocked by cable, computer, or hardware issues, move them to the whoop-down learning board tasks instead of leaving them idle.

### 1:20-1:27 - Short Simulator Reps

Students complete one quick VelociDrone rep or observe a projected rep:

- one takeoff
- one controlled turn
- one landing or reset

Ask them to connect the sim behavior to the real control, power, and video systems they just named.

### 1:27-1:30 - Exit Ticket

Students answer:

- One part of the whoop I understand better now is...
- My baseline backup is saved at...
- One simulator control habit I need to practice is...

---

## Evidence of Learning

- Student signed or acknowledged the safety agreement.
- Student completed or observed a first VelociDrone control attempt.
- Student can name the power, control, and video systems.
- Student started the Betaflight configuration worksheet.
- Student saved a baseline backup or observed and documented the backup process with a partner.

---

## Notes & Variations

- If connection troubleshooting consumes the day, protect the safety and backup goals first.
- If simulator stations are limited, use projected demo reps and quick rotations rather than skipping the hook.
- If time remains, preview arming flags in the Setup tab without changing settings.
- For a no-real-flight first week, still use VelociDrone so students start building control vocabulary.
