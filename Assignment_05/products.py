# Aufgabe 2

parts: list[tuple[int|str]] = [
    (1, '500-1', 'Hammer', 2, 'Pieces'),
    (2, '503', 'Screwdriver', 3, 'Pieces'),
    (3, '555', 'Nail', 10, 'Pieces')
]
# use a dictionary comprehension that iterates over each tuple of the list 'parts', add
# 1st index from the current tuple as key and 3rd and 4th index as tuple as value
products_dict: dict[str:tuple[int|str]] = {product[1]: (product[3], product[4]) for product in parts}

print(products_dict)