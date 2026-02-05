# Store the multiplication tables generated in problem 3 in a file named Tables.txt.
try:
    num = int(input("Enter the number for table : "))
    with open("tables.txt", "w") as table:
        table.write(f"Table of {num} :\n{[num * i for i in range(1, 11)]}")
except ValueError:
    print("Please enter the valid positive integer.")
