function trigger( element, colorName ){
    console.log(  element, colorName );

    // holding global variable about html with query selector

    var box = document.querySelector(".box");
    box.style.backgroundColor = colorName;
    // should assign the background colors to the appropriate CSS properties based on the colorName being assigned in the HTML
}

function addTextToLog (element) {
    var text = element.innerText;
    var log = document.querySelector(".log");
    log.innerHTML += '<p> ${text} </p>';
    // log.innerHTML += "<p>" + text + "</p>";
}

function toggleCatImage (element) {
    var catImage = document.querySelector(".catImage");
    console.log( catImage.classList );
    if (catImage.classList.contains("hideImage")) {
        catImage.classList.remove("hideImage");
    }
    else {
        catImage.classList.add("hideImage");
    }
}

function removeImageAndButton (element) {
    var hideShowButton = document.querySelector("hideShow");
    var catImage = document.querySelector(".catImage");
    hideShowButton.remove();
    catImage.remove();
    // disable the button now
    element.disabled=true;
}