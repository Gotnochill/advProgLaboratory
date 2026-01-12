# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference (elements in set1 but not in set2)
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)