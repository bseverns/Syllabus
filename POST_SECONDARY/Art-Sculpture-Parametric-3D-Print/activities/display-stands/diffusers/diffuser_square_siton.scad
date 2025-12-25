// ==== Shared Parameters ====
// Measure your pedestal's internal rebate (seat) carefully.
cavity_w   = 70;    // inner width (mm)
cavity_d   = 70;    // inner depth (mm)
lip_depth  = 2;     // rebate depth available for the diffuser to sit in (mm)
thickness  = 2.0;   // diffuser thickness (mm)
clearance  = 0.3;   // positive clearance for sit-on fit (mm)
chamfer    = 0.6;   // small edge break

/*
  Square diffuser — sit-on (rests in the pedestal rebate)
*/

module chamfered_plate(w,d,t, c){
  linear_extrude(height=t)
    offset(delta=-c)
      offset(delta=+c)
        square([w,d], center=true);
}

translate([0,0,thickness/2])
  chamfered_plate(cavity_w - clearance, cavity_d - clearance, thickness, chamfer);
