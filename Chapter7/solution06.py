# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter the number for factorail calculation: "))  # 5*4*3*2*1=120
total=1
for i in range(num):
    total*=num-i

print(total)