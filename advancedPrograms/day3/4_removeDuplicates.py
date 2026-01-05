#remove duplicates from a list without using set()

numbers = input("Enter the sequence of numbers seperated by spaces: ")
num_list = [int(num) for num in numbers.split()]

#hashmap to store the elements seen 
seen = {}
unique_list = []

for num in num_list:
    if num not in seen:
        seen[num] = 1
        unique_list.append(num)

print("Unique element list: " , unique_list)