# addition of 2 numpy arrays

import numpy as np

arr1 = np.array([int(item) for item in input("Enter first array : ").split()])
arr2 = np.array([int(item) for item in input("Enter second array : ").split()])

result = np.add(arr1,arr2)
print("The sum is: ")
print(result)