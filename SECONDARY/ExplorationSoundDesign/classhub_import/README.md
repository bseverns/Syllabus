# ClassHub Import Notes

These files are a thin packaging layer for the ClassHub syllabus ingest flow.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: teacher-facing session plan source formatted for the ingest parser

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/SECONDARY/ExplorationSoundDesign/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/SECONDARY/ExplorationSoundDesign/classhub_import/public_overview_classhub.md \
  --slug exploration_sound_design \
  --title "Intro to Sound Design & Engineering" \
  --default-ui-level secondary
```

## Why this layer exists

The main course repo is already useful for teachers, but ClassHub import expects:

- a public overview source
- a parseable teacher-plan source with `Session NN: Title` headings
- consistent `Mission`, `Teacher prep`, `Materials`, `Checkpoints`, `Common stuck points + fixes`, and `Extensions` sections

This folder provides those ingest-ready sources without flattening the richer repo structure.
