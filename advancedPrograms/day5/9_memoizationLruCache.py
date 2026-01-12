# Implement memoization using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the position for Fibonacci number: "))
print(f"Fibonacci number at position {num} is {fibonacci(num)}")
