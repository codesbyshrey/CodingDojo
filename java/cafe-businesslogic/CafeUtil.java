import java.util.ArrayList;
import java.util.Arrays;

public class CafeUtil {
     // int getStreakGoal()
     /* reward system for customers, sums together 1-10 and returns result
     Number printed should be 55. NinjaBonus - add numWeeks so that admin can
     change to any number of weeks they would like */

     public int getStreakGoal(int numWeeks) {
          int sum = 0;
          for (int i = 0; i <= numWeeks; i++) {
               // start at 1 so this logic works
               sum += i;
          }
          return sum;
     }

     /* double getOrderTotal(double[] prices)
     given array of item prices, sum all of them and return total
     Test lines are provided in TestCafe already*/

     public double getOrderTotal(double[] prices) {
          double totalPrice = 0;
          for (double price: prices) {
               totalPrice += price;
          }
          return totalPrice;
     }

     /* void displayMenu(ArrayList<String> menuItems)
     given ArrayList of strings, print each inde and menu item
     String name = myArray.get(0) --> accessing element */

     public void displayMenu(ArrayList<String> menuItems) {
          for (String item : menuItems) {
               System.out.println(item);
          }
     }

     /* addCustomer(ArrayList<String> customers)
     print please enter your name
     String userName = System.console().readLine()
     print username and say hello, and print # of people in line
     print the list, no need to return anything
     myArray.add("Heidi"); --> adds item to arraylist*/

     public void addCustomer(ArrayList<String> customers) {
          System.out.println("Please enter your name");
          String userName = System.console().readLine();
          System.out.println("Hello, " + userName);

          System.out.println("There are " + customers.size() + " people in front of you.");
          customers.add(userName);
          System.out.println("New List is: " + customers);
     }

     public void printPriceChart(String product, double price, int maxQuantity) {
          System.out.println(product);
          for (int i = 1; i < maxQuantity; i++) {
               System.out.printf("%s - %s\n", i, price * i);
          }
     }
}