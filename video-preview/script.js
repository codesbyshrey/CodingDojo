console.log("page loaded...");

function playVideo(vid) {
     console.log(vid); // this way we can check inspect element to show that the functon has been called when we are over the video
     vid.play();
}

function pauseVideo(vid) {
     console.log(vid);
     vid.pause();
     vid.currentTime = 0; // this allows us to reset the video to the start once the mouse is no longer hovering over it
}