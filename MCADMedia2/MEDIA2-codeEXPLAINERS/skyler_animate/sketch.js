let arrayA = [55, 40, 50];

function setup(){
  createCanvas(400, 400);
}

function draw(){
  background(255, 127, 50);

  var randNum = Math.floor(Math.random()*255);
  var randNum1 = Math.floor(Math.random()*255);
  var randNum2 = Math.floor(Math.random()*255);


  //was experimenting with arrays to try to get the
  //latest random numbers to be the block that appeared
  //when the mouse was on the left half


  let num1 = arrayA.length - 3;
  let num2 = arrayA.length - 2;
  let num3 = arrayA.length-1;

  console.log(arrayA);


  if (mouseX < width/2){

    fill(255, 0, 0);
    rect(mouseX - 20, mouseY - 30, 40, 60);


      fill(num1a, num2a, num3a);
      rect(num1a, num2a, num3a, num1a);


      console.log(arrayA);
      console.log(num1a);


  }else{
    fill(randNum, randNum1, randNum2);
    rect(randNum, randNum1, randNum2, randNum);

    arrayA.push(randNum1);
    arrayA.push(randNum2);
    arrayA.push(randNum);

    console.log(arrayA);


  }
}
