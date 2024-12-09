# Aufgabe 3

import random

intervall_anfang: int = int(input("Interval anfang: "))
intervall_ende: int = int(input("Interval ende: "))

# erzeuge ein Tuple von dem Range von dem Benutzer eingegebenen Intervallen, da diese Tuple auch
# noch später gebraucht wird, nicht eine Liste weil das ja unverändert bleiben muss
intervall: tuple[int] = tuple(range(intervall_anfang, intervall_ende + 1))

# könnte man hier random.randint verwenden, aber da ich schon die Zahlen als Intervall gespeichert habe,
# macht es mehr Sinn, random.choice() zu verwenden
zufällige_zahl: int = random.choice(intervall)

for _ in range(5):
    # Fehlerkontrolle falls der Benutzer eine Zahl eingibt, die sogar nicht in dem Intervall liegt
    while True:
        try:
            benutzer_eingabe: int = int(input("Deine Rate: "))
            if benutzer_eingabe not in intervall:
                raise ValueError(f"Eingabe liegt nicht in dem Interval von {intervall_anfang} - {intervall_ende}")
            break
        except ValueError as ve:
            print(ve, "versuche normal")
    if benutzer_eingabe == zufällige_zahl:
        print("Du hast gewonnen!")
        # falls diese Bedingung Wahr ist, muss die FOR Schleife nicht weiter laufen
        break
    elif benutzer_eingabe < zufällige_zahl:
        print("Höher")
    else:
        print("Kleiner")
else: # diese ELSE wird nur ausgeführt, wenn in der FOR Schleife KEIN 'break' ausgeführt wurde
    print("Du hast verloren")