# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if a > b:
    if a > c:
        if a > d:
            print("Greatest number is : ", a)
        else:
            print("Greatest number is : ", d)
    elif c > d:
        print("Greatest number is : ", c)
    else:
        print("Greatest number is : ", d)
elif b > c:
    if b > d:
        print("Greatest number is : ", b)
    else:
        print("Greatest number is : ", d)
elif c > d:
    print("Greatest number is : ", c)
else:
    print("Greatest number is : ", d)

print("End of program")
