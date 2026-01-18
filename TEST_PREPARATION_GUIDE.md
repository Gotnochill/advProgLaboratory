# Advanced Programming Test Preparation Guide

## Overview
Your course covers 5 main topics across Days 1-5. This guide summarizes key concepts and common patterns you'll need for the test.

---

## **DAY 1: Basic Input/Output & Arithmetic**

### Key Concepts:
- **User Input**: `input()` function (returns string by default)
- **Type Conversion**: `int()`, `float()`, `str()`
- **String Concatenation**: Using `+` operator
- **Arithmetic Operations**: `+, -, *, /, //, %, **`
- **F-strings**: `f"Value is {variable}"`

### Important Problems:
1. **User Input** - Basic I/O with multiple inputs
2. **C to Fahrenheit** - Formula: `F = (C * 9/5) + 32`
3. **Even or Odd** - Use modulo operator `%`
4. **Square Root & Cube** - Use `x**0.5` for sqrt, `x**3` for cube
5. **Biggest of Three** - Compare using `if-elif-else` or `max()`
6. **Multiplication Table** - Nested loops
7. **Prime or Composite** - Check divisibility with loop
8. **Armstrong Number** - Sum of cubes of digits equals number

### Code Patterns:
```python
# Type conversion
num = int(input("Enter number: "))
decimal = float(input("Enter decimal: "))

# String formatting
print(f"Value: {num}")

# Arithmetic
power = x ** 2
root = x ** 0.5
remainder = x % 2
```

---

## **DAY 2: String Manipulation**

### Key Concepts:
- **String Indexing**: `s[0]`, `s[-1]` (last character)
- **String Slicing**: `s[1:4]`, `s[:-1]` (exclude last)
- **String Methods**: `.lower()`, `.upper()`, `.strip()`, `.split()`, `.replace()`
- **Iteration**: Loop through characters with `for ch in string`
- **String Reversal**: `s[::-1]` or manual concatenation

### Important Problems:
1. **Reverse String** - Build reversed string backwards
2. **Consonants/Vowels/Digits/Spaces** - Categorize characters
3. **Palindrome** - Check if string equals its reverse
4. **Patterns** - Print patterns with loops
5. **Remove Duplicates** - Use set or track seen characters
6. **Email Validation** - Check for `@` and `.`
7. **Extract Numbers** - Filter digits from mixed string
8. **Diamond Shape** - Pattern printing with nested loops
9. **Encrypt/Decrypt** - Shift characters (Caesar cipher)

### Code Patterns:
```python
# String reversal
rev = ""
for ch in string:
    rev = ch + rev  # Prepend character

# Check character type
if ch.isdigit(): ...
if ch.isalpha(): ...
if ch.isspace(): ...

# Remove duplicates (set method)
unique = set(string)

# Loop with index
for i, ch in enumerate(string):
    print(f"{i}: {ch}")
```

---

## **DAY 3: List Operations**

### Key Concepts:
- **List Creation**: `lst = [1, 2, 3]`
- **List Methods**: `.append()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`
- **List Comprehension**: `[x*2 for x in range(5)]`
- **Built-in Functions**: `min()`, `max()`, `len()`, `sum()`
- **Slicing**: `lst[1:3]`, `lst[::-1]` (reverse)
- **2D Lists (Matrices)**: Nested list access `matrix[i][j]`

### Important Problems:
1. **Min/Max from List** - Use `min()` and `max()`
2. **Count Occurrences** - `.count()` method or loop
3. **Reverse via Slicing** - Use `lst[::-1]`
4. **Remove Duplicates** - Convert to set: `list(set(lst))`
5. **Sort Ascending/Descending** - `.sort()` or `sorted()`
6. **Merge Lists** - Use `+` operator or `.extend()`
7. **Common Elements** - Find intersection
8. **Rotate List** - Move elements circularly
9. **Matrix Operations** - Transpose, multiply, sum operations

### Code Patterns:
```python
# List comprehension
squared = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

# Built-in operations
min_val = min(lst)
max_val = max(lst)
total = sum(lst)

# Sorting
ascending = sorted(lst)
descending = sorted(lst, reverse=True)

# Remove duplicates
unique = list(set(lst))

# Find common elements
common = list(set(list1) & set(list2))

# Reverse
reversed_lst = lst[::-1]
```

---

## **DAY 4: Dictionary Operations**

### Key Concepts:
- **Dictionary Creation**: `d = {}` or `d = {'key': 'value'}`
- **Access**: `d['key']`, `d.get('key')`
- **Methods**: `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`, `.clear()`
- **Iteration**: `for key in dict:` or `for key, value in dict.items():`
- **Nested Dictionaries**: `d['key']['nested_key']`

### Important Problems:
1. **Student Details Dictionary** - Store key-value pairs, access keys/values
2. **Frequency of Words** - Count occurrences using dict
3. **Merge Dictionaries** - Use `.update()` or `{**d1, **d2}`
4. **Union/Intersection/Difference** - Set operations on dict keys
5. **Remove Duplicates** - From dict keys/values
6. **Sort Dictionary** - `sorted(dict)` or `dict(sorted(dict.items()))`
7. **Dict to List & Vice Versa** - Use `.items()`, list comprehension
8. **Nested Dictionary** - Access multiple levels
9. **Phone Directory** - Store numbers with names

