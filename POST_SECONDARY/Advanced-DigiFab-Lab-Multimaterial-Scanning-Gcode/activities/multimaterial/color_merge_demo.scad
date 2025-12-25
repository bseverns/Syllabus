/* Color merge: export two STLs or use modifiers to assign colors/materials */
module base(){
  cylinder(h=4, r=28, $fn=120);
}
module inlay(){
  translate([0,0,0.8]) linear_extrude(2.4) text("A", size=22, halign="center", valign="center");
}
base();
inlay();
