class Person:
    def __init__(self, name, age, weight, height, sex):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex

class Teacher(Person):
    pass

class Student(Person):
    pass

a = Teacher("Trúc", 40, 45, 161, "female")
b = Student("Nhã", 20, 80, 171, "male")

print("Giáo viên:","Name" ,a.name,"Age", a.age,"Weight", a.weight,"Height",a.height, a.sex,"Sex")
print("Học sinh:","Name" ,b.name,"Age", b.age,"Weight", b.weight,"Height",b.height, b.sex,"Sex")
