public class CafeJava {
     public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
          String generalGreeting = "Welcome to Cafe Java, ";
          String pendingMessage = ", your order will be ready shortly";
          String readyMessage = ", your order is ready";
          String displayTotalMessage = "Your total is $";

        // Menu variables (add yours below)
          double mochaPrice = 4.5;
          double dripCoffeePrice = 3.0;
          double lattePrice = 3.5;
          double cappucinoPrice = 4.0;

        // Customer name variables (add yours below)
          String customer1 = "Cindhuri";
          String customer2 = "Sam";
          String customer3 = "Jimmy";
          String customer4 = "Noah";

        // Order completions (add yours below)
          boolean isReadyOrder1 = false;
          boolean isReadyOrder2 = false;
          boolean isReadyOrder3 = true;
          boolean isReadyOrder4 = true;

        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //

     // create 3 more drink price variables for drip coffee, lattee, and cappuccino following camcelcase
     // create 3 customer variables forSam, Jimmy, and Noah, following same naming convention
     // create order status for each customer

     // simulating customer interactions. Cindhuri orders a coffee
     // Noah orders a cappucino. Use an if statement to checkstatus of order and print message
          // if ready, print message to display total

     //Sam orders 2 lattes, use if statement for appropriate order status message
     // Jimmy was charged for coffee but ordered latte, print total message w/ new calculated total
     // change price values for drinks and isReady flags to make sure logic works, even when prices / status are changed

     System.out.println(customer1 + pendingMessage);

     if (isReadyOrder4) {
          System.out.println(customer4 + readyMessage);
          System.out.println(displayTotalMessage + cappucinoPrice);
     } else {
          System.out.println(customer4 + pendingMessage);
     }

     System.out.println(displayTotalMessage + lattePrice * 2);
     if (isReadyOrder2) {
          System.out.println(customer2 + readyMessage);
     } else {
          System.out.println(customer2 + pendingMessage);
     }

     System.out.println(displayTotalMessage + (lattePrice-dripCoffeePrice));

     }
}o
