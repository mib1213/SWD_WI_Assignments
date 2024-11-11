# Ex 2

# take the input for the number of words
n: int = int(input("Number of words: "))

# create an empty list to store the words
words: list[str] = []

# run while loop for n number of times
while n > 0:
    # take the input each time while loop runs
    word: str = input("Word: ")
    words.append(word)
    # decrement the value by 1 so it reaches to 0 after n times
    n -= 1

# create a int instance to store the length of all the words
length: int = 0

# run for loop for each word in the list of words
for word in words:
    # add the length of each word to the length variable
    length += len(word)
print(length)
