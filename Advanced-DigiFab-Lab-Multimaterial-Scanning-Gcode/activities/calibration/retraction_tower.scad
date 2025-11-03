/* Retraction test: thin posts to reveal stringing at different retraction settings */
$fn=48;
for (x=[0:4]){
  for (y=[0:4]){
    translate([x*18, y*18, 0]) cylinder(h=30, r=2);
  }
}
