# Write a python function to print first n lines of the following pattern:
# ***
# **  for n=3
# *

# def pattern(n):
#     for i in range(n):
#         print("*"*(n-i),sep="")

def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    return pattern(n - 1)


pattern(10)
