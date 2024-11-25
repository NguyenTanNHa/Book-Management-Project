class TeacherTest:
    def __init__(self):
        self.teachers = []
 
    def main_menu(self):
        print("Chọn 1: Nhập vào n giảng viên")
        print("Chọn 2: Hiển thị thông tin")
        print("Chọn 3: Hiển thị giảng viên có lương cao nhất")
        print("Chọn 4: Thoát")
 
    def enter_teachers(self):
        n = int(input("Nhập số lượng giảng viên: "))
        for i in range(n):
            name = input("Nhập tên giảng viên: ")


            salary = float(input("Nhập lương giảng viên: "))
            self.teachers.append({"name": name, "salary": salary})
 
    def display_teachers(self):
        print("Danh sách giảng viên:")
        for teacher in self.teachers:
            print("Tên:", teacher["name"], ", lương:", teacher["salary"])
 
    def highest_salary(self):
        highest_salary = 0
        highest_teacher = None
        for teacher in self.teachers:
            if teacher["salary"] > highest_salary:
                highest_salary = teacher["salary"]
                highest_teacher = teacher
        if highest_teacher is not None:
            print("Giảng viên có lương cao nhất:")
            print("Tên:", highest_teacher["name"], ", lương:", highest_teacher["salary"])
        else:
            print("Không có giảng viên nào")
 
    def run(self):
        while True:
            self.main_menu()
            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice == 1:
                self.enter_teachers()
            elif choice == 2:
                self.display_teachers()
            elif choice == 3:
                self.highest_salary()
            elif choice == 4:
                break
            else:
                print("Lựa chọn không hợp lệ")
 
 
if __name__ == "__main__":
    teacher_test = TeacherTest()
    teacher_test.run()