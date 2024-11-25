import numpy as np 
x = np.array
print(x)
a = np.zeros((2,2))
print(a)
b = np.ones((1,2))
print(b)
c = np.full((3,2,2),9)
print(c)
d = np.eye(2)
print(d)
e = np.random.rand(3,2)
print(e)

x = np.array([[1,2,3],[4,5,6]], np.int32)
print(x.ndim,x.size)
print(x.shape)
print(x.dtype)  