let xpos = 10;

function setup() {
	createCanvas(400, 400);
	noLoop();
}

function draw() {
	background(255);

	while (xpos < 400) {
		fill(0,0,xpos/2);
		rect(xpos, 10, 25, 380);
		xpos = xpos + 50;
	}
}
