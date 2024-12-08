import datetime
import time

def main() -> None:
    heiligabend_2024: datetime.datetime = datetime.datetime(2024, 12, 24)
    neujahr_2025: datetime.datetime = datetime.datetime(2025, 1, 1)
    oster_2025: datetime.datetime = datetime.datetime(2025, 4, 20)

    while True:
        try:
            benutzer_eingabe: str = input("h für Heiligabend\nn für Neujahr\no für Oster\n: ").lower()
            if benutzer_eingabe not in ['h', 'n', 'o']:
                raise ValueError("Nur 'h', 'n' oder 'o' als Eingabe möglich.")
            break
        except ValueError as ve:
            print(ve, "Bitte versuche nochmal")

    if benutzer_eingabe == 'h':
        print_countdown(heiligabend_2024, 'Bis Heiligabend:')

    elif benutzer_eingabe == 'n':
        print_countdown(neujahr_2025, 'Bis Neujahr:')

    else:
        print_countdown(oster_2025, 'Bis Oster:')
    
    return

def print_countdown(enddatum: datetime.datetime, print_str: str) -> None:
    try:    
        while datetime.datetime.now() < enddatum:
            print(print_str, enddatum - datetime.datetime.now())
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgramm beendet")
    return

if __name__ == '__main__':
    main()