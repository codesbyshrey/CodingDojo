
// DojoWeather - shown in class for Belt Exam Review
// select feature changes temperature numbers on maxDegree and minDegree

console.log("hello");

function displayMessage(element) {
     alert("Loading weather report...");
}

function acceptCookie(element) {
     // could have addressed the cookie div class to make the entire div disappear, querySelector allows you to remove within elements by one level
     console.log(element);
     console.log(element.parentElement);

     console.log(element.parentElement.querySelector("h3"));
          // shows how we can navigate downwards to print / have functionality
     console.log(element.closest(".cookie")); // works in similar fashion

     alert("Thank you for accepting cookies");
     element.parentElement.remove();

     // if we have multiple cookies, this allows us to determine which cookies are being accepted / have different classes to lead to different options / repeated similar elements of cookies and such
     //querySelector allows us to navigate downwards comparatively
}

function swapTemp(element) {
     console.log(element.value);
     var degreeValues = document.querySelectorAll(".degree");

     for (var i=0; i<degreeValues.length; i++) {
          var currentNum = Number (degreeValues[i].innerText);
          console.log(currentNum);
          var newNum;
          if (element.value === "C") {
               newNum = (currentNum - 32) * 5/9;
          }
          else {
               newNum = (currentNum * 9/5 ) + 32;
          }
          degreeValues[i].innerText=Math.ceil(newNum);
}
     //querySelectorAll helps you avoid only selecting the top one, provides an array of spans comparatively so that you can grab every number, apply the formula, and update the text
     // degrees were placed outside of the span so that the querySelector can appropriately understand the numerical values only
}