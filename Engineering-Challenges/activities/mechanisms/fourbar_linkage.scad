/*
  Four-bar linkage plates with adjustable bar lengths and hole clearances.
*/
L_ground = 80;
L_input  = 60;
L_coupler= 70;
L_output = 50;
th = 4;
hole = 3.2; // M3 clearance
pad = 10;

module link(len){
  linear_extrude(height=th)
    hull(){ circle(r=pad); translate([len,0,0]) circle(r=pad); }
  translate([0,0,-1]) cylinder(h=th+2, r=hole/2, $fn=40);
  translate([len,0,-1]) cylinder(h=th+2, r=hole/2, $fn=40);
}

translate([0,0,0]) link(L_ground);
translate([0,20,0]) link(L_input);
translate([0,40,0]) link(L_coupler);
translate([0,60,0]) link(L_output);
