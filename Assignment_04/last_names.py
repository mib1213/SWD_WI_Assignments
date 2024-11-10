# Ex 3a

customers = [
["Max", "Mustermann", "01.01.83"],
["Martina", "Musterfrau", "02.02.84"],
["Gabi", "Meier", "03.03.85"]
]
last_names = []
for customer in customers:
    last_names.append(customer[1])
print(last_names)