# find common elements between 2 lists

list1 = input("Enter the first sequence seperated by spaces: ").split()
list2 = input("Enter the second sequence seperated by spaces: ").split()
result = []

for i in list1:
    for j in list2:
        if i == j and i not in result:
            result.append(i)
            #push this element in the result list

print("Common elements: ", result)