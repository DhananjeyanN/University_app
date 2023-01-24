from Staff import Staff
from UniversityAdmin import UniversityAdmin


class StaffAdmin(UniversityAdmin):
    def __init__(self, DB):
        super().__init__()
        self.DB = DB
        self.insert_into_database(self.staffs)

    def add_staff(self):
        staff = Staff()
        staff.register(len(self.users) + 1)
        self.staffs.append(staff)
        self.users.append(staff)
        print("Staff has been added")
        self.write_file("staff")

    def remove_staff(self):
        search_key = input("Please enter the staff's id or email")
        for staff in self.staffs:
            if staff.get_account_id() == search_key or staff.get_email() == search_key:
                self.staffs.remove(staff)
                print(f"{staff.get_account_id()} has been removed")
            else:
                print(f"Staff does not exist with {search_key}")

    def edit_staff(self):
        search_key = input("Please enter the staff's id or email")
        for staff in self.staffs:
            if staff.get_account_id() == search_key or staff.get_email() == search_key:
                print(staff)
                field = input("enter the field you would like to edit:")
                if field == "phone":
                    staff.set_phone_number(int(input("Please enter phone number: ")))
                elif field == "first name":
                    staff.first_name = input("Please enter your first name: ")
                elif field == "last name":
                    staff.last_name = input("Please enter your last name: ")
                elif field == "age":
                    staff.age = input("Please enter your age: ")
                elif field == "gender":
                    staff.gender = input("Please enter your gender: ")
                elif field == "phone number":
                    staff.set_phone_number(input("Please enter your phone number: "))
                elif field == "email":
                    staff.set_email(input("Please enter you email: "))
                elif field == "job":
                    staff.job = input("Please enter your job: ")
                elif field == "pay":
                    staff.pay = input("Please enter your hourly rate: ")
                elif field == "hours":
                    staff.hours = input("Please enter the hours you work in a day: ")
            else:
                print(f"Staff does not exist with {search_key}")

    def staff_dashboard(self):
        menu = """
        Welcome To The Staff Dashboard

        1:Add Staff
        2:Remove Staff
        3:Edit Staff
        4:Display All Staff
        5:Go to the main menu

        Please enter the number associated with you: 

        """
        choice = None
        while choice != 5:
            if choice == 1:
                self.add_staff()
            elif choice == 2:
                self.remove_staff()
            elif choice == 3:
                self.edit_staff()
            elif choice == 4:
                self.staff_table.title = "Staff's Data Base"
                self.staff_table.field_names = ["Account ID", "First Name", "last Name", "Age", "Gender", "Phone Number", "Email",
                                     "Job's", "Pay", "Hours"]
                for staff in self.staffs:
                    self.staff_table.add_row([staff.get_account_id(), staff.first_name, staff.last_name, staff.age, staff.gender,
                                   staff.get_phone_number(), staff.get_email(), staff.job, staff.pay, staff.hours])
                    print(self.staff_table)

            choice = int(input(menu))

    def insert_into_database(self, data_list):
        for staff in self.staffs:
            insert_query = "INSERT INTO STAFF VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            row = (int(staff.get_account_id()), staff.first_name, staff.last_name, int(staff.age), staff.gender, int(staff.get_phone_number()), staff.get_email(), str(staff.job), str(staff.pay), int(staff.hours))
            self.DB.insert_data(insert_query, row)
            self.DB.connection.commit()

    def load_datafiles(self):
        self.load_file_database("staff")
