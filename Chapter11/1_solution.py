# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector(self):
        print(f"Vector : {self.x}i + {self.y}j")


class ThreeDVector(TwoDVector):
    z = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def vector(self):
        print(f"Vector : {self.x}i + {self.y}j + {self.z}k")


a = TwoDVector(1, 2)
b = ThreeDVector(1, 2, 3)

a.vector()
b.vector()
