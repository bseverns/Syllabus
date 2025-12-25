/*
  Light‑Box Pedestal — Parametric (OpenSCAD)
  - Square pedestal with internal LED chamber and diffuser seat
  - Choose printed diffuser OR 3 mm acrylic insert
*/

// ==== Parameters ====
inner_w = 70;      // internal cavity width (mm)
inner_d = 70;      // internal cavity depth (mm)
height  = 60;      // overall pedestal height (mm)

wall_th = 3;       // wall thickness
lip_th  = 2;       // top lip thickness supporting diffuser
diff_th = 2;       // PRINTED diffuser thickness
acrylic_th = 3;    // if using acrylic

led_shelf_h = 18;  // height of internal LED shelf from base
cable_slot_w = 8;  // cable slot width
cable_slot_h = 4;  // cable slot height

use_printed_diffuser = true;  // set false for acrylic slot

$fn=96;

// ==== Derived ====
outer_w = inner_w + 2*wall_th;
outer_d = inner_d + 2*wall_th;
outer_h = height;

module box_shell(w,d,h,t){
    difference(){
        cube([w,d,h], center=false);
        translate([t,t,t]) cube([w-2*t, d-2*t, h-t], center=false);
    }
}

module cable_slot(){
    translate([0, (outer_d-cable_slot_w)/2, 6])
        cube([wall_th+1, cable_slot_w, cable_slot_h], center=false);
}

// Pedestal body
difference(){
    // shell
    box_shell(outer_w, outer_d, outer_h, wall_th);
    // LED shelf
    translate([wall_th, wall_th, led_shelf_h])
        cube([inner_w, inner_d, wall_th], center=false);
    // diffuser seat rebate
    translate([wall_th, wall_th, outer_h - lip_th])
        cube([inner_w, inner_d, lip_th+0.2], center=false);
}

// Cable slot through one wall
cable_slot();

// === Diffuser (optional printed cap) ===
if (use_printed_diffuser){
    // printed diffuser sits on the lip
    translate([0, outer_d + 5, outer_h - diff_th])
        cube([outer_w, outer_d, diff_th], center=false);
}else{
    // separate acrylic plate: print a simple alignment frame
    frame_w = outer_w;
    frame_d = outer_d;
    frame_th = 2;
    slot_tol = 0.3; // tolerance for acrylic thickness
    translate([0, outer_d + 5, outer_h - frame_th])
    difference(){
        cube([frame_w, frame_d, frame_th], center=false);
        translate([wall_th, wall_th, 0])
            cube([inner_w, inner_d, frame_th], center=false);
        // acrylic plate model (visual)
        translate([wall_th+1, wall_th+1, frame_th])
            cube([inner_w-2, inner_d-2, acrylic_th - slot_tol], center=false);
    }
}
