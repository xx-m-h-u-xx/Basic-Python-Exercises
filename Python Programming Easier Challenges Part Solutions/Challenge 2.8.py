#Rolling The Dice
import time
import random

i=input("Would you like to roll the die?")
while i==("yes"):
    n=random.randint(1,6)
    print(n)
    i=input("Would you like to roll the die?")
else:
    print("Goodbye")
    
    
    

