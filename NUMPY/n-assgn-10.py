import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Shape:", a.shape)
print("Size:", a.size)
print("Number of dimensions:", a.ndim)
print("Data type:", a.dtype)

a = a.astype(float)

print("\nAfter changing datatype:")
print(a)
print("Data type:", a.dtype)