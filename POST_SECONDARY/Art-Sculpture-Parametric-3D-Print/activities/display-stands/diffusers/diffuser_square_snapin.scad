// ==== Shared Parameters ====
// Measure your pedestal's internal rebate (seat) carefully.
cavity_w   = 70;    // inner width (mm)
cavity_d   = 70;    // inner depth (mm)
lip_depth  = 2;     // rebate depth available for the diffuser to sit in (mm)
thickness  = 2.0;   // diffuser thickness (mm)
clearance  = 0.3;   // positive clearance for sit-on fit (mm)
chamfer    = 0.6;   // small edge break

/*
  Square diffuser — snap-in (light press fit with micro barbs)
*/
barb_h   = 0.4;   // radial barb height (mm) — test small!
barb_w   = 8;     // barb width along edge (mm)
barb_count_per_side = 2;

module chamfered_plate(w,d,t, c){
  linear_extrude(height=t)
    offset(delta=-c)
      offset(delta=+c)
        square([w,d], center=true);
}

module barb(){
  cube([barb_w, barb_h, lip_depth], center=true);
}

w = cavity_w + (clearance/2); // minimal clearance; barbs take up the grip
d = cavity_d + (clearance/2);

translate([0,0,thickness/2])
  chamfered_plate(w, d, thickness, chamfer);

// place barbs around perimeter centered at mid-thickness
for (i=[-1:2:1]){
  for (k=[1:barb_count_per_side]){
    // along X edges
    translate([i*(w/2), (k/(barb_count_per_side+1))*d - d/2, lip_depth/2])
      rotate([0,0, i==1 ? 90 : -90]) barb();
    // along Y edges
    translate([(k/(barb_count_per_side+1))*w - w/2, i*(d/2), lip_depth/2])
      barb();
  }
}
