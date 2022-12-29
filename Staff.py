from Account import Account


class Staff(Account):
    def __init__(self):
        super().__init__()
        self.pay = None
        self.hours = None
        self.job = None
    def register(self, id):
        self.add_personal_info(id)
        self.pay = input("What is your salary: ")
        self.hours = int(input("How many hours do you work?: "))
        self.job = input("What is your job?: ")

    def calculate_salary(self):
        return int(self.pay) * self.hours

    def __str__(self):
        return f"{super().__str__()} {self.hours} {self.calculate_salary()}"