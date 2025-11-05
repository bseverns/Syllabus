# Session 4 – Profiles, Troubleshooting & Flight Readiness

**Theme:** Leaving with a whoop that feels like yours.  
**Duration:** 90–120 minutes

---

## Goals

By the end of this session, students will:

- Save a “final” backup of their preferred tune.
- Recognize common arming flags and basic error states.
- Work through a structured troubleshooting process.
- Draft and practice a personal pre–flight checklist.
- Demonstrate safe, intentional operation of their whoop.

---

## Instructor Prep

- Prepare a demo rig with one or two intentional problems:
  - Wrong motor order or motor direction.
  - Mode set up incorrectly so it will not arm.
- Print or share `materials/Preflight_Checklist_student.md`.

---

## Materials

- Student quads and radios
- Laptops with Betaflight Configurator
- Indoor flight area
- Printed checklists or notebooks

---

## Schedule (example for 2 hours)

### 0:00–0:15 – Warm–Up & Status Check

- Ask students:
  - “How is your whoop flying after last time?”
  - “What setting change helped the most?”
- Have each student quickly connect to Betaflight to confirm:
  - Receiver is responding.
  - Modes look correct.
  - OSD elements are still where they left them.

### 0:15–0:35 – Final Backup & Profiles

Students:

1. Connect their whoop.
2. Save a new backup with a meaningful name:
   - e.g., `studentname-whoop1-final-tune.json`
3. Note which rate profile they are using as their default.
4. Optionally, take a screenshot of the PID / Rates tab.

Explain that this backup is like a “restore point” they can return to after future experiments.

### 0:35–1:05 – Troubleshooting Clinic

On the projector, use your intentionally broken demo rig:

1. Show a problem (e.g., the quad arm but flips immediately).
2. Ask students to hypothesize the cause.
3. Walk through a systematic process:
   - Check Setup tab for orientation.
   - Check Motors tab for correct motor numbering and direction.
   - Check Receiver and Modes tabs for correct switch behavior.
   - Check arming flags or warnings on the Setup tab.

Then, invite students to:

- Share any issues their own quads have had.
- Pair up to diagnose with your supervision.

Encourage them to narrate their reasoning:
- “I’m checking the Receiver tab first because…”
- “If it won’t arm, I’m going to look at the arming flags next…”

### 1:05–1:35 – Pre–Flight Checklist Drafting

Hand out or display `materials/Preflight_Checklist_student.md` as a template.

Students:

1. Customize the checklist for their own habits and hardware.
2. Include:
   - Before plugging in (radio on, area clear, battery check).
   - After plugging in (link verified, OSD info visible).
   - Before arming (modes correct, arming switch known).
   - After landing (battery unplugged, pack cooled, quad inspected).

Have a few students read aloud one line they added or changed.

### 1:35–1:55 – Demonstrations

If space and safety allow:

- Have each student perform a short demonstration:
  - Use their checklist.
  - Arm, take a brief controlled flight, and land.
  - Disarm and unplug safely.

If flight is not possible, they can:

- Walk through the checklist and show in Betaflight that everything is configured as expected.

### 1:55–2:00 – Closing Reflection

Invite students to share:

- One thing they now understand about Betaflight that felt mysterious before.
- One experiment they might try in the future (e.g., different rates, designing a new track, trying a simulator).

Thank them and encourage them to keep good backups and good habits as they keep flying.

---

## Notes & Variations

- If many students are still in the troubleshooting phase, devote more time to pair–work and less to flying.
- For more advanced groups, you can:
  - Introduce blackbox logging if their hardware supports it.
  - Explore more advanced tuning concepts or custom OSD layouts.
