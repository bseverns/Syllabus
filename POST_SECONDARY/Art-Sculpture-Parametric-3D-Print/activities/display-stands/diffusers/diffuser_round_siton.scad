// ==== Shared Parameters ====
// Measure your pedestal's internal rebate (seat) carefully.
cavity_w   = 70;    // inner width (mm)
cavity_d   = 70;    // inner depth (mm)
lip_depth  = 2;     // rebate depth available for the diffuser to sit in (mm)
thickness  = 2.0;   // diffuser thickness (mm)
clearance  = 0.3;   // positive clearance for sit-on fit (mm)
chamfer    = 0.6;   // small edge break

/*
  Round diffuser — sit-on
*/
$fn=120;

diam = min(cavity_w, cavity_d) - clearance;

translate([0,0,thickness/2])
  linear_extrude(height=thickness)
    offset(delta=-chamfer) offset(delta=+chamfer)
      circle(r=diam/2);
