import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print("Original Array:")
print(arr)


arr1 = arr.reshape(3, 4)
print("\nShape (3,4):")
print(arr1)


arr2 = arr.reshape(2, 6)
print("\nShape (2,6):")
print(arr2)


arr3 = arr.reshape(2, 3, 2)
print("\nShape (2,3,2):")
print(arr3)