class Employee:
    name = "Dummy"
    language = "Java"
    salary = 1200000

    def __init__(self, name, salary, language):
        print("This is init method/constructor.")
        self.name = name
        self.salary = salary
        self.language = language

    def getinfo(self):
        print(self.name, self.salary, self.language)

    @staticmethod
    def greet():
        print("Hello ! Your in class.")


akhand = Employee("Akhand Pratap Singh", 1300000, "Python")
# akhand.name='Akhand Pratap Singh'
# print(akhand.name,akhand.language,akhand.salary)
akhand.getinfo()
# akhand.greet()
Employee.greet()
