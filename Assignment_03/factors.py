# Ex 3b

# take the input for the number of factors
n_factors: int = int(input("Number of factors: "))

# create a list of factors from 1 to n times
factors: list[int] = [i for i in range(1, n_factors + 1)]

# take the input for the multiplier
num: int = int(input("Multiplier: "))

# using list compresension and multiply the num' to each member of factors that is getting stored in i
multiplied_list: list[int] = [i*num for i in factors]
multiplied_list: list[int] = [i*num for i in factors]

print(multiplied_list)#