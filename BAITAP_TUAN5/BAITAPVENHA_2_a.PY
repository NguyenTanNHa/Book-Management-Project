class Person:
    def __init__(self, name, gender, birthday, address):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.address = address
    
    def input_info(self):
        self.name = input("Nhập tên: ")
        self.gender = input("Nhập giới tính: ")
        self.birthday = input("Nhập ngày sinh: ")
        self.address = input("Nhập địa chỉ: ")
    
    def display_info(self):
        print(f"Tên: {self.name}")
        print(f"Giới tính: {self.gender}")
        print(f"Ngày sinh: {self.birthday}")
        print(f"Địa chỉ: {self.address}")


# Menu
while True:
    print("---- MENU ----")
    print("1. Nhập thông tin")
    print("2. Hiển thị thông tin")
    print("3. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        person = Person("", "", "", "")
        person.input_info()
    elif choice == "2":
        if not person:
            print("Bạn chưa nhập thông tin!")
        else:
            person.display_info()
    elif choice == "3":
        print("Kết thúc chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ!") 
