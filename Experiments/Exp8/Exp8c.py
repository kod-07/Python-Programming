import numpy as np
a = np.random.random((3,4))
print("Array with 3*4 Shape : ")
print(a)
a.reshape(2,2,3)
print("Array converted to 2*2*3 : ")
print(a)
b = np.linspace(0,30,5)
print("Array using linspace : ")
print(b)
a.flatten()
print("Array after flatern : ")
print(a)

