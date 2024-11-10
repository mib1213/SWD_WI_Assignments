# Ex 1

# take the input
n: int = int(input("Height? "))

for i in range(1, n+1): # print a '#' 4 times with the line break
         print('#' * i)

for i in range(1, n): # print a '#' 3 times qith the line break
        print('#' * (n - i))
