#Now i have to count occurences from a list


numbers = input("Enter numbers seperated by spaces: ")

num_list = [int(num) for num in numbers.split()]

#create empty dictionary
occurrences = {}

for num in num_list:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1 

for num, count in occurrences.items():
    print(f"{num} occurs {count} times")