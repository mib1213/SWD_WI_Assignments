# Ex 3a

customers = [
["Max", "Mustermann", "01.01.83"],
["Martina", "Musterfrau", "02.02.84"],
["Gabi", "Meier", "03.03.85"]
]

# initiating en empty list object that will be updated in the for loop
last_names: list[str] = []

for customer in customers:
    # customer variable has a list on every iteration
    last_names.append(customer[1]) # index the 2nd value (Index 1) on each list that the
                                   # customer variable holds on each iteration
print(last_names)