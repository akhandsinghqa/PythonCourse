# Write a program to accept marks of 6 students and display them in a sorted manner.

marks_of_students = []

for i in range(6):
    marks_of_students.append(int(input(f"Enter the mark of {i + 1} student :")))

marks_of_students.sort()
print("Marks of the students :\n", marks_of_students)

# print("Marks of the students in sorted order :\n",marks_of_students.sort() )
