# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
# Add a static method in problem 2, to greet the user with hello.

class Calculator:

    def __init__(self, num):
        self.num = num

    def sequareofnum(self):
        return print("The square is : ", self.num ** 2)

    def cobeofnum(self):
        return print("The cube is : ", self.num ** 3)

    def squarerootofnum(self):
        return print("The squareroot is : ", self.num ** 0.5)

    @staticmethod
    def greet():
        print("Hi, your calculations are as follows :")


numforcalc = int(input("Enter the number for calculation : "))
calcnum = Calculator(numforcalc)

calcnum.greet()
calcnum.sequareofnum()
calcnum.cobeofnum()
calcnum.squarerootofnum()
