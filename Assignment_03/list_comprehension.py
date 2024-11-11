# Ex 3a

# take the input for the user specified character
char: str = input("Character: ")

# take the input for the number of times the character should be printed
n: int = int(input("Number: "))

# list comprehension
# using * operator to repeat the character n times
# range should start from 1 to n+1 because 0 is not needed and last number in range is exclusive

chars: list[str] = [char*i for i in range(1, n+1)]
print(chars)