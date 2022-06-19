# Multiplying a matrix

import numpy as np

A = np.array([[2,3,5],
             [1,0,6],
             [7,10,11]])
B = np.array([[0,9,13],
             [1,6,8],
             [11,9,7]])

print("Matrix A =")
print(A)
print("\nMatrix B =")
print(B)

result = np.matmul(A,B)

print("\nThe Multiplication of A & B gives = ")
print(result)