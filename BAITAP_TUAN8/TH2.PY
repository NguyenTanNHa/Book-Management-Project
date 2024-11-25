import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
odd_arr = arr[arr % 2 == 1]

print("Mảng gốc:", arr)
print("Mảng các số lẻ:", odd_arr)
