# Ex 3c

# Disclaimer: The program only deals with Natural Numbers

# take the input for the number of words
n: int = int(input("Size of a list: "))

# generate a list of numbrers from 1 to the user_input n, it will generate n amount of numbers
my_list: list[int] = [i for i in range(1, n+1)]

# using list comprehension filter out the evens after checking if their modulo with 2 is 0
evens: list[int] = [i for i in my_list if i % 2 == 0]

# similarly filter out the adds but this time check if the modulo with 2 is not 0
odds: list[int] = [i for i in my_list if i % 2 != 0]

print("Given List:", my_list)
print("Even:", evens)
print("Odd:", odds)