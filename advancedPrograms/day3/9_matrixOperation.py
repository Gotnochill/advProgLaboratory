# Perform matrix addition and subtraction using nested lists.

# Perform matrix addition and subtraction using nested lists.

# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("Enter elements of first matrix row-wise:")
matrix1 = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix1.append(row)

# Input second matrix
print("Enter elements of second matrix row-wise:")
matrix2 = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix2.append(row)

# Addition
add_result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    add_result.append(row)

# Subtraction
sub_result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    sub_result.append(row)

print("Addition result:")
for row in add_result:
    print(row)

print("Subtraction result:")
for row in sub_result:
    print(row)