# Linear Equations using NumPy

import numpy as np

# Coefficient matrix
A = np.array([[2, 3],
              [1, -1]])

# Constant vector
B = np.array([8, 1])

# Solve Ax = B
solution = np.linalg.solve(A, B)

print("Solution:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
