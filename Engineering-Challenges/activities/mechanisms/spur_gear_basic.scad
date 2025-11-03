/*
  Basic spur gear blank (visual/teaching). For production, prefer a proven gear library.
*/
module_mm = 2.0;
teeth = 18;
thickness = 6;
bore = 5.0;
$fn=200;
module gear_blank(m,z,thk)=cylinder(h=thk, r=(m*z/2)+m);
difference(){
  gear_blank(module_mm, teeth, thickness);
  translate([0,0,-1]) cylinder(h=thickness+2, r=bore/2, $fn=80);
}
