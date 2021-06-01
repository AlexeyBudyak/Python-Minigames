# Rock, Paper, Scissors 
import random 

print(f'Let\'s play a game "Rock, Paper, Scissors"!')
print('Enter your choice')
player1 = input('Rock(R), Paper(P), Scissors(S) ')
player1 = 'PS'.find(player1.upper()[0]) + 1
player2 = random.randint(0,2)
figs = ['Rock','Paper','Scissors','Rock']
print('Player1 (You):',figs[player1])
print('Player2 (Computer):',figs[player2])
if(player1 == player2):
  print("It's a tie!")
elif figs[player2 + 1] == figs[player1]:
  print("You won!")
else:
  print("I'm won!")
