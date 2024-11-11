# Ex 1a

my_list = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

# just to see how indexes look like in in my_list
my_dict = {i: char for i, char in enumerate(my_list)}

# indexes of the characters of "HELLO" in my_list
hello_idxs = [my_list.index(char) for char in 'HELLO']

# indexes of the characters of "PETER" in my_list
peter_idxs = [my_list.index(char) for char in 'PETER']

# add the characters from my_list based on hello_idxs
hello = [my_list[i] for i in hello_idxs]

# add the characters from my_list base on peter_idxs
peter = [my_list[i] for i in peter_idxs]


print("only for info:", my_dict)
print(hello)
print(peter)