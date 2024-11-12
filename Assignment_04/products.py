# Ex 1b

parts: list[tuple[int|str]] = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503',
'Screwdriver', 3, 'Pieces')]

# i returns a tuple on each iteration, then we index 3rd element on the tuple to get the product name
names: list[str] = [i[2] for i in parts]
print(names)

