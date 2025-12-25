# Format Compatibility Notes (High‑level)

| Topic | MakerBot SKETCH | LulzBot Mini 2/3 |
|---|---|---|
| Print file format | Printer‑specific **job package** created by MakerBot software | Standard **G‑code** from Cura LulzBot Edition |
| Start/End control | Encoded by MakerBot’s job pipeline | Explicit start/end G‑code (provided in repo) |
| Pauses/Inserts | Schedule via MakerBot UI | `M0`/`M600` (firmware‑dependent) or Cura post‑processing |
| Mesh level | Managed within MakerBot pipeline | `G29` each print or `M420 S1` saved mesh |
| Direct G‑code upload | **Not recommended** | **Yes** (normal workflow) |

**Bottom line:** Keep **separate slicing pipelines**, but unify models, naming, and logs.
