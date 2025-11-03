/*
  Bridge ladder: base pillars with spans increasing by step.
*/
span_start = 10;
span_end   = 50;
span_step  = 10;
pillar_w   = 10;
thickness  = 2;
height     = 30;
gap        = 10;

x = 0;
for (s = [span_start:span_step:span_end]){
    // pillars
    translate([x,0,0]) cube([pillar_w, pillar_w, height]);
    translate([x + pillar_w + s,0,0]) cube([pillar_w, pillar_w, height]);
    // bridge
    translate([x + pillar_w, 0, height])
        cube([s, pillar_w, thickness]);
    x = x + pillar_w*2 + s + gap;
}
