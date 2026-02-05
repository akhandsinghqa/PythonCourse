def divide_func(a, b):
    print(a / b)


try:
    divide_func(4, 2)
except ZeroDivisionError:
    print("This function can not divide by 0, please add input again")
except Exception as e:
    print(e)
finally:
    print("Program execution done.")
