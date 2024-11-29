längen: list[int] = list(range(1, 11))
breiten: list[int] = list(range(11, 21))


def fläche_berechnen(lange: int, breite: int):
    return lange * breite


flächen = [fläche_berechnen(längen[i], breiten[i]) for i in range(len(längen))]

def preise_berechnen(fläche, preis, steuer):
    nettopreis = fläche * preis
    bruttopreis = nettopreis * (1 + steuer)
    return nettopreis, bruttopreis

for fläche in flächen:
    nettopreis, bruttopreis = preise_berechnen(fläche, 50, 0.035)
    print("Fläche:", fläche, "Nettopreis:", nettopreis, "Bruttopreis:", bruttopreis)