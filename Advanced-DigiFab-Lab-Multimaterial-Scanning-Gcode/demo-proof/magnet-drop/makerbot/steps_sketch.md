# MakerBot SKETCH — Magnet Drop Demo

**Model:** Export STL from `../assets/magnet_token.scad` after setting params.  
**Defaults:** token Ø40 mm, 10×2 mm magnet, base 1.2 mm, cover 1.0 mm.

## Slice & Pause
1. Import STL in MakerBot slicer and pick your quality preset (match layer height with LulzBot as closely as possible).
2. Compute **pause height**: `Z_pause = base_t + magnet_t` → 3.2 mm.  
3. In the MakerBot UI, schedule a **pause at ~3.2 mm** (or at the layer/time nearest to that height).

## Procedure
- Start print. At pause, place the 10×2 mm magnet **flat** in the pocket.  
- Confirm it sits **below** the top of the last printed layer; if not, adjust or abort.  
- Resume and let the machine build the **cover**.

**Tips**
- If pocket fit is loose, a **tiny** dot of gel CA can help; avoid fumes and keep adhesive off top surfaces.
- Keep magnets well away from electronics; mind polarity for sets.
