# Ex 2

numbers: list[int] = []

user_input: str = ''
while user_input != 'stop':
    user_input = input("Number: ")
    if user_input != 'stop':
        numbers.append(int(user_input))
    
print('numbers =', numbers)

maximum: int = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

minimum: int = numbers[0]
sum: int = 0

for number in numbers:
    if number < minimum:
        minimum = number
    sum += number

mean: float = sum / len(numbers)

print(f"{minimum = }")
print(f"{maximum = }")
print(f"{mean = }")