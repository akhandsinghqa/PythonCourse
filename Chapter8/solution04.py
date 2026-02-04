# Write a recursive function to calculate the sum of first n natural numbers.

def sumOfNumber(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return n + sumOfNumber(n - 1)


num = int(input("Enter the number for sum : "))

print(f"Sum of first {num} natural numbers is {sumOfNumber(num)}")
