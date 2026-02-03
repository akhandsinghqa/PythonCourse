# Write a program to make a copy of a text file “this. txt”

with open("copyfile.txt","w") as wf:
    with open("this.txt","r") as rf:
        wf.write(rf.read())