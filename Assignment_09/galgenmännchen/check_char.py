# Aufgabe 2

def check_char(word: str, chars: list[str]) -> str:
    """
    To repalce the `_` with the characters provided in the list where these characters
    are present in the given `word` variable.
    """

    """
    Making a temporary solution word list. We could have also used the solution argument
    directly and hence must not need to create our own temporarily, but in our 
    program it is being used as a `str` which is immutable, so we would still have to
    convert that to list first, which would end up being more work then just doing this
    and fill it with the characters according to `word`.
    """
    
    solution = [' _ '] * len(word)

    """
    The idea behind this nested for-loop, is to iterate over each char in the `char`
    list and IF only the char is present in the `word`, then go ahead and search for all 
    the idx where this char appears, note that we cannot just index in the str 
    from the given char using the method str.index(char) because it will ONLY return
    the first occurence of that char in the str but we need all the occurences, so for example
    in case of 'HALLO', we need the idxs [2, 3] not just 2. Once we get these idxs,
    we can replace the same idxs of our `solution` list with the corresponding char.
    Note that we could have also taken another approch in which we would first save all the
    idxs from the `chars` list in another list using list.extend() method and then use a 
    separate for-loop to loop through all the idxs together, we wouldn't be having a nested
    for loop in this approach but 2 separate for-loops, though I preferred the first 
    approch since we only have to create one list to do the job.
    """
    for char in chars:
        if char in word:
            idxs = [idx for idx, char_ in enumerate(word) if char_ == char]
            for idx in idxs:
                solution[idx] = char
    return ''.join(solution)