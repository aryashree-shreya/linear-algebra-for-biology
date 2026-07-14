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

# Coefficient matrix
A = np.array([[2, 3],
              [1, -1]])
This represents the equations:

2x+3y=8
x−y=1
B = np.array([8, 1])

This stores the constants on the right-hand side.
olution = np.linalg.solve(A, B)

NumPy solves the system of linear equations.
