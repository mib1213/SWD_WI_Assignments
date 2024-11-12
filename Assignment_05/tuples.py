first_names = ['Jane', 'Max', 'Giannis', 'Juan']
last_names = ['Doe', 'Mustermann', 'Karamitros', 'Perez']

# list of tuples of the combination of first and last names
# zip() creates a zip object which needs to be converted to the list object (for example) to
# get its representation
names_list = list(zip(first_names, last_names))
print(names_list)

'''
Reasons why list of tuples of the combination of first and last name is better than 2 separate
lists for first and last names

1- list of tuples are easier to manage as compared to 2 separate lists when the size of lists 
gets bigger 
2- tuples make sure that the correct first name is connected to its respective last name, which
can be easily compromised on the list because lists are vulnerable to index changes
3- since we know the size of our tuple is always going to be 2 for first and last name, tuple will
make sure the size remains unchangeable
4- the only disadvantage of using the tuple here is that it will not let us change the names
later on in case we need 
'''