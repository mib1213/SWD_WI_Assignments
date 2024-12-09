import random

interval_anfang = int(input("Interval anfang: "))
interval_ende = int(input("Interval ende: "))

zufällige_zahl = random.randint(interval_anfang, interval_ende)

for _ in range(5):
    benutzer_eingabe = int(input("Deine Rate: "))
    if benutzer_eingabe == zufällige_zahl:
        print("Du hast gewonnen!")
        break