from random import randint

print ("Nhập Kéo, Búa, Bao:")
nguoichoi = input()
may = randint (0,2)
 
if may == 0:
    may = "Kéo"
if may == 1:
    may = "Búa"
if may == 2:
    may = "Lá"

print("_____")
print ("Bạn chọn: " + nguoichoi )
print ("Máy chọn: " + may)
print("_____")

if nguoichoi == "Kéo":
    if may == "Kéo":
        print("Hoà")
    if may == "Búa":
        print("Thua")
    if may == "Bao":
        print("Thắng")

if nguoichoi == "Búa":
    if may == "Kéo":
        print("Thua")
    if may == "Búa":
        print("Hoà")
    if may == "Bao":
        print("Thắng")

if nguoichoi == "Bao":
    if may == "Kéo":
        print("Thua")
    if may == "Búa":
        print("Thắng")
    if may == "Bao":
        print("Thua")
