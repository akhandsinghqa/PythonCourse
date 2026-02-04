class ParentClass:
    def parentMethod(self):
        print("This is parent class.")


class ChildClass(ParentClass):
    def childMethod(self):
        print("This is child class.")


a = ParentClass()
b = ChildClass()

a.parentMethod()
b.parentMethod()
b.childMethod()
