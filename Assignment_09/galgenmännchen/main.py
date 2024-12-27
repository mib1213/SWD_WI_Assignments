from utils import Galgenmännchen, run_galgenmännchen
from parameters import WORDS, TRIES
import sys
ARGs = ['oop', 'seq']
"""
Note: Please give one command-line argument of either to run the program with OOP or
with Sequential Programming, for OOP, the argument should be `oop` and for sequential `seq`.

Example: 
```
python main.py oop
```

In this file I am basically checking which type of program does the user want to run from the
command line argument.

"""
def main():
    if len(sys.argv) != 2:
        sys.exit(f"Erwartet 1 command-line Argument, bekommen {len(sys.argv) - 1}.")

    argv = sys.argv[1].lower()

    if argv not in ARGs:
        sys.exit(f"Das Argument muss entweder '{ARGs[0]}' oder '{ARGs[1]}' für OOP bzw. für 'Sequential Programming' sein.")

    if argv == ARGs[0]: # oop
        Galgenmännchen.run(WORDS, TRIES)   
    else: # seq
        run_galgenmännchen(WORDS, TRIES)

if __name__ == '__main__':
    main()