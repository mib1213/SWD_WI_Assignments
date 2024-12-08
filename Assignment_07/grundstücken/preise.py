def netto_preis_berechnen(fläche: int | float, preis: int | float = 50) -> int | float:
    """
    Eine Funktion, um den Nettopreis der Fläche zu berechnen.
    """
    return fläche*preis

def brutto_preis_berechnen(nettopreis: int | float, steuer: float = 0.035) -> float:
    """
    Eine Funktion, um aus dem Nettopreis den Bruttopreis auf Basis der Steuer zu berechnen.
    """
    return nettopreis * (1 + steuer)