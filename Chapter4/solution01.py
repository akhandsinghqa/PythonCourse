# Write a program to store seven fruits in a list entered by the user.

list_of_fruits = []
print("Enter seven fruit names : ")
for i in range(7):
    list_of_fruits.append(input(f"{i + 1}:"))

print(list_of_fruits)
