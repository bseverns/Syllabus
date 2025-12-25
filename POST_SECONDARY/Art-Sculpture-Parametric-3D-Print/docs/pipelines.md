# Pipelines: Code → Print

## A. OpenSCAD → STL → Slicer
1. Edit `.scad` → F6 render → export STL.
2. In slicer, start with Draft; orient for surface intent.

## B. p5.js → SVG → OpenSCAD
1. Generate `pattern.svg` with p5.js (SVG renderer).
2. In OpenSCAD: `linear_extrude(height=3) import("pattern.svg");`

## C. Heightmap (PNG) → Relief
1. Create `heightmap.png` (grayscale).
2. In OpenSCAD: `surface(file="heightmap.png")` then scale Z.
