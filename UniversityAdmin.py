from Student import Student
from Teacher import Teacher
from Staff import Staff
import csv

from prettytable import PrettyTable


class UniversityAdmin:
    def __init__(self):
        self.admins = []
        self.students = []
        self.teachers = []
        self.staffs = []
        self.users = []
        self.student_table = PrettyTable()
        self.teacher_table = PrettyTable()
        self.staff_table = PrettyTable()
        self.data = {"student" : "student_data.csv", "teacher": "teacher_data.csv", "staff": "staff_data.csv"}
        self.load_file("student")
        self.load_file("teacher")
        self.load_file("staff")
    def read_file(self, filename):
        with open(self.data[filename], "r") as file:
            data_list =list(csv.reader(file))[1:]
            return data_list

    def load_file(self, account_type):
        data = self.read_file(account_type)
        if account_type == "student":
            for row in data:
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
            fields = ["Account_ID", "First_Name", "last Name", "Age", "Gender", "Phone_Number", "Email", "Majors", "Classes", "Year"]
            with open(self.data["student"], "w") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(fields)

                for student in self.students:
                    csvwriter.writerow([student.get_account_id(), student.first_name, student.last_name, student.age, student.gender,
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
                    csvwriter.writerow([staff.get_account_id(), staff.first_name, staff.last_name, staff.age, staff.gender,
                                   staff.get_phone_number(), staff.get_email(), staff.job, staff.pay, staff.hours])






