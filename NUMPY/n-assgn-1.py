import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]  
])

print("First column:",a[:,0])
print("First row:",a[0:1, 0:3])
print(a[0:2,1:3])