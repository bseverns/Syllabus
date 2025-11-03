# Course Syllabi Collection

A growing, versioned collection of course materials designed and taught by Ben — structured for clarity, remixability, and reuse. This repo begins with the **Robotics & Vibe Coding — Level 1** course and its enrichment track, using a consistent “GreenEl_3Dp‑style” documentation pattern (teacher/student docs, safety, rubrics, BOMs, and reproducible build instructions).

## Highlights
- **8 sessions × 2 hours** with A/B block structure (code‑along then studio time).
- **Max 12 robots** target; **budget‑tiered BOMs**.
- **Three dialects** (choose-your-path): LEGO Spike (Scratch & Python), Arduino (C/C++), and MicroPython/CircuitPython (Raspberry Pi Pico).
- **Improvised lab readiness**: clear facilities checklists, portable kits, and safety.
- **PDF builds** via `pandoc` (optional).

> This repo is meant to expand. Add new courses under `/courses/<slug>/` and follow the same pattern.

## Structure
```
courses/
  robotics-vibe-coding-level1/
    syllabus.md
    syllabus_enrichment.md
    pacing_guide.md
    materials.md
    facilities.md
    assessment_rubric.md
    teacher_guide.md
    student_guide.md
    sessions/
      session_01.md ... session_08.md
    safety_checklists/
      general_safety.md
    dialects/
      lego-spike/
      arduino/
      micropython/
    assets/
      handouts/
      slides/
docs/                 # place generated PDFs here
scripts/              # build/utility scripts
templates/            # doc/code templates
tools/                # optional pandoc templates
```

## Build PDFs (optional)
Requires [pandoc](https://pandoc.org) and LaTeX (or your preferred PDF engine).
```bash
# build all course PDFs into /docs
make pdf
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). For privacy and consent practices, see [PRIVACY-ETHICS.md](PRIVACY-ETHICS.md).

---
_Last updated: 2025-11-03_


## Courses included
- [Robotics & Vibe Coding — Level 1](courses/robotics-vibe-coding-level1/)
- [Robotics & Vibe Coding — Level 2](courses/robotics-vibe-coding-level2/)

- [Robotics & Vibe Coding — Level 3](courses/robotics-vibe-coding-level3/)
_Last updated: 2025-11-03_

_Last updated: 2025-11-03_
