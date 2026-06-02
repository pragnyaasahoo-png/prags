#Difference between Pythonlist and NumPy array
print("1. Performance: NumPy arrays are optimized for performance and can be much faster than Python")
print("2. Lists occupy more memory than Numpy arrays.")
print("3. Lists can store different datatypes but numpy arrays can store elements of the same datatype.")


#Difference between dtype() and astype()
# dtype() does not change the array values but astype() creates a new array with the specified data type and returns it.
# dtype() is used to check the data type of the elements in the array, while astype() is used to convert the data type of
# the elements in the array to a specified type.

#Can a 1D array be sliced like a[:,1]?
# No, a 1D array cannot be sliced like a[:,1] because  1D array has only one axis (dimension), but a[:,1] uses two indices (row and column).
# Therefore, NumPy raises an error.