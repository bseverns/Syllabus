/*
  Tiling panel: repeated motif with adjustable spacing and wall thickness.
*/
tile_w = 20;
tile_h = 20;
cols = 8;
rows = 6;
gap = 2;
th = 2;

module motif(){
    difference(){
        square([tile_w, tile_h], center=false);
        offset(r= -3) square([tile_w, tile_h], center=false);
        translate([tile_w/2, tile_h/2]) circle(r=4, $fn=48);
    }
}

linear_extrude(height=th)
for (y=[0:rows-1])
 for (x=[0:cols-1])
  translate([x*(tile_w+gap), y*(tile_h+gap)]) motif();
