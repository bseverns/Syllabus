# MakerBot SKETCH — Magnet Drop

- Export STL from `assets/magnet_token.scad` (defaults: Ø40, pocket 10×2).
- Compute **Z_pause = base_t + magnet_t** → 3.2 mm.
- Schedule pause by **height/time** in MakerBot UI near 3.2 mm.
- At pause, drop magnet; ensure it sits **below** last layer; resume.
