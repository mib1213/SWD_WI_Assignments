# Aufgabe 2

import tkinter as tk
from tkinter import messagebox
from functools import partial

def main() -> None:
    benutzer_dict: dict[str: str] = {}
    haupt_fenster: tk.Tk = tk.Tk()
    haupt_fenster.geometry("300x150")
    haupt_fenster.title("Füge Key/Value Paare hinzu")
    key: tk.StringVar = tk.StringVar()
    value: tk.StringVar = tk.StringVar()

    leinwand: tk.Frame = tk.Frame(haupt_fenster)
    leinwand.pack(padx=5, pady=5)

    key_label: tk.Label = tk.Label(haupt_fenster, text='Enter Key')
    key_label.pack()

    key_eingabe: tk.Entry = tk.Entry(haupt_fenster, textvariable=key)
    key_eingabe.pack()
    key_eingabe.focus()

    value_label: tk.Label = tk.Label(haupt_fenster, text='Enter Value')
    value_label.pack()

    value_eingabe: tk.Entry = tk.Entry(haupt_fenster, textvariable=value)
    value_eingabe.pack()

    hinzufügen: tk.Button = tk.Button(haupt_fenster, 
                           text='Hinzufügen', 
                           command=partial(save_values_in_dict, benutzer_dict, key, value))
    hinzufügen.pack()

    speichern: tk.Button = tk.Button(haupt_fenster, text='Dict Speichern', command=partial(print_dict, benutzer_dict))
    speichern.pack()

    haupt_fenster.mainloop()
    return

def save_values_in_dict(dict: dict[str: str], key: tk.StringVar, value: tk.StringVar) -> None:
    dict[key.get()] = value.get()
    key.set('')
    value.set('')
    return

def print_dict(dict: dict[str: str]) -> None:
    messagebox.showinfo(title='Deine Dictionary', message=dict)
    return

if __name__ == '__main__':
    main()