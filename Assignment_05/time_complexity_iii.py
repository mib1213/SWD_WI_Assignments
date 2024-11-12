# Aufgabe 1c

import random
import time

def main() -> None:
    # range of 0 to 1_000_000
    population: int = 10_000_000

    # specified samples
    samples: list[int] = [10_000, 100_000, 500_000, 1_000_000]

    # generating 4 lists and 4 sets for specified 4 samples and add all 4 produced lists in a 
    # another list called 'list_of_lists', similarly all 4 produced sets in another list called
    # 'list_of_sets'

    list_of_lists: list[list[int]] = []
    list_of_sets: list[set[int]] = []
    for sample in samples:
        list_of_lists.append(random.sample(range(population), k=sample))
        list_of_sets.append(set(random.sample(range(population), k=sample)))

    # using the function 'time_it' generate time for each case and add it to a list
    list_times: list[float] = []
    set_times: list[float] = []
    for i in range(4):
        list_times.append(time_it(population, list_of_lists[i], 1000))
        set_times.append(time_it(population, list_of_sets[0], 1000))

    # print the times in the list
    for i in range(1, 5):
        print(f"list_{i} took {list_times[0]:.5f} seconds")
        print(f"set_{i} took {set_times[0]:.5f} seconds")
    
    return

# define a function that's purpose is to time the operation in each of the 8 cases
def time_it(population: range, sample: list[int] | set[int], repeat: int) -> float:
    """
    The function times the search of a random integer from a specified population in a 
    given sample specified number of times and then return the time taken as float in seconds
    """
    t1: float = time.time()
    for _ in range(repeat):
        if (random_number := random.randrange(population)) in sample:
            print(f"{random_number} found")
    t2: float = time.time()
    return t2 - t1

if __name__ == '__main__':
    main()