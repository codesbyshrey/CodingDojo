
import BankAccount from bank_account

# Users w/ Bank Accounts Assignment:
     #create a user class that has an association with the BankAccount class. You should not have to change anything in the BankAccount Class.

class User:
     def __init__(self, name, email):
          self.name = name
          self.email = email
          self.account = BankAccount(int_rate=0.02, balance=0)
     
     # other methods
     
     def make_deposit(self, amount):
          self.account.deposit(amount)
          return self

     def make_withdraw(self, amount):
          self.account.withdraw(amount)
          return self
     
     def display_user_balance (self):
          print ("Your balance is: ", self.account.balance)

# User doesn't have self.account_balance. But it does have an isntance by the name of self.account. So all you're realy doing is mirroring the methods created in the BankAccount class that self reference self.account_blanace. The BA class would be doing most the work, so there should be limited logic to add.