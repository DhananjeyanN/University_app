from AccountMaster import AccountMaster
from Database import DatabaseConfig
from Login_Manager import LoginManagement
from StaffAdmin import StaffAdmin
from StudentAdmin import StudentAdmin
from TeacherAdmin import TeacherAdmin


class MainAdmin:
    def __init__(self):
        self.DB = DatabaseConfig()
        self.DB.connect()
        self.DB.create_database("UNIVERSITY_DATABASE")
        self.student = StudentAdmin(self.DB) # instantiating self.student from StudentAdmin()
        self.teacher = TeacherAdmin(self.DB) # instantiating self.teacher from TeacherAdmin()
        self.staff = StaffAdmin(self.DB) # instantiating self.staff from StaffAdmin()
        self.admin = None
        self.exit = False


    def login_dashboard(self): # sent here if admin has not logged in yet
        login_manager = LoginManagement(self.admin, self.DB) # instantiating login_manager from LoginManagement()
        login_manager.login()
        self.exit = login_manager.exit

    def dashboard(self): # sent here when admin is logged in
        menu = """
        Welcome To The University

        1:Students
        2:Teachers
        3:Staff
        4:Quit
        
        Please enter the number associated with you: 

        """
        choice = None
        while choice != 4: # While loop quits main dashboard when choice = 4
            choice = int(input(menu)) # displays main menu
            if choice == 1:
                self.student.student_dashboard() # if choice is 1 sends to student dashboard
            elif choice == 2:
                self.teacher.teachers_dashboard() # if choice is 2 sends to teacher dashboard
            elif choice == 3:
                self.staff.staff_dashboard() # if choice is 3 sends to staff dashboard