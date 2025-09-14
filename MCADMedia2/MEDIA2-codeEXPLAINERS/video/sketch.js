let isPlaying = false;
let fingers, button;

function setup() {
  fingers = createVideo('assets/WAG.mp4');
  button = createButton('play');
  button.mousePressed(toggleVid); // attach button listener
}

// plays or pauses the video depending on current state
function toggleVid() {
  if (isPlaying) {
    fingers.pause();
    button.html('play');
  } else {
    fingers.loop();
    button.html('pause');
  }
  isPlaying = !isPlaying;
}
