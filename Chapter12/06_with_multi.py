# with open("first.txt","r") as rf:
#     print(rf.read())

with (open("first.txt", "r") as f, open("second.txt", "r") as s):
    print(f.read())
    print(s.read())
