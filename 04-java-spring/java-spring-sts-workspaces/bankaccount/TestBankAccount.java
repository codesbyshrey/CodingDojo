public class TestBankAccount {
     public static void main (String[] args) {
          BankAccount shreyFidelity = new BankAccount();
          System.out.println(shreyFidelity.numberOfAccounts);

          shreyFidelity.deposit(125000, "checking");
          shreyFidelity.deposit(250000, "savings");
          System.out.println(shreyFidelity.getCheckingBalance());
          System.out.println(shreyFidelity.getSavingsBalance());
          System.out.println(shreyFidelity.getTotal());

          System.out.println("DEPOSIT FUNCTIONS HAVE BEEN TESTED");

          shreyFidelity.withdraw(100000, "checking");
          shreyFidelity.withdraw(200000, "savings");
          System.out.println(shreyFidelity.getCheckingBalance());
          System.out.println(shreyFidelity.getSavingsBalance());
          System.out.println(shreyFidelity.getTotal());

          System.out.println("WITHDRAW FUNCTIONS HAVE BEEN TESTED");

          shreyFidelity.withdraw(100000, "checking");
          shreyFidelity.withdraw(200000, "savings");

          BankAccount shreyChase = new BankAccount();
          System.out.println(BankAccount.numberOfAccounts);
     }
}

/* NINJA BONUS 
1. add an account number class attribute
2. create private method that returns random 10 digit #
3. in constructor, call the private method from 2
     so that each user has a random ten digit account number
*/