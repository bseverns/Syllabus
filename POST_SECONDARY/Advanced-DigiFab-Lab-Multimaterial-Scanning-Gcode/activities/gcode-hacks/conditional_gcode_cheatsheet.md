# Conditional G‑code Cheatsheet (conceptual)

- **Variables**: Some slicers expose `layer_z`, `bed_temperature`, etc.
- **Pauses**: `M0` (stop), `M25` (pause SD print), `M601` (pause), `M600` (filament change) — **check firmware**.
- **Examples**:
  - Pause at layer: insert `M0` in layer change script when `layer_z > X`.
  - Insert nut: pause, move head to park, wait; resume after placement.
- Always provide a **safe park** (Z up), and document how to recover.
