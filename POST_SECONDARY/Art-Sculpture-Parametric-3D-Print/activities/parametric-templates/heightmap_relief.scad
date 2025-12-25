/*
  Heightmap relief: import a PNG (grayscale) and map to Z.
  Create your PNG with p5.js or image editor. Keep it small (<= 256x256).
*/
scale_xy = 0.5;   // mm per pixel
height_z = 5;     // max relief height

surface(file="heightmap.png", center=false, convexity=10, invert=false);
scale([scale_xy, scale_xy, height_z/100])
    surface(file="heightmap.png", center=false, convexity=10);
