def main() -> None:
    eingabe: str = input("Satz: ")
    wort_ohne_sonderzeichen: str = lösche_sonderzeichen(eingabe)
    print(ist_palindrome(wort_ohne_sonderzeichen))
    return

def lösche_sonderzeichen(wort: str) -> str:
    return ''.join([char for char in wort if char.isalnum()])

def ist_palindrome(wort: str) -> bool:
    wort = wort.lower()
    return wort == wort[::-1]
    
if __name__ == '__main__':
    main()