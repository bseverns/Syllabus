arm_len = 120; arm_w = 12; arm_t = 5; hole = 3.2; hook_gap = 4;
linear_extrude(height=arm_t)
difference(){
  hull(){ circle(r=6); translate([arm_len,0]) circle(r=6); }
  translate([0,0]) circle(r=hole/2);
  translate([arm_len-10, -hook_gap/2]) square([6, hook_gap]);
}
