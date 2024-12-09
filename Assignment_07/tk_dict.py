# Aufgabe 2

import tkinter as tk
from tkinter import messagebox
from functools import partial

def main() -> None:
    # ein Dict um später die "key/Vale" Paare zu speichern
    benutzer_dict: dict[str: str] = {}

    # erzeuge ein tk.TK objekt
    haupt_fenster: tk.Tk = tk.Tk()
    haupt_fenster.geometry("300x150")
    haupt_fenster.title("Füge Key/Value Paare hinzu")
    
    # erzeuge ein Hauptfenster
    leinwand: tk.Frame = tk.Frame(haupt_fenster)
    leinwand.pack(padx=5, pady=5)

    # erzeuge ein key und ein value Variable, deren Werte später in ENTRY hinzufügt werden  
    key: tk.StringVar = tk.StringVar()
    value: tk.StringVar = tk.StringVar()

    # erzeuge ein Label, das über dem Key Eingabebox gezeigt wird
    key_label: tk.Label = tk.Label(haupt_fenster, text='Enter Key')
    key_label.pack()

    # nehme key als Eingabe vom 'textvariable' Parameter und speichere in der 'key' variable
    key_eingabe: tk.Entry = tk.Entry(haupt_fenster, textvariable=key)
    key_eingabe.pack()
    key_eingabe.focus() # Um Mauszeiger an diesem Box zu fokussieren

    # erzeuge ein Label, das über dem Value Eingabebox gezeigt wird
    value_label: tk.Label = tk.Label(haupt_fenster, text='Enter Value')
    value_label.pack()

    # nehme value als Eingabe vom 'textvariable' Parameter und speichere in der 'value' variable
    value_eingabe: tk.Entry = tk.Entry(haupt_fenster, textvariable=value)
    value_eingabe.pack()

    # erzeuge ein Button fürs Hinzufügen und wenn es angeklickt wird, rufe die Funktion
    # 'speichere_values_ins_dict' mit 3 Argumenten auf
    hinzufügen: tk.Button = tk.Button(haupt_fenster, 
                           text='Hinzufügen', 
                           command=partial(speichere_values_ins_dict, benutzer_dict, key, value))
    hinzufügen.pack()

    # erzeuge ein Button fürs Speichern und wenn es angeklickt wird, rufe die Funktion 'print_dict'
    # mit 'benutzer_dict' als Argument auf
    speichern: tk.Button = tk.Button(haupt_fenster, 
                                     text='Dict Speichern', 
                                     command=partial(print_dict, benutzer_dict))
    speichern.pack()

    haupt_fenster.mainloop()
    return

def speichere_values_ins_dict(dict: dict[str: str], key: tk.StringVar, value: tk.StringVar) -> None:
    """
    Um StringVar Objekte in einem dict zu speichern und dann die Werte zurückzusetzen.
    """
    dict[key.get()] = value.get()
    key.set('')
    value.set('')
    return

def print_dict(dict: dict[str: str]) -> None:
    """
    Um ein Dict in einem Message Box anzuzeigen
    """
    messagebox.showinfo(title='Deine Dictionary', message=dict)
    return

if __name__ == '__main__':
    main()