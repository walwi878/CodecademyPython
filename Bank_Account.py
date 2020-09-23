"""
Bank Account class allows user's mank account to accept deposits and withdrawals, 
and print the bank account's balance and details

@author William Wallace
@date 1/05/2020
"""

class BankAccount(object):
  
  total = 0
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "This account belongs to %s and it's balance is $%.2f" % (self.name, self.total)
  
  
  def show_balance(self):
    print "Your balance is: $%.2f" % self.total
  
  def deposit(self, amount):
    if amount <= 0:
      print "Cannot deposit amounts less than or equal to zero dollars."
      return
    else:
      print "You are depositing $%.2f" % amount
      self.total += amount
      self.show_balance()
  
  def withdraw(self, amount):
    if amount <= 0:
      print "Cannot withdraw amounts less than or equal to zero dollars."
      return
    elif amount > self.total:
      print "Cannot withdraw more than your banks balance."
      return
    else:
      print "You are withdrawing $%.2f" % amount
      self.total -= amount
      self.show_balance()
  
my_account = BankAccount("William")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(61)
print my_account