# Ex 3c

n: int = int(input("Number for list: "))

my_list: list[int] = [i for i in range(1, n+1)]

evens: list[int] = [i for i in my_list if i % 2 == 0]
odds: list[int] = [i for i in my_list if i % 2 != 0]

print("Original List:", my_list)
print("Even:", evens)
print("Odd:", odds)