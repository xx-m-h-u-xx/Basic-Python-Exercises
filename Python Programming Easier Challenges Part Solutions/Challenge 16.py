import random
number = (random.randint(0,100))
attempts=1
print('Can you guess my number between 1 and 100?')
print('If you do not get the number in three goes then do not count on seeing your home country again!')
guess=input('So giz a guess, any guess...')

while (int(guess)<int(number)):
    print('WRONG LOSER. Go HIGHER babes!')
    guess=input('Giz another guess, come on, any guess')
    attempts=attempts+1
    while (int(guess)>int(number)):
        print ('WRONG LOSER. Go LOWER babes!')
        guess=input('Giz a guess, any guess')
        attempts=attempts+1

if(int(guess)==int(number)):
    print('Cheating Plonker. I will find YOU!!!!!!!!')
    print('It took you '+str(attempts)+' attempts to get it. FAIL!')
    


