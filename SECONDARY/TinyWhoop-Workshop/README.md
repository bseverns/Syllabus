# Tuning Tiny Whoops: A Betaflight Configurator Workshop

This packet contains a 10-week secondary workshop for high school students learning to configure, maintain, and race **tiny whoop** quadcopters using **Betaflight Configurator**.

The course is designed for **10 Tuesday/Thursday pairs**. Each class meeting is **90 minutes**, for a total of **20 class meetings**.

The emphasis is on:

- Safety first
- Control and practice from the first week, using VelociDrone as the low-risk playground
- Understanding what each part of the whoop actually does
- Understanding indoor vs outdoor rules and responsibilities
- Crash recovery and basic maintenance habits
- Config literacy and good backup habits
- Simulator practice in **VelociDrone** before, during, and between real-flight blocks
- Building flight feel through modes, rates, OSD, and repeatable routines
- Building toward early simulator race challenges and a final classroom race with safe habits and predictable machines

## Folder structure

- `SYLLABUS.md` - high-level overview, 10-week schedule, learning goals
- `INSTRUCTOR_NOTES.md` - safety, logistics, pacing, and implementation notes
- `sessions/` - weekly plans; each file contains a Tuesday class and a Thursday class
- `materials/` - printable checklists, worksheets, signoff cards, rubrics, and student-facing handouts
- `resources/` - reference docs on basics, rules, simulator drills, and maintenance
- `LICENSE` - MIT license for adapting this material

## How to use this packet

1. Read `SYLLABUS.md` to understand the full 10-week arc.
2. Review `INSTRUCTOR_NOTES.md` and adapt safety/admin language to local policies.
3. Read the reference docs in `resources/` before teaching outdoor rules, simulator practice, or hardware-specific examples.
4. Use each file in `sessions/` as one week of instruction:
   - Tuesday: introduce, model, and set up the skill.
   - Thursday: practice, troubleshoot, document, and apply the skill.
5. Print or duplicate the files in `materials/` for student use.

## Core student artifacts

- `materials/Betaflight_Config_Worksheet_student.md` - required record for backup, orientation, receiver, modes, failsafe, motors, OSD, and rates
- `materials/Flight_Readiness_Card.md` - teacher signoff before real flight or race readiness
- `materials/Troubleshooting_Decision_Tree.md` - printable decision path for connection, binding, arming, failsafe, rough flight, and video issues
- `materials/Student_Tune_Log_Template.md` - reusable record for settings, simulator results, real-flight notes, and next changes
- `materials/Competency_Grid.md` - novice/developing/ready/mentor assessment grid
- `materials/Whoop_Down_Learning_Board.md` - contingency board for students whose hardware or simulator station is unavailable

## Beginner pathway

If students are new to FPV or RC gear, keep the packet in this order:

1. **What does flying feel like?** Start with a short VelociDrone hook in Week 1.
2. **What is this thing?** Use `resources/tinywhoop_basics_air65.md`.
3. **What rules apply here?** Use `resources/us_indoor_outdoor_flight_rules.md`.
4. **How do we connect and back up safely?** Use Weeks 1-2.
5. **How do we practice without breaking things?** Use `resources/velocidrone_setup_and_drills.md` every week, starting in Week 1.
6. **How do we keep it flying?** Use `resources/maintenance_and_crash_recovery.md` and Week 6.
7. **How do we prepare for a fair race?** Use Weeks 7-10.

## 10-week arc

| Week | Tuesday focus | Thursday focus |
| --- | --- | --- |
| 1 | First simulator flight, ground school, safety, parts, and rules | Betaflight connection, first backup, FC orientation, and simulator reps |
| 2 | Simulator control drills, radio link, receiver tab, and channel mapping | Modes, arming logic, props-off motor tests, and simulator gate practice |
| 3 | Analog FPV/OSD concepts and simulator race-line drills | First controlled real flights and flight-area routines |
| 4 | Presets, rates, expo, and simulator feel tests | Simulator time trials plus cautious real-flight comparison |
| 5 | Backup habits, tune logs, and race setup records | Simulator race heats and documented real-lap practice |
| 6 | Crash recovery, wear points, and relaunch decisions | Battery habits and maintenance stations |
| 7 | Track design, race line, and course vocabulary | Marshal roles and structured track practice |
| 8 | Troubleshooting workflow and arming flags | Pair diagnostics and consistency flights |
| 9 | Race format, heat procedures, and final tech check | Practice heats, tune lock, and race-day planning |
| 10 | Final safety check and race event | Finals/showcase, teardown, and reflection |

## Platform note

This workshop can support mixed whoop hardware, but it includes examples and vocabulary that match a common beginner platform: the **BETAFPV Air65** with:

- a 5-in-1 flight controller stack
- an **ExpressLRS (ELRS) 2.4 GHz** control link
- an **analog 5.8 GHz VTX** and FPV camera

That gives students one concrete reference point while still leaving room for other whoops in the room.

Everything here is meant as a starting point: fork, revise, and remix for your space, your students, and your fleet of whoops.
