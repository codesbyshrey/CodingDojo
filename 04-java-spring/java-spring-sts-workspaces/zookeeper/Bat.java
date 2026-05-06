public class Bat extends Mammal {
     public Bat() {
          super();
          this.energyLevel = 300;
     }

     public void fly() {
          System.out.println("I am Batman");
          this.energyLevel -= 50;
     }

     public void eatHumans() {
          System.out.println("CHOMP");
          this.energyLevel += 25;
     }

     public void attackTown() {
          System.out.println("WEEWOOWEEWOO EVACUATE FIRE DRILL");
          this.energyLevel -= 100;
     }
}