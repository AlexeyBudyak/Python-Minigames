# Cookies
import random 
name = input("What is your name? ")
cookies = random.randint(0,10)
s = 's' * (cookies != 1)
pics = '🍪' * cookies
print(f'{name}, you can eat {cookies} cookie{s} {pics}')
