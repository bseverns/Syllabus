# Tuning Tiny Whoops: A Betaflight Configurator Workshop

This repository contains a ten-session workshop for high school students learning to configure, maintain, and race **tiny whoop** quadcopters using **Betaflight Configurator**.

The emphasis is on:

- Safety first  
- Learning what each part of the whoop actually does  
- Understanding indoor vs outdoor rules and responsibilities  
- Crash recovery and basic maintenance habits  
- Config literacy and good backup habits  
- Simulator time in **VelociDrone** before higher-stakes real flights  
- Building up “feel” through rates, modes, and presets  
- Building toward a final classroom race with safe habits and predictable machines

## Folder structure

- `SYLLABUS.md` – high–level overview, schedule, learning goals  
- `INSTRUCTOR_NOTES.md` – safety, logistics, and implementation notes  
- `sessions/` – detailed plans for each of the ten sessions  
- `materials/` – printable checklists and student–facing handouts  
- `resources/` – teacher-facing reference docs on basics, rules, and maintenance  
- `LICENSE` – MIT license for adapting this material

## How to use this repo

1. Read **SYLLABUS.md** to get the big picture.
2. Review **INSTRUCTOR_NOTES.md** and adapt any safety / admin language to your local policies.
3. Read the reference docs in `resources/` before teaching outdoors or with mixed hardware.
4. Work through each file in `sessions/` as you plan your workshop.
5. Print or duplicate the files in `materials/` for students, or import them into your LMS.

## Recommended beginner pathway

If your students are truly new, treat the workshop in this order:

1. **What is this thing?** Use `resources/tinywhoop_basics_air65.md`.
2. **What rules apply here?** Use `resources/us_indoor_outdoor_flight_rules.md`.
3. **How do we keep it flying?** Use `resources/maintenance_and_crash_recovery.md`.
4. **How do we practice without breaking things?** Use `resources/velocidrone_setup_and_drills.md`.
5. **How do we configure it?** Then move into Betaflight and the session plans.

## 10-session arc

1. Ground school, parts, rules, and first connection
2. Radio link, ELRS basics, modes, and arming
3. VelociDrone basics, analog FPV, OSD, and first controlled flights
4. Rates, presets, and flight feel
5. Profiles, backups, and tune documentation
6. Crash recovery, batteries, and maintenance
7. Track design, race line, and marshal roles
8. Troubleshooting clinic and consistency flights
9. Practice heats and race prep
10. Race day and reflection

## Platform note

This workshop can support mixed whoop hardware, but it now includes examples and vocabulary that match a common beginner platform: the **BETAFPV Air65** with:

- a 5-in-1 flight controller stack
- an **ExpressLRS (ELRS) 2.4 GHz** control link
- an **analog 5.8 GHz VTX** and FPV camera

That gives students one concrete reference point while still leaving room for other whoops in the room.

Everything here is meant as a starting point: fork, revise, and remix for your space, your students, and your fleet of whoops.
