import java.util.ArrayList;
import java.util.Arrays;

// TEST EARLY AND TEST OFTEN
// also find a text formatter, copy pasting from Learn platform leads
// an absurd amount of weird tabbed lines

public class TestCafe {
     public static void main (String[] args) {

          /* Add 1 line to instantiate the CafeUtil class, correspond w/ variable names used below) */
          CafeUtil appTest = new CafeUtil();

          // APP TEST CASES -------------------------------------
          System.out.println("\n ----- Streak Goal Test -----");
          System.out.printf("Purchases needed by week 10: %s \n\n", appTest.getStreakGoal(10));

          System.out.println("----- Order Total Test-----");
          double[] lineItems = {3.5, 1.5, 4.0, 4.5};
          System.out.printf("Order total: %s \n\n",appTest.getOrderTotal(lineItems));
          
          System.out.println("----- Display Menu Test-----");
          
          ArrayList<String> menu = new ArrayList<String>();
          menu.add("drip coffee");
          menu.add("cappuccino");
          menu.add("latte");
          menu.add("mocha");
          appTest.displayMenu(menu);

          // Learn checkboxes include Print Price Chart Test even though it's Ninja Bonus
          System.out.println("\n----- Print Price Chart Test -----");
          appTest.printPriceChart("Columbian Coffe Grounds", 15.0, 3);
     
          System.out.println("\n----- Add Customer Test-----");
          ArrayList<String> customers = new ArrayList<String>();
          // --- Test 4 times ---
          for (int i = 0; i < 4; i++) {
               appTest.addCustomer(customers);
               System.out.println("\n");
          }
     }
}

// OBJECTIVES
// practice array, arraylist, loops
// create own methods file
// understand diff b/w printing and returning a value