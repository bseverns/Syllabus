# Instructor Notes

These notes are meant for teachers / mentors running the workshop.  
Adapt freely to your local policies, gear, and students.

---

## Safety & Policy

- Treat drones like power tools: fun, powerful, and never casual.
- Make sure you understand your school / district rules about drones on campus.
- Decide whether this workshop is:
  - **indoor only**
  - **indoor first, outdoor later**
  - or a mixed indoor / outdoor program from day one
- Decide early:
  - Who is responsible for safety supervision when props are spinning?
  - Do you have a maximum number of powered–up quads at any one time?

### Indoor vs outdoor rule stance

The cleanest beginner version of this workshop is **indoor first**.

- **Indoor flight:** FAA airspace rules do not apply in the same way they do outdoors, but school rules, property rules, and your own safety procedures absolutely still do.
- **Outdoor flight:** FAA rules, local airspace restrictions, and site planning matter. Do not treat outdoor whoop flights as "just the same but outside."

For outdoor U.S. flights, verify current FAA guidance before launch. At the time of this update:

- Recreational outdoor flyers need **TRUST**.
- Drones under **250 g** flown recreationally generally do not require FAA registration.
- Drones that are required to be registered or are voluntarily registered must comply with **Remote ID**.
- Night operations and controlled airspace add more constraints.

Also note that school programs are not automatically "recreational" just because they are educational. If your district runs organized outdoor flights, verify whether the operation is truly recreational or should be handled under **Part 107** or another approved framework. Use `resources/us_indoor_outdoor_flight_rules.md` as a briefing tool, not as your only compliance check.

### FCC / FPV gear note

FAA flight rules are only part of the story. Analog FPV video transmitters and radio gear also need to comply with FCC rules.

For U.S. classroom use:

- Prefer known, FCC-compliant gear.
- Keep VTX power low indoors.
- Use a clear channel plan if more than one whoop is powered.
- Do not assume every analog VTX setting is legal for unlicensed student use.

If you run analog FPV outside or at higher power, verify your equipment and licensing assumptions before class. The workshop now includes this caveat because many beginner whoops blur the line between toy-scale flying and radio equipment that still carries real regulatory obligations.

### Suggested in–room safety rules

Feel free to paste or print these:

1. **Props off on the bench.**  
   No arming or motor tests with props mounted unless you are on the flight line.

2. **Goggles stay put.**  
   If a student is wearing FPV goggles, they are either seated in the pilot chair or standing in a clearly marked pilot area. No walking around with goggles on.

3. **Line of sight first.**  
   Early flights can be line–of–sight only. FPV is introduced once basic throttle control is comfortable.

4. **One whoop at a time** (for small rooms).  
   In a tight space, only one or two whoops should be flying at once to reduce chaos.

5. **Respect no–fly zones.**  
   Parts of the room (teacher desk, equipment shelves, doorways) are off–limits.

6. **Crash means disarm first, then inspect.**
   No student should turtle-mode, relaunch, or "just send it again" before checking props, canopy, battery lead, and frame.

Encourage students to help enforce safety as a shared responsibility, not just “teacher rules.”

---

## Technical Prep

Before Session 1:

- Install or verify access to the Betaflight Configurator app / web version on your machines.
- Test at least one known–good whoop with the exact hardware your students will use (same OS, same kind of USB cable).
- Prepare a “demo rig” that you don’t mind crashing or deliberately misconfiguring during troubleshooting activities.

Optional but recommended:

- Prepare a few **loaner whoops** in case a student’s hardware fails.
- Bring a **smoke stopper** if you anticipate any soldering or major repairs.
- Bring spare props, spare batteries, a prop tool or small driver, tweezers, tape, and at least one magnifier or bright inspection light.
- Set up at least one **VelociDrone** station and test radio USB/controller input before Session 3.

---

## Hardware Diversity

Students may show up with different:

- FC firmware targets  
- Receiver types (e.g., built–in SPI receivers, external modules)  
- Radio brands and protocols  

Plan time in Session 2 for “case–by–case work.” The goal is to teach **how to reason through** the Receiver and Modes tabs, not to memorize a single recipe.

If you want one concrete reference platform for teaching, the workshop is now written to support a **BETAFPV Air65** style whoop:

