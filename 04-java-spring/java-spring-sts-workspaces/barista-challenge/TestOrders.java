import java.util.ArrayList;

public class TestOrders {
     // entry point
     public static void main(String[] args) {

          // MENU ITEMS
          Item item1 = new Item();
          item1.name = "mocha";
          item1.price = 3.5;

          Item item2 = new Item();
          item2.name = "latte";
          item2.price = 4.25;

          Item item3 = new Item();
          item3.name = "drip coffee";
          item3.price = 4.0;

          Item item4 = new Item();
          item4.name = "capuccino";
          item4.price = 3.75;

          // ORDER VARIABLES
          Order order1 = new Order();
          order1.name = "Cindhuri";
          ArrayList<Item> cindhuriItems = new ArrayList<>();
          // System.out.println(order1.total); //prints 0.0 as expected

          Order order2 = new Order();
          order2.name = "Jimmy";
          ArrayList<Item> jimmyItems = new ArrayList<>();

          Order order3 = new Order();
          order3.name = "Noah";
          ArrayList<Item> noahItems = new ArrayList<>();

          Order order4 = new Order();
          order4.name = "Sam";
          ArrayList<Item> sameItems = new ArrayList<>();

          // APPLICATION RUN
          
          // add item1 to order2's item list and increase order total
          order2.items.add(item1);
          order2.total += item1.price;

          // order3 orders capuccino, add to order and tab
          order3.items.add(item4);
          order3.total += item4.price;

          //order4 aded a latte
          order4.items.add(item2);
          order4.total += item2.price;

          // Cindhuri's order is ready
          order1.ready = true;

          // Sam orders 2 more lattes
          order4.items.add(item2);
          order4.items.add(item2);
          order4.total += (item2.price * 2);

          // Jimmy's order is ready, update status
          order2.ready = true;

          // System print lines to test outputs and updates
          System.out.printf("Name: %s\n", order1.name);
          System.out.printf("Total: %s\n", order1.total);
          System.out.printf("Ready: %s\n", order1.ready);

          System.out.printf("Name: %s\n", order2.name);
          System.out.printf("Total: %s\n", order2.total);
          System.out.printf("Ready: %s\n", order2.ready);

          System.out.printf("Name: %s\n", order3.name);
          System.out.printf("Total: %s\n", order3.total);
          System.out.printf("Ready: %s\n", order3.ready);

          System.out.printf("Name: %s\n", order4.name);
          System.out.printf("Total: %s\n", order4.total);
          System.out.printf("Ready: %s\n", order4.ready);
     }
}

/* COFFEEDORE 64 */
// new class called CoffeeKiosk with menu and orders ArrayList of objects
// methods of addMenuItem, displaymenu, newOrder (console input w/ String)
// Ninja Bonus --> addMenuItemByInput



/* BARISTA'S CHALLENGE */
// set member variables to private, and add constructor w/ String, name, double
// create getters and setters for all member variables
// overloaded consutrctor for order as well
// order class methods --> addItem, getStatusMessage, getOrderTotal, display
// create 2 orders for unspecified guests, then 3 with names provided
// implement addItem method
// add at least 2 items to each order using addItem
// implement and test other methods
// test total by printing return value, and call display on all the orders



/* ORDERS AND ITEMS */ 
// create 4 items variables of item
// set name and price for each
     // mocha, latte, drip coffee, and capuccino
// 4 order variables to instantiate
     // Cindhuri, Jimmy, Noah, Sam
// print order1 variable to console
// predice what happens if print order1.total
// add item1 to order2 item and increment order total
// order3 has a cappucino to add to tab
// order4 adds a latte
// Cindhuri's order is now ready
// Sam ordered 2 lattes, update the order
// Jimmy's order is now ready, update status