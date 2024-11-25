#HÌNH TRÒN#
import math

ban_kinh = 10
dien_tich = math.pi * ban_kinh ** 2
chu_vi = 2 * math.pi * ban_kinh

print()
print("Diện tích của hình tròn là:", dien_tich)
print("Chu vi của hình tròn là:", chu_vi)


#HÌNH VUÔNG#
canh = 10 
dien_tich = canh ** 2
chu_vi = 4 * canh

print()
print("Diện tích của hình vuông là:", dien_tich)
print("Chu vi của hình vuông là:", chu_vi)


#HÌNH TAM GIÁC#
a = 5 # Giả sử độ dài 3 cạnh của tam giác lần lượt là a, b, c
b = 6
c = 7

chu_vi = a + b + c
nua_chu_vi = chu_vi / 2 # Sử dụng công thức Hê-rông để tính diện tích
dien_tich = math.sqrt(nua_chu_vi * (nua_chu_vi - a) * (nua_chu_vi - b) * (nua_chu_vi - c))

print()
print("Diện tích của hình tam giác là:", dien_tich)
print("Chu vi của hình tam giác là:", chu_vi)


#HÌNH CHỮ NHẬT#
chieu_dai = 20 # Giả sử chiều dài của hình chữ nhật là 6 đơn vị, chiều rộng là 4 đơn vị
chieu_rong = 40

dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

print()
print("Diện tích của hình chữ nhật là:", dien_tich)
print("Chu vi của hình chữ nhật là:", chu_vi)