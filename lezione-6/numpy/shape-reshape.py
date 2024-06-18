import numpy as np

arr = np.array([
    [1,2,3],[4,5,6]
])
print(arr.shape)
arr_reshape = arr.reshape(1,-1)
print(arr_reshape.ndim)

arr_reshape = arr.reshape(6)
print(arr_reshape.ndim)

arr_flatten= arr.flatten()
print(arr_flatten)