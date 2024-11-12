# Aufgabe 1b

import time
import random

population: int = 1_000_000

# generating a random number from the given population
random_number: int = random.randrange(population)

# generating a random list of size 100 from the given population
random_list: list[int] = random.sample(range(population), k=100)

# generating a random set of size 100 from the given population
random_set: set[int] = set(random.sample(range(population), k=100))

# time the for loop operation on the list
list_time_start: float = time.time()
# check for each number in random_list if this number is same as the random_number generated above
for number in random_list: 
    if number == random_number:
        print("Found")
        break
# else block will only run if break has not ran already, meaning if the number has not been found
else:
    print("Not Found")
list_time_end: float = time.time()
total_list_time: float = list_time_end - list_time_start

# same logic as list but on set
set_time_start: float = time.time()
for number in random_set:
    if number == random_number:
        print("Found")
        break
else:
    print("Not Found")
set_time_end: float = time.time()
total_set_time: float = set_time_end - set_time_start

print(f"{total_list_time = }")
print(f"{total_set_time = }")