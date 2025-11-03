/*
  Cantilever snap-fit coupon.
*/
base = [50,20,3];
arm_len = 35; arm_w = 8; arm_t = 2.2; hook_h = 1.6;
linear_extrude(height=base[2]) square([base[0], base[1]]);
translate([10,(base[1]-arm_w)/2, base[2]]) linear_extrude(height=arm_t) square([arm_len, arm_w]);
translate([10+arm_len,(base[1]-arm_w)/2, base[2]]) linear_extrude(height=arm_t+hook_h) square([3, arm_w]);
