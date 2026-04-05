# ClassHub Import Notes

These files package `Digital Imaging Lab — Level 1` for the ClassHub syllabus ingest flow.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/SECONDARY/digital-imaging-lab/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/SECONDARY/digital-imaging-lab/classhub_import/public_overview_classhub.md \
  --slug digital_imaging_lab_level1 \
  --title "Digital Imaging Lab — Level 1" \
  --default-ui-level secondary
```

## Why this layer exists

The main course repo is structured for teaching and adaptation. ClassHub import expects a tighter source format with:

- overview metadata
- `Session NN: Title` headings
- `Mission`
- `Teacher prep`
- `Materials`
- `Checkpoints`
- `Common stuck points + fixes`
- `Extensions`
