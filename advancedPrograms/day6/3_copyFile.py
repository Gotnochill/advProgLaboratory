# 3. Copy content from one file to another
src = input("Enter source filename: ")
dest = input("Enter destination filename: ")
try:
    with open(src, "r") as fsrc, open(dest, "w") as fdest:
        fdest.write(fsrc.read())
    print("File copied.")
except FileNotFoundError:
    print("Source file not found.")
