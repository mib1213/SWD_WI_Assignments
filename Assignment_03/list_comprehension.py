# Ex 3a

char: str = input("Character: ")
n: int = int(input("Number: "))

chars: list[str] = [char*i for i in range(1, n+1)]
print(chars)