from Account import Account


class Student(Account):
    def __init__(self):
        super().__init__()
        self.majors = None
        self.classes = []
        self.year = None

    def register(self, id):
        self.add_personal_info(id)
        self.majors = input("Please enter your majors: ")
        self.classes = input("Please enter the classes seperated by commas: ").split(",")
        self.year = input("Please enter the year: ")
    def __str__(self):
        return f"{super().__str__()} {self.majors} {self.classes} {self.year}"


