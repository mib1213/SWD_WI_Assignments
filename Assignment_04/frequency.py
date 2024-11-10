#Ex: 4

user_input = input("Give a short text: ").strip().replace(',', '').replace('.', '')

words = user_input.split(' ')
counts_dict = {}
for word in words:
    counts_dict[word] = words.count(word)

for i in counts_dict:
    print(f"{i}: {counts_dict[i]}")

print(user_input)