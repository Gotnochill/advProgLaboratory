#merge two list without using the + operator

# intuition: Have two lists and merge them by putting those two in it

# Input two lists
list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()

# Convert to integers (optional, if you want integer lists)
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# Merge using extend()
list1.extend(list2)

print("Merged list:", list1)