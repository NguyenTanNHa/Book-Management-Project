class StudentTest:
    def __init__(self):
        self.students = []

    def input_students(self):
        number_of_students = int(input("Nhập số lượng sinh viên: "))
        for i in range(number_of_students):
            print("Nhập thông tin sinh viên thứ {0}".format(i+1))
            name = input("Tên sinh viên: ")
            grade = float(input("Điểm trung bình: "))
            scholarship = input("Học bổng (có/không): ")
            self.students.append({"name": name, "grade": grade, "scholarship":scholarship})
        print("Nhập thông tin sinh viên thành công!")

    def display_info(self):
        for student in self.students:
            print("Tên SV: {0}, Điểm TB: {1}, Học bổng: {2}".format(student["name"], student["grade"], student["scholarship"]))
    
    def max_min_grade(self):
        max_grade = self.students[0]["grade"]
        min_grade = self.students[0]["grade"]
        max_student = self.students[0]["name"]
        min_student = self.students[0]["name"]
        for student in self.students:
            if student["grade"] > max_grade:
                max_grade = student["grade"]
                max_student = student["name"]
            if student["grade"] < min_grade:
                min_grade = student["grade"]
                min_student = student["name"]
        print("Sinh viên có điểm trung bình cao nhất là {0} với điểm {1}".format(max_student, max_grade))
        print("Sinh viên có điểm trung bình thấp nhất là {0} với điểm {1}".format(min_student, min_grade))
    
    def search_student(self):
        student_name = input("Nhập tên sinh viên cần tìm: ")
        for student in self.students:
            if student["name"] == student_name:
                print("Tên SV: {0}, Điểm TB: {1}, Học bổng: {2}".format(student["name"], student["grade"], student["scholarship"]))
                return
        print("Không tìm thấy sinh viên cần tìm!")
    
    def sort_by_name(self):
        sorted_students = sorted(self.students, key=lambda k: k['name'])
        for student in sorted_students:
            print("Tên SV: {0}, Điểm TB: {1}, Học bổng: {2}".format(student["name"], student["grade"], student["scholarship"]))
    
    def sort_by_grade(self):
        sorted_students = sorted(self.students, key=lambda k: k['grade'], reverse=True)
        for student in sorted_students:
            if student["scholarship"] == "có":
                print("Tên SV: {0}, Điểm TB: {1}, Học bổng: {2}".format(student["name"], student["grade"], student["scholarship"]))
    
    def run(self):
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
                print("Chọn không hợp lệ!")

test = StudentTest()
test.run()