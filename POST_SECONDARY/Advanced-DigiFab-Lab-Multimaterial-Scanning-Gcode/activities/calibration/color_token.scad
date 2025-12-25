/* Two-color token with recessed inlay (export as a single STL and use M600 at layer/height) */
difference(){
  cylinder(h=3, r=25, $fn=100);
  translate([0,0,0.6]) linear_extrude(1.8) text("LAB", size=18, halign="center", valign="center");
}
