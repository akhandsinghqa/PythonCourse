# Write a program which finds out whether a given name is present in a list or not

lst=["Akhand","Pratap","Singh", "Ravi", "Deepak"]

name=input("Enter the name : ")

# if(lst.count(name)>0):
if(name in lst):
    print("This name is present in the list. ", name)
else:
    print("This name is not in the list. ", name)

print("End of program.")
