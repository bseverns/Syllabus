# Validation + Migration

Minimum validation:
- version exists
- midi_channel 1..16
- curve is known
- smoothing_alpha in [0..1]

Migration:
- firmware reads version
- older configs migrate forward with defaults
- newer configs rejected with clear error + safe fallback

Safe apply:
- validate → write atomically → acknowledge
