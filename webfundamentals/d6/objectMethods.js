

var pet = {
     name: "Max",
     age: 6,
     owner: "Roger",
     vaccinationHistory: ["10/20/2019", "8/16/2020", "9/23/2021"],
     displayInformation: function() {
          console.log("Pet Name:", pet.name);
          console.log("Pet Age:", this.age);
          console.log("Pet Owner:", this.owner);
          console.log("Vaccination History");
          console.log(this.vaccinationHistory);
          console.log(this.vaccinationHistory.join(" - "));
          for (var i=0; i < this.vaccinationHistory.length; i++){
               console.log( this.vaccinationHistory[i]);
          }
     }
}

let nums=[10, 29, 30, 40];

nums.push(50);

pet.displayInformation();