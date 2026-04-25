// script for dojonary

function removeDefinition(element){
     console.log(element);
     element.remove();
}

function ninjaLike(element){
     alert("ninja was liked");
     console.log("ninja was liked");
}

function logout(element) {
     console.log(element.value);

     var logOutIn = document.querySelector(".logout");
     console.log(logOutIn);
     logOutIn.innerText = "Logout";

     // if span text currently reads Login, change to Logout
     // if span text currently reads Logout, change to Login
}