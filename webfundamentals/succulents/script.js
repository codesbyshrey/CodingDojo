// Easybay Yellow Belt Examination

console.log("Good Start")

// Cart Button Functionality --> create an alert

function cartEmpty (element) {
     console.log(element);
     alert("Your Cart is currently Empty");
}

// Cookie Button Funcionality --> parent element should be removed when the I accept button is being clicked. Fixed position at bottom.

function acceptCookie(element) {
     console.log(element.parentElement);
     element.parentElement.remove();
}

// Video Preview Functionality but now has to cycle through multiple images

let imageCarousel = [];


function carousel(id) {
     console.log(id)
     document.getElementById("imgId").src=imageCarousel[0];
     let timeoutID = setTimeout(imageCarousel.push, 1500);
     setTimeout(imageCarousel.push(src="./assets/cactus-s.jpg"), 1500);
     document.getElementById("imgID").src=imageCarousel[1];
     setTimeout(imageCarousel.push(src="./assets/echeveria-s.jpg"), 1500);
     document.getElementById("imgID").src=imageCarousel[2];
}

function reset (id) {
     document.getElementById("imgId").src="./assets/aeonium-s.jpg";
     console.log(id);
}
