# 1. Read a text file and count characters
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
    print("Number of characters:", len(content))
