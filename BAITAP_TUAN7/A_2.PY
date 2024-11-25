L = [2 ,4, 9, 3, 5]

a. Thay thế phần tử đầu tiên thành số âm tương ứng.
L[0] = -2

b. Thêm 20 vào cuối danh sách.
L.append(20)

c. Thêm số 0 vào vị trí thứ 3 trong danh sách.
L.insert(2, 0)

d. Xóa phần tử tại vị trí số 4 trong danh sách.
del L[3]

e. Thêm list [0,0,0] vào sau danh sách trên.
L += [0, 0, 0]

f. Sắp xếp danh sách giảm dần.
L.sort(reverse=True)

print(L) # [-2, 20, 9, 5, 4, 3, 0, 0, 0]