# Write a program to fill in a letter template given below with name and date

name = input("Enter your name, please : ")
date = input("Enter your name, please : ")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# letter.replace("<|Name|>",name).replace("<|Date|>",date) should store in 
# other variable as string is immutable

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
