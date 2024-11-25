while True:
    print("Menu:")
    print("1. Nhập list với số phần tử được nhập trước")
    print("2. Nhập list mà không biết trước số phần tử")
    choice = input("Vui lòng chọn a hoặc b: ")
    
    if choice == "a":
        n = int(input("Nhap so phan tu cua list: "))
        lst = []
        for i in range(n):
            x = int(input("Nhap phan tu thu {}: ".format(i+1)))
            lst.append(x)
        print("List vua nhap la:", lst)
        
        while True:
            option = input("Bạn có muốn nhập lại list không? (yes/no): ")
            if option == "yes":
                lst = []
                for i in range(n):
                    x = int(input("Nhap phan tu thu {}: ".format(i+1)))
                    lst.append(x)
                print("List vua nhap la:", lst)
            elif option == "no":
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                
        break
        
    elif choice == "b":
        lst = []
        while True:
            x = int(input("Nhap phan tu (nhap -1 de ket thuc): "))
            if x == -1:
                break
            lst.append(x)
        print("List vua nhap la:", lst)
        break
        
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
