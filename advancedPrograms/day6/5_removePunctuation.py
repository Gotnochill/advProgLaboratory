# 5. Read a file and remove punctuation
import string
filename = input("Enter filename: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        no_punct = content.translate(str.maketrans('', '', string.punctuation))
        print(no_punct)
except FileNotFoundError:
    print("File not found.")
