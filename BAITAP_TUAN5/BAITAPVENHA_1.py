class Nv:
    def __init__(self):
        self.name = input("nhap ten: ")
        self.age = input("nhap tuoi: ")
        self.address = input("nhap dia chi: ")
        self.salary = float(input("nhap luong: "))
        self.hour = int(input("nhap gio: "))
        self.bonus = float
        if self.hour >= 200:
            self.bonus = self.salary*0.2
        elif self.hour < 200 and self.hour >= 100:
            self.bonus = self.salary*0.1
        elif self.hour < 100:
            self.bonus = 0
    
    def print(self):
        print("ten: ", self.name, " tuoi: ", self.age, " dia chi: ", self.address, " luong: ", self.salary, " so gio lam: ", self.hour, " thuong: ", self.bonus)
    

nv1 = Nv()
nv1.print()