import random

def greeting(name):
  return f'Hello {name} weclome to heads or tails!'

name = input ("What's your name? ")
text = greeting(name)
print (text)
rnd=random.randint(0,1)
player = input ("what's your choice? Heads or Tails? ")
coin = 'Heads'
if rnd == 1:
    coin == 'Tails'
if player == coin:
    print("you won yay!!!!!!!")
else:
    print ('you lost and i won hahahahaha')
