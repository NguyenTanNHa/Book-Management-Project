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
            salary = hsalary + hours
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
    
    def run(self):
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

tc = teacher()
tc.run()