/*
  Magnet-Token with Encapsulated Pocket (pause-and-drop workflow)
  Defaults: token Ø40, magnet 10×2 mm, base 1.2 mm, cover 1.0 mm.
*/
token_d = 40;
base_t  = 1.2;
magnet_d= 10.0;
magnet_t= 2.0;
cover_t = 1.0;
clearance = 0.25; // radial (per side)
$fn = 120;
token_h = base_t + magnet_t + cover_t;
module token(){
  difference(){
    cylinder(h=token_h, r=token_d/2);
    translate([0,0,base_t]) cylinder(h=magnet_t+0.001, r=(magnet_d/2)+clearance);
  }
}
token();
// Pause height target: base_t + magnet_t
