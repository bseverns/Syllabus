# ClassHub Import Notes

These files package `AI at Work with Microsoft Learn` for the ClassHub syllabus ingest flow.

## Files

- `public_overview_classhub.md`: public-facing overview source
- `teacher_plan_classhub.md`: parseable teacher-plan source

## Suggested import command

From the `selfhosted-classhub` repo:

```bash
python3 scripts/ingest_syllabus_md.py \
  --sessions-md /path/to/Syllabus/SECONDARY/ai-at-work/classhub_import/teacher_plan_classhub.md \
  --overview-md /path/to/Syllabus/SECONDARY/ai-at-work/classhub_import/public_overview_classhub.md \
  --slug ai_at_work \
  --title "AI at Work with Microsoft Learn" \
  --default-ui-level secondary
```

## Why this layer exists

The main course already contains a full repo-native bundle. This folder adds the smaller source files the ClassHub importer expects:

- overview metadata
- `Session NN: Title` headings
- `Mission`
- `Teacher prep`
- `Materials`
- `Checkpoints`
- `Common stuck points + fixes`
- `Extensions`
