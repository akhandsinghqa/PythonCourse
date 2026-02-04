# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, designation, language, salary, doj):
        self.name = name
        self.designation = designation
        self.language = language
        self.salary = salary
        self.doj = doj

    def getprogammerinfo(self):
        print(self.company, self.name, self.designation, self.language, self.salary, self.doj)


emp1 = Programmer("Akhand", "SDET", "Java", 1500000, "14 Jan 2022")
emp2 = Programmer("Pratap", "Dev", "Python", 2000000, "14 Feb 2025")
emp3 = Programmer("Singh", "Manager", "Jira", 2500000, "14 Dec 2021")
emp4 = Programmer("New", "Test", "C++", 2100000, "14 April 2024")

emp1.getprogammerinfo()
emp2.getprogammerinfo()
emp3.getprogammerinfo()
emp4.getprogammerinfo()
