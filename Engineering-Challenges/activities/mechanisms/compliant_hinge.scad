/*
  Compliant hinge test strip.
*/
strip_w = 18; strip_l = 90; th = 3; slot_w = 1.0; slot_gap = 1.0; slots = 12;
linear_extrude(height=th)
difference(){
  square([strip_l, strip_w]);
  for(i=[0:slots-1]) translate([10 + i*(slot_w+slot_gap), (strip_w-slot_w)/2]) square([slot_w, slot_w]);
}
