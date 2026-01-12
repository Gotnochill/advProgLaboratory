# Sort a dictionary by keys and values
d = {'b': 2, 'a': 3, 'c': 1}
# Sort by keys
sorted_by_keys = dict(sorted(d.items()))
print("Sorted by keys:", sorted_by_keys)
# Sort by values
sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)