- brushless 65 mm class frame
- ELRS 2.4 GHz receiver link
- analog 5.8 GHz VTX and FPV camera
- 1S battery system

That lets you explain the signal chain clearly:

1. **Radio link:** ELRS carries pilot commands from transmitter to receiver.
2. **Flight control:** FC interprets commands and sensor data.
3. **Power stage:** ESCs drive the motors.
4. **Video link:** camera feeds the analog VTX, which sends video to goggles or a receiver.

Students often confuse the radio link and FPV video link. Separate those concepts constantly.

Whenever possible, use the projector to model:

- How you recognize the receiver protocol in Betaflight  
- How you verify that sticks and switches are doing what you expect  
- How you respond when something *doesn’t* work (reading status messages, checking arming flags, etc.)

---

## Timing & Pacing

The session plans in `sessions/` now assume a 10-session sequence at roughly 90-120 minutes each.  
For other formats:

- **90 minutes:** Trim discussion and keep one main hands–on focus per session.
- **60 minutes:** Consider splitting each session file into an “A” and “B” day.

If students are already experienced pilots, compress Sessions 1–2 and spend more time in Sessions 3–4 on:

- Multiple tune profiles
- More advanced presets
- Blackbox logging (if their FC supports it)
- Track design and timed races

For true beginners, do the opposite:

- keep Sessions 1–4 slow
- let line-of-sight control develop before full-FPV race expectations
- spend more time on recovery, relaunch decisions, and track discipline than on speed

## Simulator Use: VelociDrone

VelociDrone is worth using here because it lets students practice:

- throttle discipline
- takeoff and landing rhythm
- smooth turns
- race-line decisions
- repeated reps without prop damage

Recommended pattern:

- Use a **dedicated simulator block** in Session 3.
- Add a **10-15 minute simulator warm-up** before later real-flight sessions when possible.
- If hardware is limited, run stations:
  - sim station
  - bench setup station
  - flight line

Good beginner drills:

1. arm, lift, hover, land
2. straight line to gate
3. smooth left and right turns
4. figure-eight
5. one clean lap over the practice course

Treat simulator habits as transferable:

- same arming ritual
- same stick discipline
- same focus on clean exits from turns

---

## Differentiation

Some students will be:

- Already flying FPV at home  
- Brand new to RC gear  
- Interested mainly in coding / configuration rather than flying  

Give advanced students leadership roles:

- “Receiver whisperer” – helps others map channels
- “Safety marshal” – helps enforce in–room safety rules
- “Track designer” – designs and iterates on the whoop course

Let configuration–curious students focus on:

- Documenting settings (profiles, screenshots)
- Designing different “feel profiles” for different courses
- Writing or improving the checklists and handouts in `materials/`

---

## Documentation Culture

Encourage students to treat each change they make as a tiny experiment:

1. Save a backup before major changes.
2. Change one thing at a time when learning.
3. Write down or screenshot any tune they like so they can return to it later.

The goal is not just “a tuned whoop,” but a student who understands how their flying machine and their settings relate.

## Maintenance Culture

Tiny whoops survive because pilots check them constantly.

Teach a simple post-crash ritual:

1. Disarm.
2. Unplug if needed.
3. Check props for chips, bends, or hair wrapped on the shafts.
4. Check ducts and frame for splits.
5. Check canopy, camera angle, antenna, and battery lead.
6. Spin motors gently by hand and listen for rubbing.
7. Only relaunch if the quad passes inspection.

Use `resources/maintenance_and_crash_recovery.md` and `materials/Crash_Recovery_Checklist_student.md` so students learn that maintenance is part of piloting, not a separate topic.

## Race Day Guidance

The final race should reward safety, control, and consistency, not only aggression or raw speed.

Suggested race-day norms:

- start with a safety and channel check
- keep one clear race director voice
- assign marshals before heats start
- ground any quad that fails pre-race inspection
- stop a heat if video, control, or room safety becomes unclear

Suggested race formats:

- **Time trial:** best single clean lap or best 3-lap total
- **Heats:** small groups rotating through the track
- **Bracket:** only if the room, pilot skill, and channel discipline are strong enough

For a school workshop, time trials or small heats are usually more teachable than a full elimination bracket.
