# Shreyas Sriram Bank Account
"""
Ninja Bonus Still Remaining at Time of Submission:
- use a classmethod to print all instances of a BankAccount's info
"""

class BankAccount:
     # don't forget to add some default values for these parameters!
     # balance starts at 0 unless overridden in the new instance declaration
     # for now interest rate is established with decimal inputs
     # self.int_rate = int_rate / 100 --> in case we want to define our function input with whole numbers for ease of use
     def __init__(self, int_rate, balance = 0): 
          self.int_rate = int_rate
          self.balance = balance

     def deposit(self, amount):
          # increases the account balance by the given amount
          self.balance += amount
          return self

     def withdraw(self, amount):
          # decrease by given amount, fees if overdrawn
          # decrease the balance by overdrawn fee prior to printing the new balance, otherwise it won't reveal properly
          if self.balance >= amount:
               self.balance -= amount
          else:
               self.balance -= 5
               print(f"Insufficient funds: Charging a $5 fee{self.balance}")
          return self

     def display_account_info(self):
          #print to the console that balance is 100
          print("Your Balance Is:", self.balance)
          return self

     def yield_interest(self):
          # increase the account balance with the interest rate as long as the balance of the account is positive
          if self.balance > 0:
               self.balance += self.balance * self.int_rate
          return self

# Chain the functions for user 1 to make 3 deposits and 1 withdrawal, yield interst, and display accounts info in one line of code (chaining)

Robert = BankAccount(0.1)
Robert.deposit(200).deposit(150).deposit(250).withdraw(450).yield_interest().display_account_info()

# Make 2 deposits and 4 withdrawals, then yield interest to display the accounts info all in one line of code (chaining)

Downey = BankAccount(0.25)
Downey.deposit(200).deposit(150).withdraw(25).withdraw(25).withdraw(50).withdraw(100).yield_interest().display_account_info()

# Quick test to ensure our failure function still works and we are charged a fee
Junior = BankAccount(0.5)
Junior.deposit(100).deposit(100).withdraw(100).withdraw(90).display_account_info()
Junior.withdraw(11).display_account_info()