import numpy as np

arr1 = np.random.randint(0,2,6)
arr2 = np.random.randint(0,2,6)

print("First array: ")
print(arr1)
print("Second array: ")
print(arr2)

print("\nThe above two arrays are equal or not: ")
print((arr1==arr2).all())