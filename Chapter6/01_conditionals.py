age = int(input("Enter your age : "))

if age < 0:
    print("Enter the valid age. It cann't be nagative. ", age)
elif age == 0:
    print("Enter valid age. Age cann't be zero. ", age)
elif age < 18:
    print("You are under age. Good Bye. ", age)
else:
    print("You are welcome. ", age)

print("End of the program.")
