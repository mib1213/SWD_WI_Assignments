# Ex: 4

user_input = input("Give a short text: ").strip().replace(',', '').replace('.', '')

# split the user_input on blank ' ' and save the returned value in a list which will give all words separated by a space

words: list[str] = user_input.split(' ')

# initiate an empty dict that will be filled in the for loop
counts_dict: dict[str: int] = {}

# iterate over words in the words list to get each word in the word variable
for word in words:
    # update the dict value for each word to its count
    counts_dict[word] = len(word)

print("Given input:", user_input)
# print each member of the dict
for i in counts_dict:
    print(f"{i}: {counts_dict[i]}")

