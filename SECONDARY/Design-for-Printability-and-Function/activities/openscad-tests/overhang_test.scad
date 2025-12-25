/*
  Overhang test: prints angled roofs from 30° to 80° (from vertical).
  Params let you change step, thickness, and label size.
*/
angle_start = 30;  // deg from vertical
angle_end   = 80;
angle_step  = 10;
thickness   = 2;
tower_w     = 12;
tower_d     = 20;
tower_h     = 40;
base_h      = 4;
gap         = 8;

module tower(angle){
    // body
    translate([0,0,base_h]) cube([tower_w, tower_d, tower_h], center=false);
    // roof as overhang
    translate([0,0,base_h + tower_h])
        rotate([0, angle, 0])
            cube([tower_w, tower_d, thickness], center=false);
    // label tab
    translate([0, -4, 0]) cube([tower_w, 4, base_h], center=false);
}

x = 0;
for (a = [angle_start:angle_step:angle_end]){
    translate([x,0,0]) tower(a);
    x = x + tower_w + gap;
}
