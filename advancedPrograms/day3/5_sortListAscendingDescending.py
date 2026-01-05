#i have to sort the list in ascending and descending order

#i am assuming there is a library function to do this directly
numbers = input("Enter the sequence with spaces: ")
num_list = [int(num) for num in numbers.split()]

ascending = sorted(num_list)

descending = sorted(num_list , reverse = True)

print("Ascending order: ", ascending)
print("Descending order: " , descending)
