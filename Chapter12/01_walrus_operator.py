# Using walrus operator

if (n := len([1, 2, 3, 4, 5, 6])) > 3:
    print(f"There are {n} elements , expected <=3")

if (num := 3 * 4) > 10:
    print(f"The {num} is greater then 10")
