class Ninja {
    constructor(name, health=10) {
        this.name = name;
        this.health = health;
        this.speed = 3;
        this.strength = 3;
    }

    sayName() {
        console.log(`My name is ${this.name}`);
        return this; //allows us to chain by returning the instance
    }

    showStats() {
        console.log(`Name: ${this.name}`);
        console.log(`Health: ${this.health} || Speed: ${this.speed} || Strength: ${this.strength}`);
        return this; // important to return instance for self-referencing
    }

    drinkSake() {
        console.log(`${this.name} drank refreshing sake.`);
        this.health += 10;
        return this; // returning the instance
    }
}

//const ninja1 = new Ninja("Shreyas", 21);
//ninja1.sayName().showStats().drinkSake().showStats();


console.log("===============SUPER NINJA ASSIGNMENT====================");

class Sensei extends Ninja {
    constructor (name, health = 200, speed = 10, strength = 10) {
        super(name, health, speed, strength)
        this.wisdom = 10
    }

    speakWisdom(ninja) {
        super.drinkSake()
        console.log(`Dear ${ninja.name}... the past is history. The future is a mystery. Today, is a gift. That is why it is called the present`)
        return this
    }
}

const ninja2 = new Ninja('Po', 25)
const sensei1 = new Sensei('Master Oogway')

ninja2.drinkSake().showStats()
sensei1.speakWisdom(ninja2).drinkSake().showStats()