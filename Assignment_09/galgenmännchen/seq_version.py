import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from parameters import WORDS, TRIES
from check_char import check_char

def choose_word(words, tries):
    while True:
        random_choice = random.choice(words)
        if len(random_choice) < tries:
            break
    return random_choice

def refresh_vars():
    global word, tries, chars, solution
    word = choose_word(WORDS, TRIES)
    chars = []
    solution = ' _ ' * len(word)
    tries = TRIES

refresh_vars()

root = tk.Tk()
root.geometry("400x200")
root.title("Galgenmännchen")
tk.Frame(root).pack()
tk.Label(root, text='Verbleibende Versuche').pack()

tries_label = tk.Label(root, text=TRIES)
tries_label.pack()

solution_label = tk.Label(root, text=solution)
solution_label.pack()

def get_input():
    while True:
        try:
            char = simpledialog.askstring("Zeichen eingeben", "Gebe ein Zeichen ein").upper()
            if not char.isalpha():
                raise ValueError("Bitte gebe einen Buchstabe ein")
            if len(char) != 1:
                raise ValueError("Bitte gebe nur ein Zeichen ein")
            return char
        except ValueError as ve:
            messagebox.showerror("Fehlermeldung", ve)

def update_ui():
    solution_label.config(text=solution)
    tries_label.config(text=tries)

def exit():
    root.destroy()

def new_game():
    if messagebox.askyesno("Neues Spiel", "Willst du ein neues Spiel beginnen?"):
        refresh_vars()
        update_ui()
    else:
        exit()

def end_game():
    if word == solution:
        messagebox.showinfo("Ergebnis", f"Du hast gewonnen. Das Wort war {word}")
    else:
        messagebox.showinfo("Ergebnis", f"Du hast verloren. Das Wort war {word}")
    new_game()

def get_char():
    global word, tries, chars, solution
    char = get_input()
    chars.append(char)
    solution = check_char(word, chars)
    tries -= 1
    update_ui()
    if tries == 0 or solution == word:
        end_game()

tk.Button(root, text='Zeichen eingeben', command=get_char).pack()
tk.Button(root, text='Neues Spiel', command=new_game).pack()
tk.Button(root, text='Beenden', command=exit).pack()

root.mainloop()

