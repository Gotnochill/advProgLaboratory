import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(A, B)
# Or, equivalently:
# result = A @ B

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix multiplication result:")
print(result)