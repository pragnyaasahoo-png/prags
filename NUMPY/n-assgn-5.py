import numpy as np

arr1 = np.random.permutation(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10]))
print("1D Array:")
print(arr1)

arr2 = np.random.permutation(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])).reshape(3, 3)
print("\n2D Array:")
print(arr2)