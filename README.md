# Syllabus Grab Bag

A messy, honest archive of courses I've slung across classrooms, studios, and half-baked workshops. Each folder is a snapshot of a semester, complete with syllabi, assignments, and weird little experiments. Some files are slick markdown, others are scrappy `.docx` and `.pdf` survivors—open them however you can.

## Map
- [ExplorationSoundDesign](./ExplorationSoundDesign): complete Chromebook-friendly sound design course with station cards and 22-day lesson run.
- [MCADArduinoSculpture](./MCADArduinoSculpture): odds and ends from the Arduino Sculpture class. The real action lives in its own repo: <https://github.com/bseverns/ArduinoSculpture_MCAD>.
- [MCADMedia1](./MCADMedia1): project briefs, cheat sheets, and first-year media experiments.
- [MCADMedia2](./MCADMedia2): follow-up course with code explainers and project prompts, plus [MEDIA2-codeEXPLAINERS](./MCADMedia2/MEDIA2-codeEXPLAINERS) for p5.js demos.

## Why It Exists
I hate losing track of good teaching material, so this is my dumping ground. Fork it, remix it, throw it at your students. If something's missing, yell at me or submit a PR.

Stay curious, stay loud.

Our classroom policies riff on Corita Kent's Ten Rules—check [shared/policies](./shared/policies) if you want the full manifesto.

## Tidy Map
- [shared/](./shared): templates, policies, rubrics
- [course-briefs/](./course-briefs): day-one course starters
- Courses:
  - [ExplorationSoundDesign](./ExplorationSoundDesign)
  - [MCADArduinoSculpture](./MCADArduinoSculpture)
  - [MCADMedia1](./MCADMedia1)
  - [MCADMedia2](./MCADMedia2)

## How to use
1. Copy bits from `shared/` into your course folder.
2. Fill in `brief.md` with the YAML front matter.
3. Adapt templates, link policies, keep process logs.
4. Run `python tools/validate.py` to lint and rebuild the catalog.
5. Check `catalog/index.json` to see your course show up.
