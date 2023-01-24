from Database import DatabaseConfig
from MainAdmin import MainAdmin

def main():
    DB = DatabaseConfig()
    DB.connect()
    DB.create_database("UNIVERSITY_DATABASE")
    ACCMASTER = "CREATE TABLE ACCOUNTMASTER(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),PASSWORD VARCHAR(100))"
    STUDENT = "CREATE TABLE STUDENT(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),MAJORS VARCHAR(200),CLASSES VARCHAR(200),YEAR INT NOT NUlL)"
    TEACHER = "CREATE TABLE TEACHER(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),CLASSES VARCHAR(200),PAY INT NOT NUlL, HOURS INT NOT NULL)"
    STAFF = "CREATE TABLE STAFF(ACCOUNT_ID INT NOT NULL PRIMARY KEY,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),AGE INT NOT NULL,GENDER VARCHAR(100),PHONE_NUMBER LONG NOT NULL,EMAIL VARCHAR(100),JOB VARCHAR(200),PAY INT NOT NUlL, HOURS INT NOT NULL)"
    DB.create_tables([ACCMASTER, STUDENT, TEACHER, STAFF], ["ACCOUNT_MASTER", "STUDENT", "TEACHER", "STAFF"])
    ui_manager = MainAdmin(DB) # Instantiating ui_manager as object with MainAdmin

    while True:
        if ui_manager.admin is not None and ui_manager.admin.is_logged_in == True: #checks if admin exists and is logged in
            ui_manager.dashboard() #sends to dashboard meathod in main admin
        else:
            ui_manager.login_dashboard() # sends to admin login dashboard in Main Admin
            #print(ui_manager.admin)
            #print(ui_manager.admin.is_logged_in)
            ui_manager.dashboard()
        if ui_manager.exit == True: # checks self.exit a variable in Main Admin so program can exit
            break

if __name__ == "__main__":
    main()
