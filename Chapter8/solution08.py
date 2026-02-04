# Write a python function to print multiplication table of a given number

def multiplication(n):
    for i in range(10):
        print(f"{n}*{i + 1}={n * (i + 1)}")


num = int(input("Enter the number for table : "))

multiplication(num)
