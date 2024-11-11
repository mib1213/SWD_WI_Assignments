# Ex 3b

numbers: list[int] = [1, 4, 2, 8, 5]

# instantiating an empty list that will be filled later in the while loop
squared_numbers: list[int] = []

i: int = 0 # starting the counter from 0
while i < len(numbers): # as long as the counter does NOT arrive the len(numbers) which is 5 
                        # in this case so it will run 5 times because the counter starts from 0
    squared_numbers.append(numbers[i]**2) #index the value at index i and take the square
    i += 1 # increase the counter by 1 on every iteration

print(squared_numbers)