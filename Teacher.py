from Account import Account


class Teacher(Account):
    def __init__(self):
        super().__init__()
        self.pay = None
        self.classes = []
        self.hours = None

    def register(self, id):
        self.add_personal_info(id)
        self.classes = input("Please enter the classes seperated by commas: ").split(",")
        self.pay = input("What is your salary: ")
        self.hours = int(input("How many hours do you work?: "))

    def calculate_salary(self):
        return int(self.pay) * self.hours
    def __str__(self):
        return f"{super().__str__()} {self.classes} {self.hours} {self.calculate_salary()}"