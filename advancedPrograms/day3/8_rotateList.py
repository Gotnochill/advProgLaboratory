# rotate a list by given position

numbers = input("Enter the numbers seperated by spaces: ").split()

num_list = [int(num) for num in numbers]

k = int(input("Enter the number of positions to rotate: "))

rotated_left = num_list[k:] + num_list[:k]
rotated_right = num_list[-k:] + num_list[:-k]

print("Left rotated list: ", rotated_left)
print("Right rotated list: ", rotated_right)