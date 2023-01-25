
from random import randint

from Account import Account


class AccountMaster(Account):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.__password = None

    def set_password(self):
        password1 = input("Enter password: ")
        password2 = input("Enter password again: ")
        if password1 == password2:
            self.__password = password1
            print("Success")

    def get_password(self):
        return self.__password

    def create_admin(self):
        self.add_personal_info(randint(10000, 20000))
        self.set_password()
        self.is_logged_in = False



