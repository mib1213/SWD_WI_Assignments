# Ex 3b

n_factors: int = int(input("Number of factors: "))
factors: list[int] = [i for i in range(1, n_factors + 1)]

num: int = int(input("Multiplier: "))

multiplied_list: list[int] = [i*num for i in factors]

print(multiplied_list)