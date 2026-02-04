# Write a program using functions to find greatest of three numbers.

def greatest(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    if (num2 > num3):
        return num2
    else:
        return num3


a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

print(greatest(a, b, c))
