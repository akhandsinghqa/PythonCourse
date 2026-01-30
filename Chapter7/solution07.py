# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = 10
for i in range(1, n + 1):
    print(" " * (n - i), "*" * ((2 * i) - 1), sep="")


# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = 10
for i in range(1, n + 1):
    print("*" * (i), sep="")

# Write a program to print the following star pattern.
# * * *
# *   *  for n = 3
# * * *
m = 10

for i in range(1, m + 1):
    if(i==1 or i==m):
        print("*"*m,sep="")
    else:
        print("*"," "*(m-2),"*",sep="")