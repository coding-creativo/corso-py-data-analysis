import numpy as np

arr = np.array([1,2,3,4,5])
arr_copy = arr.copy()
arr_copy[0] = 100

print(arr)
print(arr_copy)

arr = np.array([1,2,3,4,5])
arr_view = arr.view()
arr_view[0] = 100

print(arr)
print(arr_view)