def main() -> None:
    eingabe: str = input("Wort: ")
    if ist_palindrome(eingabe):
        print("Es ist ein Palindrome")
    else:
        print("Es ist kein Palindrome")
    return

# diese Funktion vergleicht einen Str mit seiner Umkehrung und falls sie gleich sind, wird True 
# zurückgegeben.
def ist_palindrome(wort: str) -> bool:
    wort = wort.lower()
    return wort == wort[::-1]

if __name__ == '__main__':
    main()