# Ex 2

n: int = int(input("Number of words: "))

words: list[str] = []
while n > 0:
    word: str = input("Word: ")
    words.append(word)
    n -= 1

length: int = 0
for word in words:
    length += len(word)
print(length)
