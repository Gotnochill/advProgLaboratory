# Convert a dictionary to a list of tuples and vice versa
d = {'a': 1, 'b': 2, 'c': 3}
# Dictionary to list of tuples
list_of_tuples = list(d.items())
print("Dictionary to list of tuples:", list_of_tuples)
# List of tuples to dictionary
dict_from_tuples = dict(list_of_tuples)
print("List of tuples to dictionary:", dict_from_tuples)
