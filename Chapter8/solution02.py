# Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(temp):
    return round((temp*(9/5))+32,2)

ftemp=int(input("Enter the temp in celsius : "))

print(f"Temp in fahrenheit : {celsius_to_fahrenheit(ftemp)} °F")

