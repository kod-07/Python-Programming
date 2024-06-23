import numpy as np
l1 = [1.0,2.0,3.3,4.5]
a = np.array(l1)
print("Type of array : ",type(a))
b = np.zeros((3,4))
print("Array with all zeros : ")
print(b)
c = (1,2,3,4,5,6,7,8,9,0)
d = np.array(c)
print("Array using typle : ",d)
e = np.random.random((5,5))
print("Array with random values : ", e)