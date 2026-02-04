# Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class Nvector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}i + {self.b}j + {self.c}k"


print(Nvector(7, 8, 10))
