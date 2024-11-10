year = int(input("Year: "))

if year % 4 == 0: #if year is divisible by 4
    if not year % 100 == 0 or year % 400 == 0: #either year is NOT divisible by 100 or year is divisible by 400
        print("leap_year")
    else:
        print("not leap year")
else:
    print("not leap year")

