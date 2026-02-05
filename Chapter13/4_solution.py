# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

# def max_num(a, b):
#     if a > b:
#         return a
#     else:
#         return b


lsts = [2, 54, 8686, 878, 23131, 757, 464]
print(reduce(lambda x, y: x if x > y else y, lsts))
