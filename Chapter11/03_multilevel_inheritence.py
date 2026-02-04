class Employee:
    company = "Delta Corp"

    def compname(self):
        print(f"The company name is {self.company}")


class Programmer(Employee):
    language = "Python"

    def lang(self):
        print(f"You Programming language is {self.language}")


class Manger(Programmer):
    designation = "Manager"

    def __init__(self, name):
        self.name = name

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
