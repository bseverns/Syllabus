
function setup() {
	createCanvas(400, 400);
}

function draw() {
	background(255, 127, 50);
	//scale(4);


	if (mouseX < width/2) {
		fill(255, 0, 0);
		rect(10, 10, 30, 30);

	} else {
		fill(0, 0, 255);
		rect(10, 10, 50, 30);
		rect(5, 5, 20, 30);
	}
}
