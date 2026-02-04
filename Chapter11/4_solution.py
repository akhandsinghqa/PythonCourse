# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class ComplexNum:

    def __init__(self, num):
        self.num = num

    def __add__(self, b):
        x = self.num
        y = b.num
        return f"{(x.real + y.real)}+{(x.imag + y.imag)}j"

    def __mul__(self, b):
        x = self.num
        y = b.num
        return f"{(x.real * y.real) - (x.imag * y.imag)}+{(x.real * y.imag) + (x.imag * y.real)}j"


c = ComplexNum((2 + 3j))
d = ComplexNum((5 + 4j))

print(c + d)
print(c * d)
