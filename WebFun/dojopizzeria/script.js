// practice making javascript objects and using math.random
// making pizzas in javascript - create pizzaOven
// crustType, saucetype, cheeses, toppings
// create one with deep dish, traditional, mozz pepp saus
// hand tossed, marinara, mozz feta, mushr olives onions

function pizzaOven(crustType, sauceType, cheeses, toppings, sides) {
     var pizza = {};
     pizza.crustType = crustType;
     pizza.saucetype = sauceType;
     pizza.cheeses = cheeses;
     pizza.toppings = toppings;
     pizza.sides = sides;
     return pizza;
}

var p1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"], "ranch");
var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"], "bbq");
var p3 = pizzaOven("garlic crust", "spicy marinara", "mozzarella", ["pineapple", "jalapeno"], "mikes hot honey");
var p4 = pizzaOven("cheese crust", "alfredo", ["parmesan", "feta"], ["spinach", "peppers", "tomatoes", "basil"],["ranch", "bbq"]);

console.log(p1, p2, p3, p4);

//create a function called randomPizza that uses Math.random() to create a random pizza!
// not doing it yet but this is what rough steps should probably look like:
// for each var input in the pizzaOven function, define an array of possible values
// create a randomizer that accepts the range of array values (# per var)
// create a random picking function to determine which one in the array will be picked
// create a randomPizza function that assigns function calles to each subtype, with loops that push array values - pizza.cheeses.push(randomPick(cheeses)) based on the random range values for the iterations



// function sandwichFactory(bread, protein, cheese, toppings) {
//      var sandwich = {};
//      sandwich.bread = bread;
//      sandwich.protein = protein;
//      sandwich.cheese = cheese;
//      sandwich.toppings = toppings;
//      return sandwich
// }

// var s1 = sandwichFactory("wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"]);
// console.log(s1);

// var sandwich = {
//      bread: "sourdough",
//      protein: "london broil",
//      cheese: "lacey swiss cheese",
//      toppings: ["romaine lettuce", "heirloomtomatoes", "horseradish sauce"]
// };

// console.log(sandwich);