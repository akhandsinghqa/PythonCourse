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
        print(f"You Programming language is {self.language} in {self.company}")


class Manger(Programmer):
    designation = "Manager"
    company = "New Delta Corp"

    def __init__(self, name, designation):
        super().__init__()
        self.name = name
        self.designation = designation
        print("This is manager class.")

    def desig(self):
        print(f"{self.name},Your designation in {self.company} is {self.designation} with language as {self.language}")

    @classmethod
    def classdesig(cls):
        print(f"Your designation in {cls.designation}")


# cobject = Employee()
# cobject.compname()
#
# pobject = Programmer()
# pobject.lang()
# pobject.compname()

mobject = Manger("Akhand", "Sr Manager")
mobject.desig()
# mobject.lang()
# mobject.compname()
mobject.classdesig()
