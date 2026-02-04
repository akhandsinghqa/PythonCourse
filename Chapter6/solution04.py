# Write a program to find whether a given username contains less than 10
# characters or not.

usrname = input("Enter the username : ")

if len(usrname) < 10:
    print("This user name has less than 10 characters,", usrname)
else:
    print("This user name has 10 or more characters,", usrname)

print("End of program")
