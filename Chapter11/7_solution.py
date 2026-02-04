# Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class Nvector:
    def __init__(self, v):
        self.v = v

    def __len__(self):
        return len(self.v)


nvector = Nvector([1, 2, 3, 4, 5])
print(len(nvector))
