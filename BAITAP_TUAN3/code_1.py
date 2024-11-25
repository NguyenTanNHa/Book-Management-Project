A = int(input("Nhập số A:"))
if A < 2:
    print(A, "Không phải là số nguyên tố")
else :
    is_prime = True
    for i in range(2, int(A**0.5)+1):
        if A % i == 0:
            is_prime = False
            break
    if is_prime:
        print(A, "Là số nguyên tố")
    else :
        print(A, "Không phải là số nguyên tố")    