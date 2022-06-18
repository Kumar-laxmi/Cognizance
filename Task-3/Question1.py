import numpy as np

first = int(input("First Number: "))
last = int(input("Last Number: "))
arr = np.array([i for i in range(first,last+1)])

new_arr = np.zeros(len(arr) + (len(arr)-1)*5)
new_arr[::6] = arr

print(new_arr)


