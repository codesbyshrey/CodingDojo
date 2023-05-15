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
        console.log(`Name:        ${this.name}`);
        console.log(`health:      ${this.health}`);
        console.log(`speed:       ${this.speed}`);
        console.log(`strength:    ${this.strength}`);
        return this; // important to return instance for self-referencing
    }

    drinkSake() {
        console.log(`${this.name} drank refreshing sake.`);
        this.health += 10;
        return this; // returning the instance
    }
}

const ninja1 = new Ninja("Shreyas", 21);
ninja1.sayName();
ninja1.drinkSake();
ninja1.showStats();
console.log("!@#$!@#$!@#$ now try to chain after including return this !@#$!@#$!@#$")
ninja1.sayName().showStats().drinkSake().showStats();