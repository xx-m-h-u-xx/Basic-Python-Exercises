print("Welcome to Guess My Number!")
print("I'm thinking of a number between 1 and 100.")
import random
number = random.randint(1,100)
guess=int(input("Take a guess:"))
tries = 1
while guess != number:
    if guess > number:
        print("Lower...")
    if guess < number:
        print("Higher...")
    guess=int(input("Guess now:"))
    tries=tries+1
print("You Got It! it was",number)
print("you took",tries,"tries!")
