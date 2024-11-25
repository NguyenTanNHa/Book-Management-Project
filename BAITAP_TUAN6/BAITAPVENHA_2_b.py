class Person:
    def __init__(self):
        self.name = input("nhap ten: ")
        self.birthday = input("nhap ngay sinh: ")
        self.address = input("nhap dia chi: ")
        self.gender = input("nhap gioi tinh: ")
    def print(self):
        print("ten: ", self.name, " ngay sinh: ", self.birthday, " dia chi: ", self.address, " gioi tinh: ", self.gender)
        print("ma sv: ", self.code, " diem tb: ", self.MS, " email: ", self.email, " hoc bong: ", self.SS)

class Student(Person):
    def __init__(self):
        a = "@"
        b = " "
        self.SS = 0
        Person.__init__(self)
        self.code = input("nhap ma sv: ")
        while len(self.code) != 8:
            self.code = input("nhap ma sv: ")
        self.MS = float(input("nhap diem trung binh: "))
        self.email = input("nhap email: ")
        if(self.MS >= 8):
            self.SS = "co"
        while a not in self.email:
            self.email = input("nhap email: ")
        while  b in self.email:
            self.email = input("nhap email: ")

hs1 = Student()
hs1.print()