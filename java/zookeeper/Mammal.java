public class Mammal {
     // mammals have default energy level of 100
     protected static int energyLevel = 100;

     // displayEnergy method
     public int displayEnergy() {
          System.out.println(this.energyLevel);
          return this.energyLevel;
     }
}