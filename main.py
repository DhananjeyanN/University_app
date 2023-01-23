from MainAdmin import MainAdmin


def main():
    ui_manager = MainAdmin() # Instantiating ui_manager as object with MainAdmin
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