### Code Patterns:
```python
# Dictionary creation & access
student = {'name': 'John', 'age': 20}
name = student['name']
age = student.get('age', 'N/A')  # Safe access

# Iteration
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

# Merge dictionaries
merged = {**dict1, **dict2}

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

# Frequency counter
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort dictionary by keys/values
sorted_dict = dict(sorted(student.items()))
sorted_by_values = dict(sorted(freq.items(), key=lambda x: x[1]))
```

---

## **DAY 5: Functions, Recursion & Advanced Concepts**

### Key Concepts:
- **Function Definition**: `def function_name(parameters):`
- **Return Statement**: `return value`
- **Default Arguments**: `def func(x, y=10):`
- **Lambda Functions**: `lambda x: x * 2`
- **Recursion**: Function calling itself with base case
- **Higher-Order Functions**: `map()`, `filter()`, `reduce()`
- **Memoization/LRU Cache**: Optimize recursive functions

### Important Problems:
1. **Factorial** - Simple iteration: `n * (n-1) * ... * 1`
2. **Prime Check** - Check if divisible only by 1 and itself
3. **Lambda Even Filter** - Use `filter(lambda x: x % 2 == 0, lst)`
4. **List Stats** - Apply functions to calculate statistics
5. **Recursive Fibonacci** - Compute Fibonacci with recursion
6. **Map Uppercase** - Use `map(str.upper, strings)`
7. **Reduce Product** - Use `reduce(lambda x, y: x*y, lst)`
8. **Default Keyword Args** - Functions with default parameters
9. **Memoization/LRU Cache** - Optimize with caching

### Code Patterns:
```python
# Function definition
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Recursion (with base case!)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Lambda
square = lambda x: x ** 2
evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))

# Map
uppercase = list(map(str.upper, ['hello', 'world']))

# Reduce (import from functools)
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

# LRU Cache (for memoization)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

---

## **Important Algorithms to Know**

### 1. **Finding Min/Max**
```python
min_val = min(list)
max_val = max(list)
# Or with loop
min_val = list[0]
for num in list[1:]:
    if num < min_val:
        min_val = num
```

### 2. **Checking Prime**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### 3. **Palindrome Check**
```python
# Method 1: String comparison
if string == string[::-1]:
    print("Palindrome")

# Method 2: Loop
rev = ""
for ch in string:
    rev = ch + rev
if string == rev:
    print("Palindrome")
```

### 4. **Removing Duplicates**
```python
# From list
unique = list(set(lst))
# Preserving order
seen = set()
unique = [x for x in lst if not (x in seen or seen.add(x))]

# From string
unique_chars = ''.join(dict.fromkeys(string))
```

### 5. **Frequency Counting**
```python
# Dictionary method
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Using Counter
from collections import Counter
freq = Counter(items)
```

---

## **Common Test Mistakes to Avoid**

1. ❌ **Forgetting type conversion** → Remember `int(input())`
2. ❌ **String vs Integer confusion** → Type matters!
3. ❌ **Off-by-one errors** → Check loop ranges carefully
4. ❌ **Modifying list while iterating** → Use copy or list comprehension
5. ❌ **Base case in recursion** → Always include stopping condition
6. ❌ **Infinite loops** → Make sure loop conditions will eventually be False
7. ❌ **Not initializing variables** → Initialize sum=0, count=0, etc.
8. ❌ **Forgetting return statement** → Functions should return values
9. ❌ **Mutable default arguments** → `def func(lst=[]):` is dangerous!
10. ❌ **Not handling edge cases** → Empty lists, single elements, etc.

---

## **Quick Reference Cheat Sheet**

### String Methods
- `s.upper()`, `s.lower()`, `s.strip()`
- `s.split()`, `s.replace(old, new)`
- `s.startswith()`, `s.endswith()`
- `s.count()`, `s.find()`

### List Methods
- `lst.append(x)`, `lst.remove(x)`, `lst.pop()`
- `lst.sort()`, `lst.reverse()`
- `lst.count(x)`, `lst.index(x)`

### Dictionary Methods
- `d.keys()`, `d.values()`, `d.items()`
- `d.get(key)`, `d.pop(key)`, `d.update()`
- `d.clear()`, `d.copy()`

### Built-in Functions
- `len()`, `sum()`, `min()`, `max()`
- `sorted()`, `reversed()`, `enumerate()`
- `range()`, `zip()`, `map()`, `filter()`

---

## **Practice Tips**

1. **Understand, don't memorize** - Know WHY each solution works
2. **Trace through examples** - Run code mentally with sample inputs
3. **Practice edge cases** - Empty lists, single elements, negative numbers
4. **Write clean code** - Use meaningful variable names
5. **Test your code** - Run it with multiple inputs
6. **Optimize if needed** - Think about time/space complexity
7. **Comment your code** - Explain complex logic

---

**Good luck with your test! 🎯**
