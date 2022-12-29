from AccountMaster import AccountMaster


class LoginManagement:
    def __init__(self):
        self.admin = None
        self.load_admin()
        self.exit = False
    def load_admin(self): # reading admin data from account.csv
        with open("account.csv", "r") as account:
            data = account.readlines()
            values = []
            for row in data:
                field = row.split(":")[1][:-1]
                values.append(field)
            self.admin = AccountMaster()
            self.admin.first_name = values[0]
            self.admin.last_name = values[1]
            self.admin.age = values[2]
            self.admin.gender = values[3]
            self.admin.set_phone_number(values[4])
            self.admin.set_email(values[5])
            self.admin.password = values[6]
            self.admin.is_logged_in = False
    def login(self): # when admin has logged in this is called so an admin can be created, login, or program can be quit
        menu = """
        Welcome to the University 
        press 1 to login
        Press 2 to sign up
        Press 3 to Quit Program
        """
        print(menu)

        choice = input("Enter your choice")
        if choice == "1":
            email = input("Enter email: ")
            password = input("Enter Password: ")

            if self.admin is not None:
                print(self.admin.get_email(), self.admin.password)
                if self.admin.get_email() == email and self.admin.password == password:
                    self.admin.is_logged_in = True

                else:
                    print("Incorrect Password")
                    ch = input("1: Forgot Password \t 2: Try Again")
                    if ch == "1" and self.admin.get_email() == email:

                        self.admin.set_password()
                        print(self.admin.get_password())
                        self.save_admin()
                        self.load_admin()
                    else:
                        self.login()
            else:
                print("No account found please create account")
                self.register()
        elif choice == 2:
            self.register()
        elif choice == 3:
            self.exit = True


    def register(self): # For admin Signup
        self.admin = AccountMaster()
        self.admin.create_admin()
        self.save_admin()
    def save_admin(self): # for saving admin data to account.csv
        with open("Account.csv", "w") as account:
            account.write("first name:" + self.admin.first_name + "\n")
            account.write("last name:" + self.admin.last_name + "\n")
            account.write("age:" + self.admin.age + "\n")
            account.write("gender:" + self.admin.gender + "\n")
            account.write("phone number:" + self.admin.get_phone_number() + "\n")
            account.write("email:" + self.admin.get_email() + "\n")
            account.write("password:" + self.admin.get_password() + "\n")

