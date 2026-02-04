class Company:
    name = "DTC InfoTech"

    def __init__(self):
        print("This is Company Class.")

    def compmethod(self):
        return f"The company name is {self.name}."


class Coder:
    language = "Python"

    def __init__(self):
        print("This is Coder Class.")

    def codermethod(self):
        return f"Your coding language is {self.language}."


class Programmer(Coder, Company):
    ename = "Akhand"
    salary = 2000000

    def __init__(self):
        super().__init__()
        print("This is Programmer class.")

    def programmethod(self):
        return f"The employee {self.name} is getting {self.salary}."


pobject = Programmer()
print(pobject.programmethod(), pobject.compmethod(), pobject.compmethod())
