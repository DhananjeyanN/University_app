from Student import Student
from UniversityAdmin import UniversityAdmin


class StudentAdmin(UniversityAdmin): # creating class Student Admin as a child class of University Admin
    def __init__(self, database_obj):
        super().__init__() # bringing in init of Student Admin in the init of Student Admin
        self.database = database_obj
        self.insert_into_database(self.students)

    def add_student(self):
        student = Student()
        student.register(len(self.users) + 1)
        self.students.append(student)
        self.users.append(student)
        print("Student has been added")
        #self.insert_into_database(self.students)
        self.write_file("student")

    def remove_student(self):
        search_key = input("Please enter the student's id or email")
        for student in self.students:
            if student.get_account_id() == search_key or student.get_email() == search_key:
                self.students.remove(student)
                print(f"{student.get_account_id()} has been removed")
            else:
                print(f"Student does not exist with {search_key}")

    def edit_student(self):
        search_key = input("Please enter the student's id or email")
        for student in self.students:
            if student.get_account_id() == search_key or student.get_email() == search_key:
                print(student)
                field = input("enter the field you would like to edit:")
                if field == "phone":
                    student.set_phone_number(int(input("Please enter phone number: ")))
                elif field == "classes":
                    student.classes = input("Enter new classes seperated by commas: ").split(",")
                elif field == "majors":
                    student.majors = input("Enter your majors serperated by commas: ").split(",")
                elif field == "year":
                    student.year = input("Please enter your year: ")
                elif field == "first name":
                    student.first_name = input("Please enter your first name: ")
                elif field == "last name":
                    student.last_name = input("Please enter your last name: ")
                elif field == "age":
                    student.age = input("Please enter your age: ")
                elif field == "gender":
                    student.gender = input("Please enter your gender: ")
                elif field == "phone number":
                    student.set_phone_number(input("Please enter your phone number: "))
                elif field == "email":
                    student.set_email(input("Please enter you email: "))
            else:
                print(f"Student does not exist with {search_key}")

    def student_dashboard(self):
        menu = """
        Welcome To The Student Dashboard

        1:Add Student
        2:Remove Student
        3:Edit Students
        4:Display All Students
        5:Go to the main menu

        Please enter the number associated with you: 

        """
        choice = None
        while choice != 5:
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.remove_student()
            elif choice == 3:
                self.edit_student()
            elif choice == 4:

                self.student_table.title = "Student Data Base"
                self.student_table.field_names = ["Account ID", "First Name", "last Name", "Age", "Gender", "Phone Number", "Email",
                                     "Majors", "Classes", "Year"]
                for student in self.students:
                    self.student_table.add_row(
                        [student.get_account_id(), student.first_name, student.last_name, student.age, student.gender,
                         student.get_phone_number(), student.get_email(), student.majors, student.classes,
                         student.year])

                print(self.student_table)
            choice = int(input(menu))

    def insert_into_database(self, data_list):
        create_table_query = "CREATE TABLE STUDENT(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),MAJORS VARCHAR(200),CLASSES VARCHAR(200),YEAR INT NOT NUlL)"

        self.database.create_table("STUDENT", create_table_query)

        for student in self.students:
            insert_query = "INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            row = (int(student.get_account_id()), student.first_name, student.last_name, int(student.age), student.gender, int(student.get_phone_number()), student.get_email(), str(student.majors), str(student.classes), int(student.year))
            self.database.insert_data(insert_query, row)
            self.database.connection.commit()
