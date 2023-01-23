from AccountMaster import AccountMaster


class LoginManagement:
    def __init__(self, admin, DB):
        self.DB = DB
        self.admin = admin
        self.load_admin()
        self.exit = False
    def load_admin(self): # reading admin data from account.csv
        with open("account.csv", "r") as account:
            data = account.readlines()
            if len(data) != 0:

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
                print(self.admin)
            else:
                self.register()
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
                if self.admin.get_email().strip() == email and self.admin.password.strip() == password:
                    print(self.admin.get_email())
                    print(self.admin.password)
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
        with open("account.csv", "w") as account:
            account.write("Account ID: "+self.admin.get_account_id() + "\n")
            account.write("first name:" + self.admin.first_name + "\n")
            account.write("last name:" + self.admin.last_name + "\n")
            account.write("age:" + self.admin.age + "\n")
            account.write("gender:" + self.admin.gender + "\n")
            account.write("phone number:" + self.admin.get_phone_number() + "\n")
            account.write("email:" + self.admin.get_email() + "\n")
            account.write("password:" + self.admin.get_password() + "\n")
        self.insert_into_database()

    def insert_into_database(self):
        create_table_query = "CREATE TABLE ACCCOUNTMASTER(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),PASSWORD VARCHAR(100))"

        self.DB.create_table("ACCOUNTMASTER", create_table_query)
        self.DB.connection.close()
        self.DB.connect()
        insert_query = "INSERT INTO ACCOUNTMASTER VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        row = (int(self.admin.get_account_id()), self.admin.first_name, self.admin.last_name, int(self.admin.age), self.admin.gender, int(self.admin.get_phone_number()), self.admin.get_email(), self.admin.get_password())
        self.DB.insert_data(insert_query, row)
        self.DB.connection.commit()

