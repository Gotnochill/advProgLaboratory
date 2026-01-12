# Recursive function to compute Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the position for Fibonacci number: "))
print(f"Fibonacci number at position {num} is {fibonacci(num)}")
