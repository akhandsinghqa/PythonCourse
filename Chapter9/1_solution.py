# Write a program to read the text from a given file 'poems.txt' and find out
# whether it contains the word 'twinkle'.

with open("poem.txt", "r") as f:
    text = f.read().lower()

if "twinkle" in text:
    print("This file contains the twinkle in it.")
else:
    print("This file does not contains the twinkle in it.")
# print(f"************************\n{text}\n************************\n")
# isTwinkle = text.find('twinkle')
# numTwinkle = 0
# if isTwinkle >= 0:
#     numTwinkle = text.count('twinkle')
#
# print(f"Number of twinkle in poem : {numTwinkle}")
