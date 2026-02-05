def divide_func(a, b):
    if b == 0:
        raise ZeroDivisionError("You can not divide by zero")
    print(a / b)


try:
    divide_func(4, 0)
# except ZeroDivisionError:
#     print("This function can not divide by 0, please add input again")
except Exception as e:
    print(e)
finally:
    print("Program execution done.")
