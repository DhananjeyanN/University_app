from AccountMaster import AccountMaster
from Database import DatabaseConfig
from Student import Student
from Teacher import Teacher
from Staff import Staff
import csv

from prettytable import PrettyTable


class UniversityAdmin:  # Parent class of student admin, teacher admin, and staff admin
    def __init__(self):
        self.admins = []  # creates list to store admins
        self.students = []  # creates list to store students
        self.teachers = []  # creates list to store teachers
        self.staffs = []  # creates list to store staff
        self.users = []
        self.student_table = PrettyTable()
        self.teacher_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.data = {"student": "student_data.csv", "teacher": "teacher_data.csv",
                     "staff": "staff_data.csv"}  # dictionary used in read file, the given input for filename is used to pull the right key from dictionary

    def read_file(self, filename):  # takes filename to access keys in in self.data
        with open(self.data[filename], "r") as file:  # filename is used to read the right file
            data_list = list(csv.reader(file))[1:]
            return data_list

    def load_file(self, account_type):  # loads file from saved data
        data = self.read_file(account_type)  # read_file used and account type passed in
        if account_type == "student":  # if used to read data depending on student, teacher, or staff
            for row in data:  # goes through every line in data, the lines are stored in lists
                student = Student()
                student.set_account_id(row[0])
                student.first_name = row[1]
                student.last_name = row[2]
                student.age = row[3]
                student.gender = row[4]
                student.set_phone_number(row[5])
                student.set_email(row[6])
                student.majors = row[7]
                student.classes = row[8]
                student.year = row[9]
                self.students.append(student)
        elif account_type == "teacher":
            for row in data:
                teacher = Teacher()
                teacher.set_account_id(row[0])
                teacher.first_name = row[1]
                teacher.last_name = row[2]
                teacher.age = row[3]
                teacher.gender = row[4]
                teacher.set_phone_number(row[5])
                teacher.set_email(row[6])
                teacher.classes = row[7]
                teacher.pay = row[8]
                teacher.hours = row[9]
                self.teachers.append(teacher)
        elif account_type == "staff":
            for row in data:
                staff = Staff()
                staff.set_account_id(row[0])
                staff.first_name = row[1]
                staff.last_name = row[2]
                staff.age = row[3]
                staff.gender = row[4]
                staff.set_phone_number(row[5])
                staff.set_email(row[6])
                staff.job = row[7]
                staff.pay = row[8]
                staff.hours = row[9]
                self.staffs.append(staff)

    def write_file(self, account_type):
        if account_type == "student":
            data = self.students
            fields = ["Account_ID", "First_Name", "last Name", "Age", "Gender", "Phone_Number", "Email", "Majors",
                      "Classes", "Year"]
            with open(self.data["student"], "w") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(fields)

                for student in self.students:
                    csvwriter.writerow(
                        [student.get_account_id(), student.first_name, student.last_name, student.age, student.gender,
                         student.get_phone_number(), student.get_email(), student.majors, student.classes,
                         student.year])
        elif account_type == "teacher":

            data = self.teachers
            fields = ["Account ID", "First Name", "last Name", "Age", "Gender", "Phone Number", "Email",
                      "Class's", "Pay", "Hours"]
            with open(self.data["teacher"], "w") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(fields)
                print(self.teachers)

                for teacher in self.teachers:
                    row = [teacher.get_account_id(), teacher.first_name, teacher.last_name, teacher.age, teacher.gender,
                           teacher.get_phone_number(), teacher.get_email(), teacher.classes, teacher.pay, teacher.hours]
                    csvwriter.writerow(row)
        elif account_type == "staff":
            data = self.staffs
            fields = ["Account ID", "First Name", "last Name", "Age", "Gender", "Phone Number", "Email",
                      "Job's", "Pay", "Hours"]
            with open(self.data["staff"], "w") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(fields)

                for staff in self.staffs:
                    csvwriter.writerow(
                        [staff.get_account_id(), staff.first_name, staff.last_name, staff.age, staff.gender,
                         staff.get_phone_number(), staff.get_email(), staff.job, staff.pay, staff.hours])

    def load_file_database(self,account_type):
        if account_type == "student":  # if used to read data depending on student, teacher, or staff
            data = self.DB.fetch_data("STUDENT")
            print(data)
            for row in data:  # goes through every line in data, the lines are stored in lists
                student = Student()
                student.set_account_id(row[0])
                student.first_name = row[1]
                student.last_name = row[2]
                student.age = row[3]
                student.gender = row[4]
                student.set_phone_number(row[5])
                student.set_email(row[6])
                student.majors = row[7]
                student.classes = row[8]
                student.year = row[9]
                self.students.append(student)
        elif account_type == "teacher":
            data = self.DB.fetch_data("TEACHER")
            for row in data:
                teacher = Teacher()
                teacher.set_account_id(row[0])
                teacher.first_name = row[1]
                teacher.last_name = row[2]
                teacher.age = row[3]
                teacher.gender = row[4]
                teacher.set_phone_number(row[5])
                teacher.set_email(row[6])
                teacher.classes = row[7]
                teacher.pay = row[8]
                teacher.hours = row[9]
                self.teachers.append(teacher)
        elif account_type == "staff":
            data = self.DB.fetch_data("STAFF")
            for row in data:
                staff = Staff()
                staff.set_account_id(row[0])
                staff.first_name = row[1]
                staff.last_name = row[2]
                staff.age = row[3]
                staff.gender = row[4]
                staff.set_phone_number(row[5])
                staff.set_email(row[6])
                staff.job = row[7]
                staff.pay = row[8]
                staff.hours = row[9]
                self.staffs.append(staff)
        elif account_type == "ADMIN":
            data = self.DB.fetch_data("ACCOUNTMASTER")
            for row in data:
                admin = AccountMaster()
                admin.set_account_id(row[0])
                admin.first_name = row[1]
                admin.last_name = row[2]
                admin.age = row[3]
                admin.gender = row[4]
                admin.set_phone_number(row[5])
                admin.set_email(row[6])
                admin.set_password(row[7])
                self.admins.append(admin)


