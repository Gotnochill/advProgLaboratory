# Function using default and keyword arguments
def greet(name, msg="Hello", punctuation="!"):
    print(f"{msg}, {name}{punctuation}")

greet("Alice")
greet("Bob", msg="Hi")
greet(name="Charlie", msg="Welcome", punctuation=".")
