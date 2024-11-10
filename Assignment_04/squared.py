# Ex 3b

numbers: list[int] = [1, 4, 2, 8, 5]
squared_numbers: list[int] = []

i: int = 0
while i < len(numbers):
    squared_numbers.append(numbers[i]**2)
    i += 1

print(squared_numbers)