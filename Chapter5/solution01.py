# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up

trans = {
    "seb": "Apple",
    "Kela": "Banana",
    "Dimag": "Brain",
    "Hindi": "English"
}

key = input("Enter the hindi word : ")
print(trans.get(key))
