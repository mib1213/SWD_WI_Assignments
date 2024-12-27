from utils import Galgenmännchen, run_galgenmännchen
from parameters import WORDS, TRIES
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(f"Erwartet 1 command-line Argument, bekommen {len(sys.argv) - 1}.")
    
    if sys.argv[1] not in ['class', 'seq']:
        sys.exit(f"Das Argument muss entweder 'class' oder 'seq' für OOP bzw. für 'Sequential Programming' sein.")

    if sys.argv[1] == 'class':
        Galgenmännchen.run(WORDS, TRIES)
    
    else:
        run_galgenmännchen(WORDS, TRIES)

if __name__ == '__main__':
    main()