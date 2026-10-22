import numpy as np

def logical_flatten(arr):
    result = np.empty(arr.size, dtype=arr.dtype)

    for i, index in enumerate(np.ndindex(arr.shape)):
        result[i] = arr[index]

    return result

a = np.array([[1, 2], [3, 4]])

print(logical_flatten(a))  # [1 2 3 4]
print(a.flatten())  