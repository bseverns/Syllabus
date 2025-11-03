/* 20 mm calibration cube with embossed axes */
size=20;
difference(){
  cube([size,size,size], center=true);
  translate([0,0,size/2-1]) linear_extrude(1) text("Z", size=6, halign="center", valign="center");
  rotate([90,0,0]) translate([0,0,size/2-1]) linear_extrude(1) text("Y", size=6, halign="center", valign="center");
  rotate([0,90,0]) translate([0,0,size/2-1]) linear_extrude(1) text("X", size=6, halign="center", valign="center");
}
