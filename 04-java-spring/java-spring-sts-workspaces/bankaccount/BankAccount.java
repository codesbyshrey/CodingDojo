public class BankAccount {
     // ATTRIBUTES ------------------------------------------
          // users can't set any of the attributes from the class
     // double w/ checking and savings
     private static double checkingBalance;
     private static double savingsBalance;

     // static class member w/ number of accounts
     public static int numberOfAccounts;

     // static class member w/ total money in every account
     private static double total;

     // CONSTRUCTORS ----------------------------------------
     // make sure to increment account count
     public BankAccount() {
          BankAccount.numberOfAccounts ++;
     }

     // METHODS ---------------------------------------------
     // allow user to deposit money into either account
     public void deposit (double amount, String account) {
          if(account.indexOf("che") >= 0) {
               this.checkingBalance += amount;
               this.total += amount;
          }
          else if(account.indexOf("sav") >= 0) {
               this.savingsBalance += amount;
               this.total += amount;
          }
     }

     // method for withdrawal, no can do if insufficient funds
     public void withdraw(double amount, String account) {
          if ((account.indexOf("che") >= 0) && (this.checkingBalance > amount)) {
               this.checkingBalance -= amount;
               this.total -= amount;
          }
          else if ((account.indexOf("sav") >= 0) && (this.savingsBalance > amount)) {
               this.savingsBalance -= amount;
               this.total -= amount;
          }
          else {
               System.out.println("You have insufficient funds.");
          }
     }

     // see total values
     public double getTotal() {
          return this.total;
     }

     // SETTERS AND GETTERS ---------------------------------
     // getter for checking and saving account balance

     public double getCheckingBalance() {
          return this.checkingBalance;
     }
     public double getSavingsBalance() {
          return this.savingsBalance;
     }

}