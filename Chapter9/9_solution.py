# Write a program to find out whether a file is identical & matches the content of
# another file.

with open("copyfile.txt", "r") as wf:
    with open("this.txt", "r") as rf:
        is_identical = wf.read() == rf.read()

if is_identical:
    print("Both files are identical.")
else:
    print("files are not identical")
