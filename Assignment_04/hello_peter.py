# Ex 1

my_list = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

hello = 'HELLO'
peter = 'PETER'

idx_list_in_hello = []
idx_list_for_hello_in_my_list = []
for idx, i in enumerate(my_list):
    if i in hello:
        idx_list_in_hello.append(hello.index(i))
        idx_list_for_hello_in_my_list.append(my_list.index(i))

idx_set_in_hello = set(idx_list_in_hello)
idx_list_in_hello = list(idx_set_in_hello)
idx_list_in_hello = idx_list_in_hello.sort()

idx_set_for_hello_in_my_list = set(idx_list_for_hello_in_my_list)
idx_list_for_hello_in_my_list = list(idx_set_for_hello_in_my_list)
idx_list_for_hello_in_my_list = idx_list_for_hello_in_my_list.sort()

print(f"{idx_list_in_hello = }")
print(f"{idx_list_for_hello_in_my_list = }")
