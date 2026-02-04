# Write a python function to remove a given word from a list ad strip it at the same time.

def removeFromList(lst, word):
    newlst = []
    for item in lst:
        if (item != word):
            newlst.append(item.strip(word))
    return newlst


listOfWords = ["Akhand", "Pratap", "Singh", "gh", "NoName"]
print(removeFromList(listOfWords, "gh"))
