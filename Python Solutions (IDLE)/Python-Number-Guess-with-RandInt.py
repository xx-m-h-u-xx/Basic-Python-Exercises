minimum_number = int(input("Enter a number between 10 to 20"))
if minimum_number < 10:
    print("Enter a number between 10 to 20 again")
    if minimum_number > 20:
        print("Enter a number between 10 to 20 again")
maximum_number = int(input("Enter a number between 40 to 50"))
import random
minimum_number = random.randint(10,20)
guess=int(input("Take a guess:"))
tries = 1
while guess != minimum_number:
    if guess > number:
        print("Lower...")
    if guess < number:
        print("Higher...")
    guess=int(input("Guess now:"))
    tries=tries+1
print("You Got It! it was",number)
print("you took",tries,"tries!")
