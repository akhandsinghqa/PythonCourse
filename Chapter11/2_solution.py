# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self):
        print("This is Animals class.")


class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("This is Pets Class.")


class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("This is Dog class.")

    @staticmethod
    def bark():
        print("Dog makes barking sound.")


a = Animals()
b = Pets()
c = Dog()
c.bark()
