// ==== Shared Parameters ====
// Measure your pedestal's internal rebate (seat) carefully.
cavity_w   = 70;    // inner width (mm)
cavity_d   = 70;    // inner depth (mm)
lip_depth  = 2;     // rebate depth available for the diffuser to sit in (mm)
thickness  = 2.0;   // diffuser thickness (mm)
clearance  = 0.3;   // positive clearance for sit-on fit (mm)
chamfer    = 0.6;   // small edge break

/*
  Round diffuser — snap-in with micro barbs
*/
$fn=120;
barb_h = 0.4;
barb_w = 6;
barb_count = 8;

diam = min(cavity_w, cavity_d) + (clearance/2);

translate([0,0,thickness/2])
  linear_extrude(height=thickness)
    offset(delta=-chamfer) offset(delta=+chamfer)
      circle(r=diam/2);

// barbs placed radially
for (i=[0:barb_count-1]) {
  ang = 360/barb_count * i;
  translate([ (diam/2), 0, lip_depth/2 ])
    rotate([0,0,ang])
      linear_extrude(height=lip_depth)
        square([barb_w, barb_h], center=true);
}
