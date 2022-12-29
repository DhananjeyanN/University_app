from Teacher import Teacher
from UniversityAdmin import UniversityAdmin


class TeacherAdmin(UniversityAdmin):
    def __init__(self):
        super().__init__()

    def add_teacher(self):
        teacher = Teacher()
        teacher.register(len(self.users) + 1)
        self.teachers.append(teacher)
        self.users.append(teacher)
        print("Teacher has been added")
        self.write_file("teacher")

    def remove_teacher(self):
        search_key = input("Please enter the teacher's id or email")
        for teacher in self.teachers:
            if teacher.get_account_id() == search_key or teacher.get_email() == search_key:
                self.teachers.remove(teacher)
                print(f"{teacher.get_account_id()} has been removed")
            else:
                print(f"Teacher does not exist with {search_key}")

    def edit_teacher(self):
        search_key = input("Please enter the teacher's id or email")
        for teacher in self.teachers:
            if teacher.get_account_id() == search_key or teacher.get_email() == search_key:
                print(teacher)
                field = input("enter the field you would like to edit:")
                if field == "phone":
                    teacher.set_phone_number(int(input("Please enter phone number: ")))
                elif field == "classes":
                    teacher.classes = input("Enter new classes seperated by commas: ").split(",")
                elif field == "first name":
                    teacher.first_name = input("Please enter your first name: ")
                elif field == "last name":
                    teacher.last_name = input("Please enter your last name: ")
                elif field == "age":
                    teacher.age = input("Please enter your age: ")
                elif field == "gender":
                    teacher.gender = input("Please enter your gender: ")
                elif field == "phone number":
                    teacher.set_phone_number(input("Please enter your phone number: "))
                elif field == "email":
                    teacher.set_email(input("Please enter you email: "))
                elif field == "pay":
                    teacher.pay = input("Please enter your hourly rate: ")
                elif field == "hours":
                    teacher.hours = input("Please enter the hours you work in a day: ")
            else:
                print(f"Teacher does not exist with {search_key}")

    def teachers_dashboard(self):
        menu = """
        Welcome To The Teacher Dashboard

        1:Add Teacher
        2:Remove Teacher
        3:Edit Teachers
        4:Display All Teachers
        5:Go to the main menu

        Please enter the number associated with you: 

        """
        choice = None
        while choice != 5:
            if choice == 1:
                self.add_teacher()
            elif choice == 2:
                self.remove_teacher()
            elif choice == 3:
                self.edit_teacher()
            elif choice == 4:
                self.teacher_table.title = "Teacher's Data Base"
                self.teacher_table.field_names = ["Account ID", "First Name", "last Name", "Age", "Gender", "Phone Number", "Email",
                                     "Class's", "Pay", "Hours"]
                for teacher in self.teachers:
                    self.teacher_table.add_row(
                        [teacher.get_account_id(), teacher.first_name, teacher.last_name, teacher.age, teacher.gender,
                         teacher.get_phone_number(), teacher.get_email(), teacher.classes, teacher.pay, teacher.hours])
                    print(self.teacher_table)

            choice = int(input(menu))
