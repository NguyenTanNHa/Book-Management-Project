a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

while True:
    print("Menu:")
    print("1. Không dùng List Comprehension")
    print("2. Dùng List Comprehension")
    choice = input("Vui lòng chọn cách thức giải quyết: ")
    
    if choice == "1":
        # a) Không dùng List Comprehension
        c = []
        for x in a:
            if x in b and x not in c:
                c.append(x)
        print("Các phần tử chung của 2 list là:", c)
        while True:
            ans = input("Bạn có muốn tiếp tục chương trình không? (y/n): ")
            if ans == "y":
                break
            elif ans == "n":
                exit()
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
    elif choice == "2":
        # b) Dùng List Comprehension
        c = list(set([x for x in a if x in b]))
        print("Các phần tử chung của 2 list là:", c)
        while True:
            ans = input("Bạn có muốn tiếp tục chương trình không? (y/n): ")
            if ans == "y":
                break
            elif ans == "n":
                exit()
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
