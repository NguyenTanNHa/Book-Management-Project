import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
c = np.concatenate((a, b) , axis = 1)

print("Mảng a:\n", a)
print("Mảng b:\n", b)
print("Mảng c:\n", c)
