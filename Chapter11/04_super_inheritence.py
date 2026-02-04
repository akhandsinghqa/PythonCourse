class Employee:
    company = "Delta Corp"

    def __init__(self):
        print("This is Employee Class.")

    def compname(self):
        print(f"The company name is {self.company}")


class Programmer(Employee):
    language = "Python"

    def __init__(self):
        super().__init__()
        print("This is Programmer class.")

    def lang(self):
        print(f"You Programming language is {self.language}")


class Manger(Programmer):
    designation = "Manager"

    def __init__(self, name):
        super().__init__()
        self.name = name
        print("This is manager class.")

    def desig(self):
        print(f"{self.name},Your designation is {self.designation}")


cobject = Employee()
cobject.compname()

pobject = Programmer()
pobject.lang()
pobject.compname()

mobject = Manger("Akhand")
mobject.desig()
mobject.lang()
mobject.compname()
