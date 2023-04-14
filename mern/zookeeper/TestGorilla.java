public class TestGorilla {
     public static void main (String[] args) {
          Gorilla shrey = new Gorilla();
          // can't chain commands? unsure why

          // throw something 3x
          shrey.throwSomething();
          shrey.throwSomething();
          shrey.throwSomething();

          // eat bananas 2x
          shrey.eatBananas();
          shrey.eatBananas();

          // climb once
          shrey.climb();
          
          // display energyLevel
          shrey.displayEnergy();
     }
}