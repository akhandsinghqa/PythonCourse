# Repeat program 4 for a list of such words to be censored.

words = ['donkey','hello']
with open("OriginalFile.txt", "r") as rf:
    text = rf.read().lower()
for word in words:
    if word in text:
        text = text.replace(word, '#'*len(word))
        with open("OriginalFile.txt", "w") as wf:
            wf.write(text)
        print(f"The word {word} replaced by ##### in the OriginalFile.txt")
    else:
        print(f"The word {word} not present in the OriginalFile.txt")