# 4. Count lines, words, and characters in a file
filename = input("Enter filename: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()
        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", len(content))
except FileNotFoundError:
    print("File not found.")
