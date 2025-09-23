# Syllabus Grab Bag

A messy, honest archive of courses I've slung across classrooms, studios, and workshops. Each folder is a snapshot of a semester,
complete with syllabi, assignments, and weird little experiments. Some files are slick markdown, others are scrappy `.docx` and
`.pdf` survivors—open them however you can and remix at will.

## How the repo is laid out
Think of this directory like a teaching studio with stations. Jump in wherever your class needs a spark.

### Course stacks ready to run
- [CTMSoundDesign](./CTMSoundDesign): cue sheets, reflections, and a quickstart guide for a compact sound unit.
- [ExplorationSoundDesign](./ExplorationSoundDesign): Chromebook-friendly sound design adventure with station cards and a 22-day arc.
- [MCADArduinoSculpture](./MCADArduinoSculpture): documentation scraps from my Arduino sculpture class. The canonical repo still lives at <https://github.com/bseverns/ArduinoSculpture_MCAD>.
- [MCADMedia1](./MCADMedia1): project briefs, cheat sheets, and first-year media experiments.
- [MCADMedia2](./MCADMedia2): follow-up course with code explainers and project prompts, including [MEDIA2-codeEXPLAINERS](./MCADMedia2/MEDIA2-codeEXPLAINERS) for p5.js demos.
- [Robotics-to-FPV-Course](./Robotics-to-FPV-Course): full robotics-to-FPV pathway with build plans, assessments, safety docs, and sim exercises.

### Resource bins and shared infrastructure
- [shared/](./shared): policies, assessment tools, and templates grounded in Corita Kent's Ten Rules.
- [catalog/](./catalog): JSON index + schema for wrangling these courses into something a little more machine-readable.
- [tools/](./tools): utility scripts for validating the catalog and keeping data honest.

### Future courses + reference piles
- [future-course-briefs/](./future-course-briefs): rough briefs and provocations for classes still percolating.
- [SMM/](./SMM) & [MPS_comEd/](./MPS_comEd): legacy lesson plans hanging out as `.docx` files—convert, annotate, or cannibalize them.

## Why it exists
I hate losing track of good teaching material, so this is my dumping ground. Fork it, remix it, throw it at your students. If
something's missing, yell at me or submit a PR.

Want the full classroom manifesto? Hit [shared/policies](./shared/policies) for expectations riffing on Corita Kent's Ten Rules.

## How to work with this stash
- Start with a course stack, then raid `shared/` for rubrics or policies to glue it together.
- Use the JSON `catalog/` when you want to surface courses on a website or in another tool—`tools/validate.py` keeps you from breaking it.
- Everything is remixable. Annotate, translate, break, rebuild. Just send back the cool stuff.
