# Ex 3c

import random
secret_number = random.randint(1, 100) # Generate random number
def gen():
    i = 0 
    while True:
        yield i
        i += 1

for i in gen():
    guess = int(input("Guess a number btw 1 and 100: "))
    if guess > secret_number:
        print("Too high, guess again")
    elif guess < secret_number:
        print("Too low, gues again")
    else:
        print(f"You guessed it, the number was {secret_number}")
        break