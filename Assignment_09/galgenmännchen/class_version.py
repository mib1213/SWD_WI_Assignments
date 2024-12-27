import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from parameters import WORDS, TRIES
from check_char import check_char

class Galgenmännchen:
    def __init__(self, words, tries):
        self.words = words
        self.max_tries = tries
        self.refresh_vars()
        self.init_gui()

    def refresh_vars(self):
        self.word = self.choose_word()
        self.chars = []
        self.solution = ' _ ' * len(self.word)
        self.tries = self.max_tries

    def choose_word(self):
        while True:
            random_choice = random.choice(self.words)
            if len(random_choice) < self.max_tries:
                break
        return random_choice

    def init_gui(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Galgenmännchen")
        tk.Frame(self.root).pack()

        tk.Label(self.root, text='Verbleibende Raten').pack()

        self.tries_label = tk.Label(self.root, text=self.max_tries)
        self.tries_label.pack()

        self.solution_label = tk.Label(self.root, text=self.solution)
        self.solution_label.pack()

        tk.Button(self.root, text='Zeichen eingeben', command=self.get_char).pack()
        tk.Button(self.root, text='Neues Spiel', command=self.new_game).pack()
        tk.Button(self.root, text='Beenden', command=self.exit).pack()

    def get_char(self):
        self.char = self.get_input()
        self.chars.append(self.char)
        self.solution = check_char(self.word, self.chars)
        self.tries -= 1
        self.update_ui()
        if self.tries == 0 or self.solution == self.word:
            self.end_game()
    def get_input(self):
        while True:
            try:
                char = simpledialog.askstring("Zeichen Eingeben", "Gebe ein Zeichen ein").upper()
                if not char.isalpha():
                    raise ValueError("Bitte gebe einen Buchstabe ein")
                if len(char) != 1:
                    raise ValueError("Bitte gebe nur ein Zeichen ein")
                return char
            except ValueError as ve:
                messagebox.showerror("Fehlermeldung", ve)

    def update_ui(self):
        self.solution_label.config(text=self.solution)
        self.tries_label.config(text=self.tries)
            
    def end_game(self):
        if self.word == self.solution:
            messagebox.showinfo("Ergebnis", f"Du hast gewonnen. Das Wort war {self.word}")
        else:
            messagebox.showinfo("Ergebnis", f"Du hast verloren. Das Wort war {self.word}")
        self.new_game()

    def new_game(self):
        if messagebox.askyesno("Neues Spiel", "Willst du ein neues Spiel beginnnen?"):
            self.refresh_vars()
            self.update_ui()
        else:
            self.exit()
    
    def exit(self):
        self.root.destroy()

    @classmethod
    def run(cls, words, tries):
        game = Galgenmännchen(words, tries)
        game.root.mainloop()

if __name__ == '__main__':
    Galgenmännchen.run(WORDS, TRIES)



