import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = arr % 2 == 1
arr[mask] = -1

print("Mảng đã thay thế là: ", arr)
