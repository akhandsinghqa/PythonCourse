# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subone = int(input("Enter Makrs : "))
subtwo = int(input("Enter Makrs : "))
subthree = int(input("Enter Makrs : "))

total_percentage = ((subone + subtwo + subthree) / 300) * 100

if subone >= 33 and subtwo >= 33 and subthree >= 33 and total_percentage >= 40:
    print("Congrats, The student is passed. ", total_percentage)
else:
    print("Sorry. The student failed. ", total_percentage)
print("Program ended.")
