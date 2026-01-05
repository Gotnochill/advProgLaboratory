# reverse a list using slicing, what is slicing first?


numbers = input("Enter the numbers seperated by spaces: ")

num_list = [int(num) for num in numbers.split()]

reversed_list = num_list[::-1]

print("Original list: " , num_list)
print("Reversed list: " , reversed_list)

