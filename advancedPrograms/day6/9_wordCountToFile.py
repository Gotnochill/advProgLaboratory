# 9. Count occurrence of each word and store the output in a new file
filename = input("Enter filename: ")
outputfile = input("Enter output filename: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        words = content.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
    with open(outputfile, "w") as outf:
        for word, count in freq.items():
            outf.write(f"{word}: {count}\n")
    print("Word count written to", outputfile)
except FileNotFoundError:
    print("File not found.")
