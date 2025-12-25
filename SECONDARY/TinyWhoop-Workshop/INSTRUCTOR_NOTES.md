# Instructor Notes

These notes are meant for teachers / mentors running the workshop.  
Adapt freely to your local policies, gear, and students.

---

## Safety & Policy

- Treat drones like power tools: fun, powerful, and never casual.
- Make sure you understand your school / district rules about drones on campus.
- Decide early:
  - Are you flying **indoors only** for this workshop?
  - Who is responsible for safety supervision when props are spinning?
  - Do you have a maximum number of powered–up quads at any one time?

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

---

## Hardware Diversity

Students may show up with different:

- FC firmware targets  
- Receiver types (e.g., built–in SPI receivers, external modules)  
- Radio brands and protocols  

Plan time in Session 2 for “case–by–case work.” The goal is to teach **how to reason through** the Receiver and Modes tabs, not to memorize a single recipe.

Whenever possible, use the projector to model:

- How you recognize the receiver protocol in Betaflight  
- How you verify that sticks and switches are doing what you expect  
- How you respond when something *doesn’t* work (reading status messages, checking arming flags, etc.)

---

## Timing & Pacing

The session plans in `sessions/` assume ~2 hours.  
For other formats:

- **90 minutes:** Trim discussion and keep one main hands–on focus per session.
- **60 minutes:** Consider splitting each session file into an “A” and “B” day.

If students are already experienced pilots, compress Sessions 1–2 and spend more time in Sessions 3–4 on:

- Multiple tune profiles
- More advanced presets
- Blackbox logging (if their FC supports it)
- Track design and timed races

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
