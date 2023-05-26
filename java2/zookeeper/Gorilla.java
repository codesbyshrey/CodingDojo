public class Gorilla extends Mammal {
     public Gorilla() {
          super(); //calls parent class data
     }

     public void throwSomething() {
          System.out.println("Gorilla threw something");
          this.energyLevel -= 5;
     }

     public void eatBananas() {
          System.out.println("Gorilla's Potassium increased");
          this.energyLevel += 10;
     }

     public void climb() {
          System.out.println("Gorilla has climbed a tree");
          this.energyLevel -= 10;
     }
}