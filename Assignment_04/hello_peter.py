# Ex 1a

my_list = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

my_dict = {i: char for i, char in enumerate(my_list)}

hello_idxs = [my_list.index(char) for char in 'HELLO']

peter_idxs = [my_list.index(char) for char in 'PETER']

hello = [my_list[i] for i in hello_idxs]

peter = [my_list[i] for i in peter_idxs]
    
print(my_dict)
print(hello)
print(peter)