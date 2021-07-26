all_food = [] 
food = input('Enter food on any letter ').lower()
all_food.append(food)
letter = food[-1]
fails = 0

while food != 'x':
  food = input(f'Enter food on letter "{letter}" or "X" for exit ').lower()
  if food[0] != letter and food != 'x':
    print('Wrong first letter!')
    fails+= 1
  if food in all_food:
    print('Sorry, we already ate this')
    fails+= 1
  else:
    all_food.append(food)
    # all_food+= [food]
    letter = food[-1]
  if fails == 3:
    print('You failed!')
    break

print('Game Over!')
print(f'You have eaten: {", ".join(all_food)}')
