#  Write a program to filter a list of numbers which are divisible by 5.

lsts = [5, 7, 18, 25, 60, 34, 75, 2334675, 4242350, 3213, 5435]

print(list(filter(lambda x: x % 5 == 0, lsts)))
