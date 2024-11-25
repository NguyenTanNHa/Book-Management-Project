M = int(input("Nhập vào số M"))
N = int(input("Nhập vào số N"))

print("Các số chẵn trong khoảng (", M, "," , N,"):")
for i in range(M, N+1 ):
    if i % 2 == 0:
        print(i)

