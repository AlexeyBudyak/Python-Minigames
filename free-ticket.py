import random
#US flag
#print ('US Flag')
def flag_us():
  line = '*' * 10 + '⬛' * 30 + '\n'
  block = line * 5
  line2 = '⬛' * 40 + '\n'
  block2 = line2 * 6
  flag = block + block2
  print(flag)

#print()
#print('ukraine flag')
def flag_ukraine():
  line = 'E' * 40 + '\n'
  block = line * 6  
  line2 = '⬛' * 40 + '\n'
  block2 = line2 * 6 
  flag = block + block2
  print(flag)

#print()
#print ('Russian flag ')
def flag_russian():
  line = 'E' * 40 + '\n'
  block = line * 4  
  line2 = '⬛' * 40 + '\n'
  block2 = line2 * 4 
  line3 = 'V' * 40 +'\n'
  block3 = line3 * 4
  flag = block + block2 + block3
  print(flag)

#print()
#print('Italian flag')
def flag_italian():
  line = 'Z' * 13 + 'V' * 13 + 'W' * 13 + '\n'
  block = line * 10
  print(block)


 

ticket = random.randint(0,3)
print (ticket)
countries = ['US', 'Russia', 'Ukraine', 'Italy']
country = countries[ticket]
print (f"you won a ticket to {country}")
if ticket == 0: flag_us()
if ticket == 1: flag_russian()
if ticket == 2: flag_ukraine()
if ticket == 3: flag_italian()
