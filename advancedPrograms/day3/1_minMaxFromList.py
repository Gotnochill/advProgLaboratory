numbers = input("Enter the numbers seperated by spaces: ")

#Convert the input string into a list of integers
num_list = [int(num) for num in numbers.split()]

minimum = min(num_list)
maximum = max(num_list)

print("Minimum Value is: ", minimum)
print("Maximum Value is: ", maximum)