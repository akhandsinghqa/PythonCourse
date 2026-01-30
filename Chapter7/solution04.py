# Write a program to find whether a given number is prime or not.

num = int(input("Enter the number to check for prime : "))

till = int(num / 2) + 1

is_prime = True

if num <= 1:
    print(num, " is not prime.")
else:
    for i in range(2, till):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, " is prime.")
    else:
        print(num, " is not prime")
