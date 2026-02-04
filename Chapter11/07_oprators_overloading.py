class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, n):
        return self.num + n.num


a = Number(7)
b = Number(8)

print(b + a)
