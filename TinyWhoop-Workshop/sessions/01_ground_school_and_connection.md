# Session 1 – Ground School & First Connection

**Theme:** Meet the brain of your whoop.  
**Duration:** 90–120 minutes

---

## Goals

By the end of this session, students will:

- Understand basic safety expectations for the workshop.
- Identify major components of a tiny whoop quadcopter.
- Connect their quad to Betaflight Configurator.
- Export and save a configuration backup.
- Verify that the FC orientation matches the physical quad.

---

## Instructor Prep

- Confirm all machines can open the Betaflight Configurator app / web tool.
- Test one demo quad from USB connection through backup export.
- Print copies of `materials/Preflight_Checklist_student.md` (optional) so students can start marking their own habits.

---

## Materials

- Student tiny whoops and radios
- Laptops/desktops with Betaflight access
- USB data cables (plus a few spares)
- Projector or large display
- Whiteboard or large paper for safety rules

---

## Schedule (example for 2 hours)

### 0:00–0:15 – Welcome & Safety Brief

- Introduce the workshop and overall arc of the four sessions.
- Establish safety as the first priority:
  - “Props off on the bench.”
  - No arming in your hands or near faces.
  - Goggles stay in the pilot area.
- Invite students to help refine the safety list; write it visibly in the room.

### 0:15–0:30 – Anatomy of a Tiny Whoop

- Have students hold their quads (with batteries unplugged).
- Point out:
  - Frame
  - AIO FC/ESC
  - Motors & ducts
  - Receiver and antenna
  - VTX/camera (if present)
  - Battery leads and connector
- Show on your demo rig where the USB connector and any boot button/pads live.

### 0:30–0:45 – Meet Betaflight Configurator

On the projector:

- Launch Betaflight Configurator.
- Show the Connect / Disconnect button.
- Briefly tour:
  - Setup tab
  - Configuration tab
  - Receiver tab
  - Modes tab
  - Motors tab
- Emphasize: we’ll move slowly and always aim for understanding, not random slider–dragging.

### 0:45–1:20 – First Connections (Hands–On)

Students:

1. Plug in their whoop via USB (no battery yet).
2. Confirm the correct port and click **Connect**.
3. On the Setup tab, gently tilt the quad and verify that the on–screen model moves in the same directions.
4. Export a configuration backup and save it to a known location:
   - Suggest a simple naming scheme like: `studentname-whoop1-baseline.json`.

Circulate to help with:

- USB cable issues
- Driver / permission hiccups
- Identifying the correct firmware target & version

### 1:20–1:40 – Guided Reflection & Quick Share

- Ask a few students:
  - “What did you notice inside Betaflight that you weren’t expecting?”
  - “What part of the quad’s anatomy is still confusing?”
- If time permits, let one or two students share their backup file names and where they stored them; reinforce backup habits.

### 1:40–2:00 – Wrap & Exit Ticket

- Ask students to write a one–sentence reflection:
  - “One thing I learned about my whoop today is…”
- Make sure every student:
  - Has at least one saved backup.
  - Knows where they saved it.
  - Can reconnect to Betaflight without assistance.

---

## Notes & Variations

- If time is short, prioritise:
  - Safety culture
  - First connection
  - Backup export

- If time runs long, you can:
  - Demonstrate the Motors tab with props off.
  - Show how arming flags appear in the Setup tab when things aren’t ready.
