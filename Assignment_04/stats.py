# Ex 2

# instantiate an empty list object
numbers: list[int] = []

# instantiate an empty string object because it is needed to for the while loop
user_input: str = ''
while user_input != 'stop': # the while loop will run until user_input is NOT equals to 'stop'
    user_input = input("Number: ") # taking input everytime for each while loop iteration
    if user_input != 'stop': # as long as the user does not type 'stop',
        numbers.append(int(user_input)) # keep appending the numbers to the list
    
print('numbers =', numbers)

# assuming maximum is the first number in the list
maximum: int = numbers[0]
for number in numbers: # assign the value of the number in number variable
    if number > maximum: # check if the number from the list is greater than the assumed maximum
                         # in first case it is our assumed max i.e. the first number
        maximum = number # if the number is greater than our assumed number that update the maximum
                         # value to the new number
                         # keep checking the condition until all the numbers are iterated 

# the same logic of maximum is applied to calculate the minimum as well
minimum: int = numbers[0]
# for the sum, starts the sum from 0 and add the value of the number on each iteration
sum: int = 0
for number in numbers:
    if number < minimum:
        minimum = number
    sum += number

# mean is the calculated sum divided by the number of numbers or length of numbers list
mean: float = sum / len(numbers)

print(f"{minimum = }")
print(f"{maximum = }")
print(f"{mean = :.2f}") # because mean is a float, it should print only the 2 decimal places