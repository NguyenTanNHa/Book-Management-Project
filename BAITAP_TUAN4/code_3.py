class Sohoc:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0

    def inputInfo(self):
        self.number1 = float(input("Nhập số thứ nhất:"))
        self.number2 = float(input("Nhập số thứ hai:"))

    def printInfo(self):
        print("Hai số vừa nhập là: " , self.number1, "va" , self.number2)

    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2

sh = Sohoc()
sh.inputInfo()
sh.printInfo()


print("Tổng:", sh.add())
print("Hiệu:", sh.sub())