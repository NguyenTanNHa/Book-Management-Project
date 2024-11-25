class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def input(self):
        self.name = input("Nhập tên: ")
        self.age = input("Nhập tuổi: ")

    def display(self):
        print("Tên:", self.name)
        print("Tuổi:", self.age)


class Teacher(Person):
    def __init__(self, name=None, age=None, lop_day=None, luong_1_gio_day=None, so_gio_day_trong_thang=None):
        super().__init__(name, age)
        self.lop_day = lop_day
        self.luong_1_gio_day = luong_1_gio_day
        self.so_gio_day_trong_thang = so_gio_day_trong_thang

    def input(self):
        super().input()
        self.lop_day = input("Nhập lớp dạy (sáng/chiều/tối): ")
        self.luong_1_gio_day = int(input("Nhập lương 1 giờ dạy: "))
        self.so_gio_day_trong_thang = int(input("Nhập số giờ dạy trong tháng: "))

    def display(self):
        super().display()
        print("Lớp dạy:", self.lop_day)
        print("Lương 1 giờ dạy:", self.luong_1_gio_day)
        print("Số giờ dạy trong tháng:", self.so_gio_day_trong_thang)

    def tinh_luong(self):
        if self.lop_day in ["sáng", "chiều"]:
            return self.luong_1_gio_day * self.so_gio_day_trong_thang
        elif self.lop_day == "tối":
            return self.luong_1_gio_day * self.so_gio_day_trong_thang + 200000


# Ví dụ sử dụng
t = Teacher()
t.input()
t.display()
luong = t.tinh_luong()
print("Lương:", luong)
