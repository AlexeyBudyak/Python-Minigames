import random 

name = input('What is your name? ')
print(f'Hello {name}!')
print()
print(f"{name}, let's play a game!")
task = input("What's your task? ")
pro = random.randint(0,100)
contro = 100 - pro
pro = str(pro)
contro = str(contro)
print('Voting for this task')
print('Pro: ' + pro + '%')
print(f'Contro {contro}%')
