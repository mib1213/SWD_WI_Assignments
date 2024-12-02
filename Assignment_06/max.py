# für die Max Funktion im Allgemeinen habe ich mir überlegt, ob sie im Fall, wenn alle Zahlen gleich 
# sind, None zurückgeben soll, aber diese Vorgehensweise macht das Program einfach zu lang, deswegen habe 
# ich hier so gemacht, dass falls alle Zahlen gleich sind, wird die Funktion einfach die Zahl zurückgibt,
# was tatsächlich in vielen Fällen sogar hilfreicher sein könnte.

def main() -> None:

    print(f"max2: {max2(2, 3) == 3}")
    print(f"max3a: {max3a(2, 3, 4) == 4}")
    print(f"max3b: {max3b(2, 3, 4) == 4}")
    print(f"maxn: {maxn(2, 3, 4, 5, 6) == 6}")
    return

# eine Funktion, die zwei Zahlen vergleicht und gibt die größere zurück, falls die beide Zahlen gleich
# sind, gibt einfach die Zahl zurück.
def max2(a: int, b: int) -> int:
    if a > b:
        return a
    return b
    
# eine Funktion, die drei Zahlen miteinander vergleicht und gibt die größte Zahl zurück, falls alle
# drei gleich sind, gibt einfach die Zahl zurück
def max3a(a: int, b: int, c: int) -> int:
    max: int = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

# genau gleiche Funktionilität wie 'max3a' außer hier wird die max2 verwendet, um maximum zweier Zahlen 
# zu bekommen.
def max3b(a: int, b: int, c: int) -> int:
    return max2(max2(a, b), max2(a, c))

# eine Funktion, die die größte Zahl aller Argumente zurückgibt, es könnte unendlich viele Argumente
# eingegeben werden.
def maxn(*args: tuple[int]) -> int | None:
    if not args:
        return
    max: int = args[0] 
    for zahl in args:
        max = max2(max, zahl)
    return max

if __name__ == '__main__':
    main()