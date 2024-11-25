class teacher:
    def __init__(self):
        self.teacher = []

    def input_info(self):
        numberofteacher = int(input("enter n teachers: "))
        for i in range(numberofteacher):
            print("enter info of teacher no {0}".format(i+1))
            name = input("name: ")
            hsalary = int(input("hourly salary: "))
            hours = int(input("working hours: "))
            salary = hsalary * hours
            self.teacher.append({"name": name, "hourly salary": hsalary, "working hours":hours, "salary":salary})
        print("success")
    
    def show_info(self):
        for teacher in self.teacher:
            print("name: {0}, working hours: {1}, hourly salary: {2}, salary: {3}".format(teacher["name"], teacher["working hours"], teacher["hourly salary"], teacher["salary"]))

    def maxminsalary(self):
        max_salary = self.teacher[0]["salary"]
        min_salary = self.teacher[0]["salary"]
        max_teacher = self.teacher[0]["name"]
        min_teacher = self.teacher[0]["name"]
        for teacher in self.teacher:
            if teacher["salary"] > max_salary:
                max_salary = teacher["salary"]
                max_teacher = teacher["name"]
            if teacher["salary"] < min_salary:
                min_salary = teacher["salary"]
                min_teacher = teacher["name"]
        print("The teacher with the highest salary is  {0} with {1}".format(max_teacher, max_salary))
        print("The teacher with the lowest salary is {0} with {1}".format(min_teacher, min_salary))
    
    def run1(self):
        while True:
            print("""
            option 1: enter teachers info
            option 2: show info
            option 3: show the teacher with the highest salary and the lowest salary
            option 4: exit
            """)
            option = int(input("enter: "))
            if option == 1:
                self.input_info()
            elif option == 2:
                self.show_info()
            elif option == 3:
                self.maxminsalary()
            elif option == 4:
                print("exit")
                break
            else:
                print("invalid")

class Person:
    def __init__(self):
        self.name = input("nhap ten: ")
        self.birthday = input("nhap ngay sinh: ")
        self.address = input("nhap dia chi: ")
        self.gender = input("nhap gioi tinh: ")

class Student(Person):
    def __init__(self):
        self.students = []

    def input_students(self):
        number_of_students = int(input("Nhập số lượng sinh viên: "))
        for i in range(number_of_students):
            print("Nhập thông tin sinh viên thứ {0}".format(i+1))
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
            while a not in self.email and b in self.email:
                self.email = input("nhap email: ")
            
            self.students.append({"ten": self.name, "ngay sinh": self.birthday, "dia chi": self.address, "gioi tinh": self.gender, "ma sv": self.code,  "diem tb": self.MS, "email": self.email, "hoc bong": self.SS})
            print("Nhập thông tin sinh viên thành công!")

    def display_info(self):
            for student in self.students:
                print("ten: {0}, ngay sinh: {1}, dia chi: {2}, gioi tinh: {3}, ma sv: {4}, diem tb: {5}, email{6}, hoc bong{7}".format(student["ten"], student["ngay sinh"], student["dia chi"], student["gioi tinh"], student["ma sv"], student["diem tb"], student["email"], student["hoc bong"]))
        
    def max_min_grade(self):
        max_grade = self.students[0]["diem tb"]
        min_grade = self.students[0]["diem tb"]
        max_student = self.students[0]["ten"]
        min_student = self.students[0]["ten"]
        for student in self.students:
            if student["diem tb"] > max_grade:
                max_grade = student["diem tb"]
                max_student = student["ten"]
            if student["diem tb"] < min_grade:
                min_grade = student["diem tb"]
                min_student = student["ten"]
        print("Sinh viên có điểm trung bình cao nhất là {0} với điểm {1}".format(max_student, max_grade))
        print("Sinh viên có điểm trung bình thấp nhất là {0} với điểm {1}".format(min_student, min_grade))

    def search_student(self):
        student_name = input("Nhập tên sinh viên cần tìm: ")
        for student in self.students:
            if student["ten"] == student_name:
                print("ten: {0}, ngay sinh: {1}, dia chi: {2}, gioi tinh: {3}, ma sv: {4}, diem tb: {5}, email{6}, hoc bong{7}".format(student["ten"], student["ngay sinh"], student["dia chi"], student["gioi tinh"], student["ma sv"], student["diem tb"], student["email"], student["hoc bong"]))
                return
        print("Không tìm thấy sinh viên cần tìm!")

    def sort_by_name(self):
        sorted_students = sorted(self.students, key=lambda k: k['ten'])
        for student in sorted_students:
            print("ten: {0}, ngay sinh: {1}, dia chi: {2}, gioi tinh: {3}, ma sv: {4}, diem tb: {5}, email{6}, hoc bong{7}".format(student["ten"], student["ngay sinh"], student["dia chi"], student["gioi tinh"], student["ma sv"], student["diem tb"], student["email"], student["hoc bong"]))

    def sort_by_grade(self):
        sorted_students = sorted(self.students, key=lambda k: k['diem tb'], reverse=True)
        for student in sorted_students:
            if student["hoc bong"] == "co":
                print("ten: {0}, ngay sinh: {1}, dia chi: {2}, gioi tinh: {3}, ma sv: {4}, diem tb: {5}, email{6}, hoc bong{7}".format(student["ten"], student["ngay sinh"], student["dia chi"], student["gioi tinh"], student["ma sv"], student["diem tb"], student["email"], student["hoc bong"]))
    
    def run2(self):
        while True:
            print("""
            Chọn 1: Nhập vào n sinh viên
            Chọn 2: Hiển thị thông tin
            Chọn 3: Hiển thị SV có điểm trung bình cao nhất và SV có điểm thấp nhất
            Chọn 4: Tìm kiếm SV theo mà SV. 
            Chọn 5: Hiển thị tất cả SV theo thứ tự tên trong bảng chữ cái
            Chọn 6: Hiển thị các SV được học bổng và sắp xếp thep thứ tự điểm từ cao- thấp
            Chọn 7: Thoát
            """)
            choice = int(input("Chọn: "))
            if choice == 1:
                self.input_students()
            elif choice == 2:
                self.display_info()
            elif choice == 3:
                self.max_min_grade()
            elif choice == 4:
                self.search_student()
            elif choice == 5:
                self.sort_by_name()
            elif choice == 6:
                self.sort_by_grade()
            elif choice == 7:
                print("Thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ")

while True:
    option = int(input("chon giao vien: 1 / sv: 2 / thoat: 3  : "))
    if option == 1:
        tc = teacher()
        tc.run1()
    elif option == 2:
        sv = Student()
        sv.run2()
    elif option == 3:
        print("thoat")
        break
    else: False
