# Display Stands — Light‑Box Pedestal (Parametric)

A simple pedestal with an internal LED chamber and a slot for a **diffuser lid** (printed in translucent PLA or 3 mm acrylic). Sized for code-art vases and translucent studies.

## Bill of Materials (baseline)
- 5 V LED: either a short **WS2812B strip** (10–20 LEDs) or a small 5 V puck
- 5 V USB power supply (≥ 1 A) and cable
- (Recommended) 220 Ω series resistor on DIN (for addressable strips)
- (Recommended) 1000 µF electrolytic across 5 V / GND at the strip
- Black PLA for pedestal; natural/white translucent PLA for diffuser

## Build Steps
1. Print `light_box_pedestal.scad` → `pedestal.stl` and `diffuser_xxx.stl` (choose print-in diffuser or acrylic slot).
2. Coil or mount LEDs inside on the internal shelf; route cable through side slot.
3. Test power, verify no light leaks at the seam; add a felt pad to the base if desired.
4. Place artwork centered on the diffuser; aim seam to the least-visible side.


## Extras
- See `diffusers/` for **round/square** sit-on & snap-in tops.
- See `electronics/` for **gallery-safe LED controller** sketches (FastLED power-capped and NeoPixel fallback).
