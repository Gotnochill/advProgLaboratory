# Use lambda to filter even numbers from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print("Even numbers:", even_numbers)
