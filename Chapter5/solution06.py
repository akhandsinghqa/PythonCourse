# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# If the names of 2 friends are same; what will happen to the program in problem 6?
# If languages of two friends are same; what will happen to the program in problem 6 ?

d = {}

for i in range(4):
    key = input("Enter your name : ")
    value = input("Enter you favorite : ")
    d.update({key: value})

print(d.items())
