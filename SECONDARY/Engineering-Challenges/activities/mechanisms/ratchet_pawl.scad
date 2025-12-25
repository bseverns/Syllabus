/*
  Ratchet & pawl (demonstrator blank).
*/
teeth = 12;
radius = 20;
thickness = 6;
pawl_len = 25;
pawl_th = 4;
$fn=180;

module wheel(){ cylinder(h=thickness, r=radius); }
module pawl(){ linear_extrude(height=pawl_th) square([pawl_len, 6]); }

wheel();
translate([radius+10,0,0]) pawl();
