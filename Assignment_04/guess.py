# Ex 3c

import random
secret_number: int = random.randint(1, 100) # Generate random number

# create a generator that generates the next number starting from 0
def gen():
    i = 0 
    while True:
        yield i
        i += 1

# using for loop with gen() makes sure that the for loop will run forever
for i in gen():
    guess: int = int(input("Guess a number btw 1 and 100: "))
    if guess > secret_number:
        print("Too high, guess again")
    elif guess < secret_number:
        print("Too low, gues again")
    else:
        print(f"You guessed it, the number was {secret_number}")
        # once the user has guessed the right number break the for loop
        break