from AccountMaster import AccountMaster
from Login_Manager import LoginManagement
from StaffAdmin import StaffAdmin
from StudentAdmin import StudentAdmin
from TeacherAdmin import TeacherAdmin


class MainAdmin:
    def __init__(self):
        self.student = StudentAdmin()
        self.teacher = TeacherAdmin()
        self.staff = StaffAdmin()
        self.admin = None
        self.exit = False


    def login_dashboard(self): # sent here if admin has not logged in yet
        login_manager = LoginManagement() # instantiating login_manager from LoginManagement()
        self.admin = login_manager.admin
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
        while choice != 4:
            choice = int(input(menu))
            if choice == 1:
                self.student.student_dashboard()
            elif choice == 2:
                self.teacher.teachers_dashboard()
            elif choice == 3:
                self.staff.staff_dashboard()