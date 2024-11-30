# Aufgabe 1

def main() -> None:
    # Beispiel Liste für 3 Grundstücke als 3 Tuple mit jeweils ihrer (Länge, Breite) 
    grundstücke: list[tuple[int | float]] = [(10, 10), (10, 15), (15, 20)]

    # List Comprehension um die Fläche jeder Gründstücke zu appenden, der von der Funktion 'fläche_berechnen'
    # zurückgegeben wird
    flächen: list[int | float] = [fläche_berechnen(länge, breite) for länge, breite in grundstücke]

    for fläche in flächen:
        # ein Tupel von (nettopreis, bruttopres) als Rückgabewert von der Funktion 'preise_berechnen'
        preis: tuple[int | float] = preise_berechnen(fläche, 1, 0.1)
        # Nettopreis bzw. Bruttopreis in dem Tuple an der Stelle 0 bzw. 1 indexen und in einer Variable speichen 
        nettopreis: int | float = preis[0]
        bruttopreis: float = preis[1]
        print(f"Fläche = {fläche:.0f}; Nettopreis = {nettopreis:.0f}; Bruttopreis = {bruttopreis:.0f}")
    return

def fläche_berechnen(länge: int | float, breite: int | float) -> int | float:
    """
    Eine Funktion, um die Fläche von der Länge und Breite zu berechnen.
    """
    return länge * breite

def preise_berechnen(fläche: int | float, preis: int | float = 50, steuer: float = 0.035) -> tuple[int | float]:
    """
    Eine Funktion, um den Netto- und Bruttopreis auf der Basis von Grundpreis, Steuer und Fläche 
    zu berechnen.
    """
    nettopreis: int | float = fläche * preis
    bruttopreis: float = nettopreis * (1 + steuer)
    return nettopreis, bruttopreis

if __name__ == '__main__':
    main()