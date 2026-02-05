# Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

try:
    qua_num = num_one / num_two
    print(qua_num)
except ZeroDivisionError:
    print("This is infinite as first number is divided by 0.")
