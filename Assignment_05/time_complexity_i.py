# Aufgabe 1a

import random

population: int = 1_000_000

# generating a random sample of 100 from the given range of population
random_list: list[int] = random.sample(range(population), k=100)

# generating a random sample of 100 and convert it to set since it random.sample returns a list
random_set: set[int] = set(random.sample(range(population), k=100))

print(f"{random_list = }")
print(f"{random_set = }")