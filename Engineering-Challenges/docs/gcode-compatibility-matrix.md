# Format Compatibility (High‑level)

| Topic | MakerBot SKETCH | LulzBot Mini 2/3 |
|---|---|---|
| Print file | Proprietary job package (via MB slicer) | Standard G‑code (Cura LE) |
| Start/End | Managed by MB pipeline | Explicit start/end G‑code (this repo) |
| Pauses/Inserts | Schedule in UI | `M0`/`M600` or Cura post‑processing |
| Bed mesh | Managed in MB pipeline | `G29` per print or `M420 S1` saved mesh |
| Direct G‑code | Not recommended | Normal workflow |
