class Account:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.__phone_number = None
        self.__email = None
        self.gender = None
        self.__accountid = None

    def generate_account_id(self, id):
        self.__accountid = f"{self.age}{id}"

    def set_account_id(self, id):
        self.__accountid = id

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_account_id(self):
        return self.__accountid
    def add_personal_info(self, id):
        self.first_name = input("Please enter first name: ")
        self.last_name = input("Please enter last name: ")
        self.age = input("Please enter age: ")
        self.gender = input("Please enter gender")
        self.set_phone_number(input("Please enter your phone number: "))
        self.set_email(input("Please enter your email: "))
        self.generate_account_id(id)

    def __str__(self):
        return f"{self.__accountid} {self.first_name} {self.last_name} {self.age} {self.gender} {self.__phone_number} {self.__email}"



