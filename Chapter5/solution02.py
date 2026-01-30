#  Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s=set()
print("Please enter the eight numbers :")
for i in range(8):
    s.add(int(input(f"{i+1} num : ")))

print("The unique numbers ",s)