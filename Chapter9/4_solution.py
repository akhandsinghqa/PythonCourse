# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file

word = 'donkey'
with open("OriginalFile.txt", "r") as rf:
    text = rf.read().lower()

if word in text:
    text = text.replace(word, '#'*len(word))
    with open("OriginalFile.txt", "w") as wf:
        wf.write(text)
    print("The word donkey replaced by ##### in the OriginalFile.txt")
else:
    print("The word donkey not present in the OriginalFile.txt")