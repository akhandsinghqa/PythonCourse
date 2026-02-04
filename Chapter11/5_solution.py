# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them

class Nvector:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        x = self.vector
        y = other.vector
        if len(x) == len(y):
            z = []
            for i in range(len(x)):
                z.append(x[i] + y[i])
            return z
        else:
            return f"Both vector are of different size"

    def __mul__(self, other):
        x = self.vector
        y = other.vector
        if len(x) == len(y):
            total=0
            for i in range(len(x)):
                total+=x[i] * y[i]
            return total
        else:
            return f"Both vector are of different size"


a = Nvector([1, 3, -8, 4, 7])
b = Nvector([3, 8, -8, -12, 6])

print(a + b)
print(a * b)
