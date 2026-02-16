# 2. Append data to a file
with open("test.txt", "a") as f:
    data = input("Enter data to append: ")
    f.write(data + "\n")
print("Data appended.")
