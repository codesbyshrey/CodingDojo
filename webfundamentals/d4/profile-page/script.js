console.log("page loaded...");

// clicking button will remove from requests, or increase connections
// clicking edit profile will change the name to any other name

var requestSpan = document.querySelector("#requests");
var connectionSpan = document.querySelector("#connections");
var username = document.querySelector("#username");

function accept (id){
     var element = document.querySelector(id);
     element.remove();
     requestSpan.innerText--;
     connectionSpan.innerText++;
}

function ignore (id) {
     var element = document.querySelector(id);
     element.remove();
     requestSpan.innerText--;
}

function edit() {
     username.innerText = "Shreyas Sriram";
}