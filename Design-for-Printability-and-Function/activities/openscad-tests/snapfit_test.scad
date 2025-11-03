/*
  Cantilever snap-fit test coupon for cycle testing.
*/
base_w = 12;
base_l = 60;
base_h = 4;
arm_t  = 2.4;
arm_w  = 8;
arm_l  = 40;
hook_h = 3;
hook_o = 1.2;

union(){
  // base
  cube([base_l, base_w, base_h]);
  // arm
  translate([10, (base_w-arm_w)/2, base_h])
    cube([arm_l, arm_w, arm_t]);
  // hook
  translate([10+arm_l, (base_w-arm_w)/2, base_h+arm_t-hook_h])
    cube([4, arm_w, hook_h]);
  // stop
  translate([base_l-6, 0, 0]) cube([2, base_w, base_h+arm_t]);
}
