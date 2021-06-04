# Just for lerning classes

import random

class Account():
  def __init__ (self, owner, balance = 0):
    self.owner = owner
    self.balance = balance
  def deposit(self, dep_amt):
    self.balance = self.balance + dep_amt
    print(f'Added ${dep_amt} to the balance')
  def gambling(self, gm_amt):
    if random.randint(0,90) > 50:
      self.balance = self.balance + (gm_amt * 2)
      print('You won!')
      print(f'Added ${gm_amt} to the balance')
    else:
      print('You lose!')
  def withdrawal(self, wd_amt):
    if self.balance >= wd_amt:
      self.balance = self.balance - wd_amt
      print(f'Withdrawn ${wd_amt}')
      return True
    else:
      print('Sorry non enough funds!')
      return False
  def __str__(self):
    return f'Owner: {self.owner} \nBalance: {self.balance}'

name = input("What's your name? ")
print(f"{name}, let's play cazino! Bank gives you $1000 credit!")
money = Account(name, 1000)
choice = '';

while choice != 'x':
  print('How much would you like put on risk?')
  print('Enter "b" for balance  or enter "x" for exit')
  choice = input()
  if choice.isdigit():
    if money.withdrawal(int(choice)):
      money.gambling(int(choice))
  if choice == 'b':
    print(money)
print(money)
print('You need pay back $1000 to bank.')
if money.balance < 1000:
  print('You are a bankrupt')
else:
  money.withdrawal(1000)
  print(money)
