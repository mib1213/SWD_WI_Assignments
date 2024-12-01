def main() -> None:

    print(f"max2: {max2(2, 3) == 3}")
    print(f"max3a: {max3a(2, 3, 4) == 4}")
    print(f"max3b: {max3b(2, 3, 4) == 4}")
    print(f"maxn: {maxn(2, 3, 4, 5, 6) == 6}")
    return

def max2(a: int, b: int) -> int:
    if a > b:
        return a
    return b
    
def max3a(a: int, b: int, c: int) -> int:
    max: int = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

def max3b(a: int, b: int, c: int) -> int:
    return max2(max2(a, b), max2(a, c))

def maxn(*args: tuple[int]) -> int | None:
    if not args:
        return
    max: int = args[0] 
    for zahl in args:
        max = max2(max, zahl)
    return max

if __name__ == '__main__':
    main()