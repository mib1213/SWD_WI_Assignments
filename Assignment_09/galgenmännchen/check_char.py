# Aufgabe 2

def check_char(word, chars):
    solution = [' _ '] * len(word)
    for char in chars:
        if char in word:
            idxs = [idx for idx, char_ in enumerate(word) if char_ == char]
            for idx in idxs:
                solution[idx] = char
    return ''.join(solution)