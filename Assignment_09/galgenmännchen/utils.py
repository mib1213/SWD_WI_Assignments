import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from check_char import check_char

"""
I have written the same program once as OOP and once as functional/sequential Programming,
at first I had written as sequential, but because of the necessary use of global keywords,
which I personally don't prefer, I wondered if it would be a good example to use OOP as 
compared to the common sequential programming in Python, so I end up writing the code in both.
Honestly speaking, comparing these two, I wouldn't say OOP is much better, since the logic and
program is exactly the same, except in OOP approch, one has more freedom of sequence and in
sequential programming you always have to remember that you are using the global keywords. I
could imagine once the program gets more complex, it would get very messy with sequential
programming to manage.
"""

"""
I am only going to explain the functionality in the sequential programming version (below),
since the class version is just the, well, class version of that program with exactly same
logic and functionality. 
"""

# class version

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
        
        if messagebox.askyesno("Neues Spiel", "Willst du ein neues Spiel beginnnen?"): 
            self.new_game()
        else:
            self.exit()

    def new_game(self):
            self.refresh_vars()
            self.update_ui()
    
    def exit(self):
        if messagebox.askyesno("Beenden", "Willst du das Programm beenden?"):
            self.root.destroy()

    @classmethod
    def run(cls, words, tries):
        game = Galgenmännchen(words, tries)
        game.root.mainloop()

# sequential version

def run_galgenmännchen(_words: str, _tries: int) -> None:
    # _words, _tries to differentiate from the local words, tries
    def choose_word(words, tries):
        """
        Here I am just making sure that we don't have less number of tries than the chars 
        in a word, because if that's the case, then the game is not possible to win.
        """
        while True:
            random_choice = random.choice(words)
            if len(random_choice) < tries:
                break
        return random_choice

    def refresh_vars():
        """
        Setting up variable to their default values.
        """
        global word, tries, chars, solution
        word = choose_word(_words, _tries)
        chars = []
        solution = ' _ ' * len(word)
        tries = _tries

    refresh_vars()

    # defining the initial structure of the GUI
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Galgenmännchen")
    tk.Frame(root).pack()
    tk.Label(root, text='Verbleibende Versuche').pack()

    tries_label = tk.Label(root, text=_tries)
    tries_label.pack()

    solution_label = tk.Label(root, text=solution)
    solution_label.pack()

    # making sure we get the input as a single character and it must be a letter of 
    # the alphabets, otherwise keep prompting the user for the correct input
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

    # updating the labels with new solution and number of tries
    def update_ui():
        solution_label.config(text=solution)
        tries_label.config(text=tries)

    # exit the program but take a confirmation before
    def exit():
        if messagebox.askyesno("Beenden", "Willst du das Programm beenden?"):
            root.destroy()

    def new_game():
            refresh_vars()
            update_ui()
    
    def end_game():
        if word == solution:
            messagebox.showinfo("Ergebnis", f"Du hast gewonnen. Das Wort war {word}")
        else:
            messagebox.showinfo("Ergebnis", f"Du hast verloren. Das Wort war {word}")

        # ask if the user wants to play a new game, if yes then call new_game(),
        # if not then call exit() 
        if messagebox.askyesno("Neues Spiel", "Willst du ein neues Spiel beginnen?"):
            new_game()
        else:
            exit()

    # update all the global variables as soon as the button is clicked and this function
    # is called
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