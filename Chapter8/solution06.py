# Write a python function which converts inches to cms

def inch_to_cms(inches):
    return round(inches*2.54,2)

inch=int(input("Enter the inches : "))

print(f"{inch} in centimers : {inch_to_cms(inch)}")