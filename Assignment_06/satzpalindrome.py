# Aufgabe 3b

def main() -> None:
    eingabe: str = input("Satz: ")
    wort_ohne_sonderzeichen: str = lösche_sonderzeichen(eingabe)
    print(ist_palindrome(wort_ohne_sonderzeichen))
    return

# durch diese Funktion werden alle Sonderzeichen aus einem Str gelöscht.
def lösche_sonderzeichen(wort: str) -> str:
    # prüft zuerst ob jedes Zeichen in einem Str "Alphanumeric" Typ ist und falls ja, wird es 
    # zu einer Liste appended, am Ende wird diese Liste zu nochmal einem Str umgewandelt 
    # mit der Funktion ''.join.
    return ''.join([char for char in wort if char.isalnum()])

# diese Funktion vergleicht der Str mit seiner Umkehrung und wenn die beide gleich sind, wird True
# zurückgegeben.
def ist_palindrome(wort: str) -> bool:
    wort = wort.lower()
    return wort == wort[::-1]
    
if __name__ == '__main__':
    main()