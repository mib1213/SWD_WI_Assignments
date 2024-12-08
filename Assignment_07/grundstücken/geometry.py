# Aufgabe 1a

from preise import netto_preis_berechnen, brutto_preis_berechnen
from fläche import fläche_berechnen

# ich habe angenommen, dass die Werte von Grundstücke sowie die Preise die beide Datentypen "int" 
# und "float" haben können

def main() -> None:
    # Beispiel Liste für 3 Grundstücke als 3 Tuple mit jeweils ihrer (Länge, Breite) 
    grundstücke: list[tuple[int | float]] = [(10, 10), (10, 15), (15, 20)]

    # List Comprehension um die Fläche jeder Gründstücke zu appenden, der von der Funktion 'fläche_berechnen'
    # zurückgegeben wird
    flächen: list[int | float] = [fläche_berechnen(länge, breite) for länge, breite in grundstücke]

    for fläche in flächen:
        # ein Tupel von (nettopreis, bruttopres) als Rückgabewert von der Funktion 'preise_berechnen'
        nettopreis: int | float = netto_preis_berechnen(fläche, 1)
        bruttopreis: float = brutto_preis_berechnen(nettopreis, 0.1)

        # interessenterweise würde die Floatextension ":.0f" sogar mit "int" Typ funktionieren und man
        # wird keine Fehlermeldung bekommen, falls die Variablen "int" Typ sind.
        print(f"Fläche = {fläche:.0f}; Nettopreis = {nettopreis:.0f}; Bruttopreis = {bruttopreis:.0f}")
    return

if __name__ == '__main__':
    main()