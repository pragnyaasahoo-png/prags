import numpy as np

a=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]  
])


print("First row:",a[0:1, 0:3])
print("Second column:",a[:,1])
print(a[1:2,1:2])